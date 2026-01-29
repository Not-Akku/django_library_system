from django.db import models
from django.core.validators import MinValueValidator, RegexValidator
from datetime import timedelta
from django.utils import timezone

class Reader(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    date_of_membership = models.DateField(auto_now_add=True)
    fine_pending = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, validators=[MinValueValidator(0)])

    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    isbn = models.CharField(
        max_length=13, 
        unique=True,
        validators=[RegexValidator(
            regex=r'^(?:97[89]\d{10}|\d{9}[\dX])$',
            message='Enter a valid ISBN-10 or ISBN-13'
        )]
    )
    available_for_loan = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} (ID: {self.pk or 'new'})"
    
class Loan(models.Model):
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    loan_date = models.DateField(auto_now_add=True)
    due_date = models.DateField(null=True, blank=True)
    return_date = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.due_date:
            self.due_date = timezone.now().date() + timedelta(days=14)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.book.title} loaned to {self.reader.name}"