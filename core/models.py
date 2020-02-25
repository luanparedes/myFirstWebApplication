from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Evento(models.Model):
    title = models.CharField(max_length=30)
    about = models.TextField(blank=True, null=True)
    date = models.DateTimeField(verbose_name='Event date')
    created = models.DateTimeField(auto_now=True, verbose_name='Created') #Insere a data da inserção, data atual
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'evento'

    def __str__(self):
        return self.title
        #Quando chamar  objeto vai mostrar o titulo conforme especificamos.
