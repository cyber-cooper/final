from django import forms
from.models import Tarea
class TF(forms.ModelForm):

	class Meta:
		model =Tarea
		fields =['tarea']
		