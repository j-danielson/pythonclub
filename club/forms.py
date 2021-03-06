from itertools import product
from socket import fromshare
from django import forms
from .models import Meeting, Resource

class ResourceForm(forms.ModelForm):
    class Meta:
        model=Resource
        fields='__all__'

class MeetingForm(forms.ModelForm):
    class Meta:
        model=Meeting
        fields='__all__'