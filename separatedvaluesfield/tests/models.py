from django.db import models

from separatedvaluesfield.models import SeparatedValuesField


class Project(models.Model):
    name = models.CharField(max_length=150)
    languages = SeparatedValuesField(max_length=150, choices=(('en', 'English'),
                                                              ('fr', 'French')), blank=True)


class RequiredProject(models.Model):
    name = models.CharField(max_length=150)
    languages = SeparatedValuesField(max_length=150, choices=(('en', 'English'),
                                                              ('fr', 'French')))
