from django import forms
from django.core.exceptions import ValidationError

class LendingForm(forms.Form):
    reader_id = forms.IntegerField(label="Reader ID", min_value=1)
    book_id = forms.IntegerField(label="Book ID", min_value=1)
    
    def clean_reader_id(self):
        reader_id = self.cleaned_data['reader_id']
        if reader_id <= 0:
            raise ValidationError("Reader ID must be a positive number")
        return reader_id
    
    def clean_book_id(self):
        book_id = self.cleaned_data['book_id']
        if book_id <= 0:
            raise ValidationError("Book ID must be a positive number")
        return book_id

class ReturnForm(forms.Form):
    book_id = forms.IntegerField(label="Book ID", min_value=1)
    
    def clean_book_id(self):
        book_id = self.cleaned_data['book_id']
        if book_id <= 0:
            raise ValidationError("Book ID must be a positive number")
        return book_id

class FineSystem(forms.Form):
    reader_id = forms.IntegerField(label="Reader ID", min_value=1)
    fine = forms.DecimalField(max_digits=10, decimal_places=2, label="Fine Amount (₹)", min_value=0.01)
    
    def clean_reader_id(self):
        reader_id = self.cleaned_data['reader_id']
        if reader_id <= 0:
            raise ValidationError("Reader ID must be a positive number")
        return reader_id
    
    def clean_fine(self):
        fine = self.cleaned_data['fine']
        if fine <= 0:
            raise ValidationError("Fine amount must be greater than zero")
        return fine
