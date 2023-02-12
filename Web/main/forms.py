from .models import vote
from django.forms import ModelForm, TextInput, Textarea

class voteForms(ModelForm):
    class Meta:
        model =vote
        fields = ['name','full_text']

        widgets= {
            "name": TextInput(attrs={
                'class':'form-control',
                'placeholder':'Название'
            }),
            "full_text":Textarea(attrs={
                    'class':'form-control',
                    'placeholder':'Описание'
            })
        }
