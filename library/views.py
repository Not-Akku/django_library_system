from django.shortcuts import render
from . forms import LendingForm , ReturnForm, FineSystem
from . models import Reader, Loan, Book
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta
from decimal import Decimal, DecimalException

# Fine calculation constants
DAILY_FINE_RATE = Decimal('0.50')
BASE_FINE_AMOUNT = Decimal('25.00')

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
                    
                        Loan.objects.create(
                            reader = the_reader,
                            book = the_book
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

def _calculate_overdue_fine(overdue_days):
    """Calculate fine for overdue books."""
    fine_interest = Decimal(str(overdue_days)) * DAILY_FINE_RATE
    return fine_interest + BASE_FINE_AMOUNT

def return_book(request):
    form = ReturnForm()
    if request.method == 'POST':
        form = ReturnForm(request.POST)
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
                    overdue_days = time_difference.days
                    total_fine = _calculate_overdue_fine(overdue_days)

                    reader = loan.reader
                    reader.fine_pending += total_fine
                    reader.save()
                    
                    messages.warning(request, f"Book returned late. Fine of ₹{total_fine} added to your account.")
                else:
                    messages.success(request, "Book returned successfully!")
                
                # Mark loan as returned and make book available
                loan.return_date = timezone.now()
                loan.save()
                book = loan.book
                book.available_for_loan = True
                book.save()

            except Loan.DoesNotExist:
                messages.error(request, f"No active loan found for book ID {book_id}")
            except (ValueError, TypeError, AttributeError) as e:
                messages.error(request, f"Invalid data provided: {e}")
            except Exception as e:
                messages.error(request, "An unexpected error occurred. Please try again.")

    return render(request, 'lib/return.html', {'form': form})



def _validate_fine_payment(fine_amount, pending_fine):
    """Validate fine payment amount and return error message if invalid."""
    if fine_amount <= 0:
        return "Payment amount must be greater than zero"
    if fine_amount > pending_fine:
        return f"Payment amount (₹{fine_amount}) exceeds pending fine (₹{pending_fine})"
    return None

def _process_fine_payment(reader, fine_amount):
    """Process fine payment and return success message."""
    reader.fine_pending -= fine_amount
    reader.save()
    
    remaining_fine = reader.fine_pending
    success_msg = f"Fine payment of ₹{fine_amount} processed."
    if remaining_fine > 0:
        success_msg += f" Remaining fine: ₹{remaining_fine}"
    else:
        success_msg += " All fines cleared!"
    return success_msg

def fine(request):
    form = FineSystem()
    if request.method == 'POST':
        form = FineSystem(request.POST)
        if form.is_valid():
            try:
                reader_id = form.cleaned_data['reader_id']
                fine_amount = form.cleaned_data['fine']
                
                reader = Reader.objects.get(pk=reader_id)
                
                error_msg = _validate_fine_payment(fine_amount, reader.fine_pending)
                if error_msg:
                    messages.error(request, error_msg)
                else:
                    success_msg = _process_fine_payment(reader, fine_amount)
                    messages.success(request, success_msg)
                        
            except Reader.DoesNotExist:
                messages.error(request, "Invalid reader ID")
            except (ValueError, TypeError, DecimalException) as e:
                messages.error(request, f"Invalid data provided: {e}")
            except Exception as e:
                messages.error(request, "An unexpected error occurred. Please try again.")
    
    return render(request, 'lib/fine.html', {'form': form})