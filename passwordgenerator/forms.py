from django import forms
from .models import passgenerator



class passgeneratormodelform(forms.ModelForm) :
    class Meta :
        model = passgenerator
        fields = ["number" ]

        widgets = {
                "number" : forms.NumberInput(attrs={"class" : "input" ,'type': 'range' , "min" : "1" , "max" : "20" , "value" : "8" ,"id" : "myRange"})

        }
