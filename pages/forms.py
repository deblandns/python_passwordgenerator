from django import forms
from .models import contactus


class contactUsmodelform(forms.ModelForm):
    class Meta :
        model = contactus
        fields = ["name" , "email" , "message"]

        widgets = {
                    "name" : forms.TextInput(attrs={"class" : "inputs"}),
                    "email" : forms.EmailInput(attrs={"class": "inputs"}),
                    "message": forms.Textarea(attrs={"class": "inputs"}),


        }
        labels = {
            "name" : "NAME",
            "email" : "EMAIL" ,
            "message" : "MESSAGE"
        }


