from django.shortcuts import render
from .forms import registerForm
from django.http import HttpResponseRedirect
from django.contrib import messages
# Create your views here.


def register(request):
    #check if the method get or post
    if request.method=='GET':
        form1=registerForm()
    else:
        form1=registerForm(request.POST)
        if form1.is_valid():
            form1.save()
            #giving a success message for the user
            messages.success(request,'user created successfully!!')
            #redirecting user to the same page
            return HttpResponseRedirect(request.path_info)
    return render(request,'reg.html',{'form':form1})