from django import forms


class LendingForm(forms.Form):
    reader_id = forms.IntegerField()
    book_id = forms.IntegerField()