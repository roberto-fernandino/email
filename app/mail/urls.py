# urls.py
from django.urls import path
from .views import track_email_view, send_emails_view, send_custom_emails_view


app_name = "mail"

# urls donw here
urlpatterns = [
    path("track-email/<int:email_id>", track_email_view, name="track-email-view"),
    path("send_emails", send_emails_view, name="send-email-view"),
    path("custom-send_emails", send_custom_emails_view, name="send-custom-email-view"),
]

