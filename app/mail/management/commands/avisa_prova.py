from django.core.management.base import BaseCommand 
from django.conf import settings
from mailjet_rest import Client
from os import getenv
import traceback
from django.template import Template, Context

def avisa_prova(email, subject:str, header:str, texto:str,  email_template_path:str):
   
    secret = getenv("MAIL_PRIVATE")
    public = getenv("MAIL_PUBLIC")
    mailjet = Client(auth=(public, secret), version='v3.1')
    context = {
        'header': header,
        'texto': texto,
    }
    try:
        with open (email_template_path, 'r') as file:
            template_content = file.read()
            template = Template(template_content)
            email_body = template.render(Context(context))
    except Exception as e:
        print(f"Exception as {e}")
    
    data = {
        'Messages': [
            {
                "From": {
                    "Email": getenv("EMAIL_HOST_USER"),
                    'Name': "Plataforma"
                },
                "To":[
                    {
                    'Email': email,
                    'Name': "Roberto",
                    },
                ],
                'Subject': f"Roberto, {subject}",
                'HTMLPart': email_body,
            }
        ]
    }
    try:
        result = mailjet.send.create(data=data)
        result_json, status_code = result.json(), result.status_code
        status = result_json["Messages"][0]["Status"]
        if status == "success":
            print("Correcao de prova avisada via email kkk, otima correção corretor!")
        return result.status_code, result.json()
    except Exception as e:
        traceback.print_exc()
        return print(f"Exception sending: {e}")
    

class Command(BaseCommand):
    def handle(self, *args, **kwargs) -> str | None:
        avisa_prova("romfernandino@gmail.com", "Prova sendo Corrigida", "Jaja sua nota sai hein lerdao", "fica esperto", f"{settings.BASE_DIR}/mail/emails/custom/email-template-base.html")
