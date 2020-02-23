from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm

# Create your views here.
# sendemail/views.py
def pdf1(request):
    return render(request, "MCN/PDF/TREGUESIT_INTERNET_VITI_2019.pdf")
def pdf2(request):
    return render(request, "MCN/PDF/TREGUESIT_TELEFONIKE_VITI_2019.pdf")
def homepage(request):
    return render(request,"MCN/index.html")
def internet(request):
    return render(request,"MCN/internet.html")
def telefoni(request):
    return render(request,"MCN/telefoni.html")
def design(request):
    return render(request,"MCN/webdesign.html")
def networking(request):
    return render(request,"MCN/networking.html")
def software(request):
    return render(request,"MCN/software.html")
def trainime(request):
    return render(request,"MCN/trajnime.html")
def kontakt(request):
    return render(request,"MCN/kontakt.html")

def emailView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['E_mail']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['yllcaka1516457@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('../success/')
    return render(request, "MCN/kontakt.html", {'form': form})

def successView(request):
    return render(request,"MCN/redirect.html")


def tripi_me_email(request):
    Emri = request.POST.get('Emri')

    E_mail= request.POST.get('E-mail')

    subjekti = request.POST.get('subjekti')

    kategoria = request.POST.get('kategoria')

    message = request.POST.get('message')

    context = {'Emri': Emri , 'E-mail': E_mail ,
               'subjekti': subjekti , 'kategoria': kategoria ,
               'message': message}
    content = f"{kategoria}\n{message}\nNga: {Emri}."
    # if request.method == 'GET':
    #     form = ContactForm()
    # else:
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            # subject = form.cleaned_data['subject']
            # from_email = form.cleaned_data['E_mail']
            # message = form.cleaned_data['message']
            try:
                send_mail(subjekti, content, E_mail, ['yllcaka1516457@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('../success/')
    return render(request , 'MCN/kontakt.html' , {'form': form})
