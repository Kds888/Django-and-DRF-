from django.db import models

# Create your models here.


class student(models.Model):
    # Student Id field is created automatically
    first_name=models.CharField(max_length=50)
    last_name= models.CharField(max_length=50)
    amount_due= models.IntegerField()
    dob= models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"