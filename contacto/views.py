from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm
from core.settings import EMAIL_HOST_USER



# Create your views here.
def contact(request):
 

    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            #enviamos el correo y redireccionamos
            email = EmailMessage("Ugt Brake: Nuevo mensaje de contacto",
                                 "De {} <{}>\n\nEscribió:\n\n{}".format(name, email, content),
                                  EMAIL_HOST_USER,
                ["brake@gmail.com"],
                reply_to=[email])
            # Lo enviamos y redireccionamos
            try:
                email.send()
                # Todo ha ido bien, redireccionamos a OK
                return redirect(reverse('contacto:contacto') + "?ok")
            except:
                # Algo no ha ido bien, redireccionamos a FAIL
                return redirect(reverse('contacto:contacto') + "?fail")

    context = {
        'form': contact_form,
      
    }

    print(contact_form)

    return render(request, "contacto/contacto.html", context)
