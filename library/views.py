from django.shortcuts import render
from . forms import LendingForm
from . models import Reader, Loan, Book
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta #to calculate due date...

# Create your views here.

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