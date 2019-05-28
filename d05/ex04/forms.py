from django import forms

class my_form(forms.Form):
	text = forms.CharField(label='',max_length=64)
