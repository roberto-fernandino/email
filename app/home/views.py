from django.shortcuts import render, redirect
from mail.models import EmailTracked
# Create your views here.
def relatorio(request):
    emails = EmailTracked.objects.all()
    emails_sent = []
    emails_not_sent = []
    for email in emails:
        if email.sent:
            emails_sent.append("email")
        else:
            emails_not_sent.append("email")
    context = {
       "emails_sent": len(emails_sent),
       "emails_not_sent": len(emails_not_sent)
    }
    return render(request, "home/home.html", context)