from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm

# Create your views here.
# sendemail/views.py
def bigkontakt(request):
    return render(request,"MCN/kontaktim.html")
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

# def emailView(request):
#     if request.method == 'GET':
#         form = ContactForm()
#     else:
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             subject = form.cleaned_data['subject']
#             from_email = form.cleaned_data['E_mail']
#             message = form.cleaned_data['message']
#             try:
#                 send_mail(subject, message, from_email, ['yllcaka1516457@gmail.com'])
#             except BadHeaderError:
#                 return HttpResponse('Invalid header found.')
#             return redirect('../success/')
#     return render(request, "MCN/kontakt.html", {'form': form})

def successView(request):
    return render(request,"MCN/redirect.html")

def tripi_madh_me_email(request):
    #Prejqituhit jon kto name te forma e madhe
    person = request.POST.get("person")
    company = request.POST.get("company")
    nipt = request.POST.get("nipt")
    tel = request.POST.get("tel")
    cel = request.POST.get("cel")
    faks = request.POST.get("faks")
    address = request.POST.get("address")
    message1 = request.POST.get("message1")
    message2 = request.POST.get("message2")
    message3 = request.POST.get("message3")
    color1 = request.POST.get("color1")
    konkurent1 = request.POST.get("konkurent1")
    gjuhet1 = request.POST.get("gjuhet1")
    ngjyrat = request.POST.get("ngjyrat")
    domain = request.POST.get("domain")
    time = request.POST.get("time")
    natyra = request.POST.get("natyra")
    funksionalitet = request.POST.get("funksionalitet")
    grupfjalet = request.POST.get("grupfjalet")
    pagenr = request.POST.get("pagenr")
    #deri qitu
    context = {'Emri dhe Mbiemri': person , 'company': company ,
               'nipt': nipt , 'tel': tel ,
               'cel': cel,'faks': faks,'address': address,
               'message1': message1,'message2': message2,'message3': message3,
               'color1': color1,'konkurent1': konkurent1,'gjuhet1': gjuhet1,
               'ngjyrat': ngjyrat,'domain': domain,'time': time,
               'natyra': natyra,'funksionalitet': funksionalitet,'grupfjalet': grupfjalet,
               'pagenr': pagenr,}
    for k,v in context.items():
        if k == "subjekti" or k == "kategoria":
            continue
        content+= f"{k.capitalize()}:\n\t{str(v).capitalize()}\n"
    subjekti = f"{company}({person})"

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
    return render(request , 'MCN/kontaktim.html' , {'form': form})

def tripi_me_email(request):
    Emri = request.POST.get('Emri')

    E_mail= request.POST.get('E-mail')

    subjekti = request.POST.get('subjekti')

    kategoria = request.POST.get('kategoria')

    message = request.POST.get('message')

    context = {'Emri dhe Mbiemri': Emri , 'E-mail': E_mail ,
               'subjekti': subjekti , 'kategoria': kategoria ,
               'message': message}
    content = f""
    for k,v in context.items():
        if k == "subjekti" or k == "kategoria":
            continue
        content+= f"{k.capitalize()}:\n\t{str(v).capitalize()}\n"
    # if request.method == 'GET':
    #     form = ContactForm()
    # else:
    subjekti = f"{subjekti}({kategoria})"
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
