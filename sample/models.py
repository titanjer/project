from django.db import models

# Create your models here.
from django.db import models
from django import forms

from formfield import ModelFormField

class PersonMetaForm(forms.Form):
    age = forms.IntegerField()
    sex = forms.ChoiceField(choices=((1, 'male'), (2, 'female')), required=False)


class Person(models.Model):
    name = models.CharField(max_length=200)

    meta_info = ModelFormField(PersonMetaForm)
