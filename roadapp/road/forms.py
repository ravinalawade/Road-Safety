from .models import Update
from django import forms


class Updateform(forms.ModelForm):
	class Meta:
		model = Update
		exclude = ()