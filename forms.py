from .models import Database1
from django import forms
class GetForm(forms.ModelForm):
    status=((1,_("java")),(2,("python 3.9")))
    lang=forms.ChoiceField(choices=status)
	class Meta:
		model=Database1
		fields="__all__"