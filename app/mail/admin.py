from django.contrib import admin
from .models import Destinatario, EmailTracked
from django.shortcuts import redirect

# Register your models here.

@admin.action(description="Envia email para destinatarios selecionados.")
def envia_email(modeladmin, request, queryset):
    request.session['selected_dest_ids'] = list(queryset.values_list("id", flat=True))
    return redirect("mail:send-email-view")

@admin.action(description="Enviar email customizado para destinatarios selecinados")
def envia_email_custom(modeladmin, request, queryset):
    request.session['selected_dest_ids'] = list(queryset.values_list('id', flat=True))
    return redirect("mail:send-custom-email-view")

class DestinatarioAdmin(admin.ModelAdmin):
    actions = [envia_email, envia_email_custom]
    list_display = ['email', 'nome', 'sobrenome']
    list_display_links = ['email']
    fieldsets = (
        (None, {"fields": ['email', "nome", "sobrenome"]}),
    )

@admin.register(EmailTracked)
class EmailAdmin(admin.ModelAdmin):
    list_display = ['id','dest', 'opened', 'sent_try', 'sent']
    list_display_links = ['dest']


admin.site.register(Destinatario, DestinatarioAdmin)