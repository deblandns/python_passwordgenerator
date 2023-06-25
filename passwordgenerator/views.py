from django.shortcuts import render , redirect
import random
from .models import passgenerator
import string
from django.views import View
from django.views.generic.base import TemplateView
from .models import passgenerator
from .forms import passgeneratormodelform
# Create your views here.


class homepageView(View):
    def get(self , request):
        form = passgeneratormodelform()
        return render(request , "homepage.html" , {"form" : form } )


    def post(self , request):
        form = passgeneratormodelform(request.POST)
        if form.is_valid():
            availiable_charectors = string.digits + string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase + string.punctuation
            password = ''.join(random.choice(availiable_charectors)for i in range(form.cleaned_data["number"]))
            return render( request, "homepage.html" , {"form" : form , "password" : password})




def header_components(request):
    return render(request , "shared/header_component.html" , {})

def footer_component(request):
    return render(request , "shared/footer_component.html" , {})








