from django.shortcuts import render
from . forms import LendingForm , ReturnSystem, fineSystem
from . models import Reader, Loan, Book
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta #to calculate due date...

# Create your views here.

# view logics for leading book 
def lend(request):
    form = LendingForm()

    if request.method == 'POST':
        form = LendingForm(request.POST)
        if form.is_valid():
            book_id = form.cleaned_data['book_id']
            reader_id = form.cleaned_data['reader_id']
            try:
                the_reader = Reader.objects.get(pk = reader_id)
                the_book = Book.objects.get(pk = book_id)

                if the_reader.fine_pending > 0:
                    messages.error(request, "sorry you have some fines pending!")
                else:

                    if the_book.available_for_loan:
                    
                        borrow_date = timezone.now()
                        due_date = borrow_date + timedelta(days=14)

                        Loan.objects.create(
                            reader = the_reader,
                            book = the_book,
                            loan_date = borrow_date,
                            due_date = due_date
                            )
                        
                        the_book.available_for_loan = False
                        the_book.save()

                        messages.success(request,f"Book '{the_book.title}' loaned successfully to {the_reader.name}.")
                    else:
                        messages.error(request,"sorry the book is not available!")
                

            
            except Reader.DoesNotExist:
                messages.error(request, 'invalid reader id!')

            except Book.DoesNotExist:
                messages.error(request, 'invalid book id!')

            

    return render(request, 'lib/lend.html', {'form': form})

def return_book(request):
    form = ReturnSystem()
    if request.method == 'POST':
        form = ReturnSystem(request.POST)
        if form.is_valid():
            book_id = form.cleaned_data['book_id']
            try:
                # check the loans db with the same id and recent loan.
                loan = Loan.objects.get(
                    book_id = book_id,
                    return_date__isnull = True
                )
                today = timezone.now().date()
                due_date = loan.due_date

                if today > due_date:
                    time_difference = today - due_date
                    overdue = time_difference.days
                    fine_interest = overdue * 0.5
                    total_fine = fine_interest + 25

                    reader = loan.reader
                    reader.fine_pending += total_fine
                    reader.save()
            
                else:

                    messages.error(request)
                    # mark loan returned
                    loan.return_date = timezone.now()
                    loan.save()
                    # update the book availability in book db
                    book = loan.book
                    book.available_for_loan = True
                    book.save()

            except Loan.DoesNotExist:
                messages.error(request, f"No active loan found for book ID {book_id}")

            except Exception as e:
                messages.error(request, f"An unexpected error occured: {e}")

    return render(request, 'lib/return.html', {'form': form})



def fine(request):
    form = fineSystem()
    if request.method == 'POST':
        form = fineSystem(request.POST)
        if form.is_valid():
            fine = form.cleaned_data['fine']