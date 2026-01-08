from django import forms



class LendingForm(forms.Form):
    reader_id = forms.IntegerField()
    book_id = forms.IntegerField()

class ReturnSystem(forms.Form):
    book_id = forms.IntegerField()

class fineSystem(forms.Form):
    fine = forms.IntegerField()
