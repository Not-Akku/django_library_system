from django.db import models

# Create your models here.

class Reader(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    date_of_membership = models.DateField()

    def __str__(self):
        return self.name
    
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13)
    available_for_loan = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} (copy: {self.id})"
    
class Loan(models.Model):
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    loan_date = models.DateField(auto_now_add=True)
    due_date = models.DateField(null=True)
    return_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.book.title} loaned to {self.reader.name}"