from django.db import models

# Create your models here.



class String_Concatenation(models.Model):
    string1 = models.CharField(max_length=128, blank=True)
    string2 = models.CharField(max_length=128, blank=True)


class String_Multiplication(models.Model):
    string_for_multiplication = models.CharField(max_length=128)
    n = models.IntegerField()
