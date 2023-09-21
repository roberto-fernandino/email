from django.db import models
from django.utils import timezone
# Create your models here.
class Destinatario(models.Model):
    nome = models.CharField(max_length=60, null=True, blank=True)
    sobrenome = models.CharField(max_length=60, null=True, blank=True)
    email = models.EmailField(null=False, blank=False)
    
    def __str__(self) -> str:
        return f"{self.email}"

class EmailTracked(models.Model):
    dest = models.ForeignKey(Destinatario, on_delete=models.DO_NOTHING)
    sent_try = models.DateTimeField(auto_now_add=True)
    sent = models.BooleanField(default=False)
    opened = models.BooleanField(default=False)
    opened_at = models.DateTimeField(null=True, blank=True)

