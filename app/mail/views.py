from django.shortcuts import render, redirect
from django.core.mail import EmailMessage, get_connection
from .models import EmailTracked, Destinatario
from django.utils import timezone
from django.http import HttpResponse
from django import forms
from .funcs import send_tracked_email, send_custom_tracked_email
from os import listdir, path, makedirs
from django.conf import settings
import base64
import traceback
# Create your views here.

BASE_DIR = settings.BASE_DIR

def track_email_view(request, email_id):
    print("Url acessada.")
    try:
        email = EmailTracked.objects.get(pk=email_id)
        print(f"Email com ID {email_id} encontrado!")
        if not email.opened:
            print(f"marcando email como lido.")
            email.opened_at = timezone.now()
            email.opened = True
            email.save()
        else:
            print(f"Email ja estava aberto")
            
    except EmailTracked.DoesNotExist:
        pass
    pixel_data = b"GIF89a\x01\x00\x01\x00\x80\x00\x00\xff\xff\xff\x00\x00\x00!\xf9\x04\x01\x00\x00\x00\x00,\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02D\x01\x00;"
    
    return HttpResponse(pixel_data, content_type='image/gif')


class EmailSubjectForm(forms.Form):
    subject = forms.CharField(max_length=200, widget=forms.TextInput(attrs={
        "placeholder": "Subject",
        "name": "subject"
    }))

def send_emails_view(request):
    selected_ids = request.session.get("selected_dest_ids")

    if not selected_ids:
        return redirect("admin:mail_Destinatario_changelist")
    
    if request.method == "POST":
        form = EmailSubjectForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            email = request.POST.get("email")
            if email != None:
                queryset = Destinatario.objects.filter(id__in=selected_ids)
                for dest in queryset:
                    send_tracked_email(dest, subject, f"{BASE_DIR}/mail/emails/{email}")

    emails_templates = [f for f in listdir(f"{BASE_DIR}/mail/emails") if f.endswith(".html")]
    form = EmailSubjectForm()
    context = {
        "templates": emails_templates,
        "form": form
    }
    return render(request, "mail/send_email_form.html", context)

class CustomEmailForm(forms.Form):
    subject = forms.CharField(max_length=200, widget=forms.TextInput(attrs={
        "placeholder": "Subject",
        "name": "subject"
    }))
    header = forms.CharField(max_length=200, widget=forms.TextInput(attrs={
        "placeholder": "Header",
        "name": "subject"
    }))
    image = forms.ImageField(widget=forms.FileInput)
    texto = forms.CharField(max_length=1000 ,widget=forms.Textarea(attrs={
        "placeholder": "Texto",
        "name": "texto"
    }))

def send_custom_emails_view(request):
    selected_ids = request.session.get("selected_dest_ids")

    if not selected_ids:
        return redirect("admin:mail_Destinatario-changelist")

    if request.method == "POST":
        form = CustomEmailForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            try:
                email = request.POST.get("email")
                subject = form.cleaned_data['subject']
                header = form.cleaned_data['header'] 
                texto = form.cleaned_data['texto']        
                image = form.cleaned_data.get('image')
                image_path = path.join(f'{BASE_DIR}/mail/static/images/', image.name)
                with open(image_path, "wb+") as f:
                    for chunk in image.chunks():
                        f.write(chunk)
                with open(f'{BASE_DIR}/mail/static/images/{image.name}', "rb") as image_file:
                    img_base64 = base64.b64encode(image_file.read()).decode("utf-8")

                if email != None:
                    queryset = Destinatario.objects.filter(pk__in=selected_ids)
                    for dest in queryset:
                        send_custom_tracked_email(dest, subject,header, texto, img_base64, f"{BASE_DIR}/mail/emails/custom/{email}")
            except Exception as e:
                traceback.print_exc()
                print(f'Erro email custom: {e}')
        else:
            print(f"form invalido: {form.errors}")

                        
                
    emails_templates = [f for f in listdir(f"{BASE_DIR}/mail/emails/custom") if f.endswith(".html")]
    form = CustomEmailForm()
    context = {
        "templates": emails_templates,
        "form": form
    }
    return render(request, "mail/send_email_form.html", context)