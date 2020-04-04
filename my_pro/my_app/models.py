from django.db import models

# Create your models here.

from django.db import models    # importing models 
class Book(models.Model):       
    book_title = models.CharField(max_length=100, blank=True, null=True)
    book_description = models.CharField(max_length=500, blank=True, null=True)
    def __str__(self):
        return str(self.book_title )

