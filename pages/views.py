from django.shortcuts import render , redirect
from .forms import contactUsmodelform
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
# Create your views here.

class aboutus(TemplateView):
    template_name = "aboutus.html"
    
# def aboutus(request):
#     return  render(request , "aboutus.html")
class callus(CreateView):
    template_name = "callus.html"
    form_class = contactUsmodelform
    success_url = "/"
    context_object_name = "form"


# def callus(request) :
#     contact_form = contactUsmodelform()
#     if request.method == "POST":
#         contact_form = contactUsmodelform(request.POST)
#         if contact_form.is_valid():
#             contact_form.save()
#             return redirect("homepage")
#         else:
#             contact_form = contactUsmodelform()
#     return render(request , "callus.html" , {"contact_form" : contact_form} )






