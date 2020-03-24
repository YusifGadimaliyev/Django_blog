from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

# Create your views here.


def contactView(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            message = form.cleaned_data.get('message')
            form.save()
            messages.success(request, "We have recieved your message successfully!")
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})