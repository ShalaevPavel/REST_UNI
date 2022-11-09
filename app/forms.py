from django.forms import ModelForm
from django.forms import forms
from .models import String_Concatenation, String_Multiplication

class String_ConcatenationForm(ModelForm):

    class Meta:
        model = String_Concatenation
        fields = ('string1', 'string2')


class String_MultiplicationForm(ModelForm):

    class Meta:
        model = String_Multiplication
        fields = ('string_for_multiplication', 'n')
