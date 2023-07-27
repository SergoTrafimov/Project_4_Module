from django.db import models

class Advertisement(models.Model):
    title = models.CharField("Заголовок", max_length=128)
    deskription = models.TextField("Описание")
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2 )
    auction = models.BooleanField("Торг", help_text='Если торг уместен то True(1), если не уместен то False(0)')
    create_at= models.DateTimeField(auto_now_add=True)
    update_at= models.DateTimeField(auto_now=True)