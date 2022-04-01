from django import forms
from django.forms import ModelForm
from .models import Event

class EventForm(ModelForm):
	class Meta:
		model = Event
		fields = ('name', 'event_date', 'attendees', 'description')
		labels = {
			'name': '',
			'event_date': 'YYYY-MM-DD HH:MM:SS',
			# 'venue': 'Venue',
			'attendees': 'Attendees',
			'description': '',			
		}
		widgets = {
			'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Event Name'}),
			'event_date': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Event Date'}),
			# 'venue': forms.Select(attrs={'class':'form-select', 'placeholder':'Venue'}),
			'attendees': forms.SelectMultiple(attrs={'class':'form-control', 'placeholder':'Attendees'}),
			'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Description'}),
		}