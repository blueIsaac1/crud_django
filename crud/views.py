from django.shortcuts import render, redirect, get_object_or_404
from crud.models import Contact
from crud.forms import ContactForm

def home(request):
    return render(request, 'crud/home.html')

def contactlist(request):
    contact = Contact.objects.all()
    return render(request, 'crud/contactlist.html', {"contact": contact})

def forms(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('forms')
    else:
        form = ContactForm()
    return render(request, 'crud/forms.html', {"form": form})

def contact_create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contactlist')
    else:
        form = ContactForm()
    return render(request, 'crud/forms.html', {"form": form})

def contact_update(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contactlist')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'crud/forms_update.html', {"form": form})

def contact_delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('contactlist')
    return render(request, 'crud/confirm_contact_delete.html', {'contact': contact})