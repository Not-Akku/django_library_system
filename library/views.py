from django.shortcuts import render
from . forms import LendingForm , ReturnSystem
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

                if the_book.available_for_loan:
                
                    borrow_date = timezone.now()
                    due_date = borrow_date + timedelta(days=14)

                    new_loan = Loan.objects.create(
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
                
                # mark loan returned
                loan.return_date = timezone.now()
                loan.save()
                # update the book availability in book db
                book = loan.book
                book.available_for_loan = True
                book.save()
            except:
                messages.error(request, f"there is no book with {book_id} book id.")
    return render(request, 'lib/return.html', {'form': form})

