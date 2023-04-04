from django.db import models

# Create your models here.
class Urun(models.Model):
    title = models.CharField(("Ürün Tanıtım Başlık"), max_length=50)
    text = models.TextField(("Ürün Tanıtım Açıklama"), max_length=300)
    image = models.FileField(("Ürün Tanıtım Resmi"), upload_to='', max_length=100)
    def __str__(self):
        return self.title
class SatilikUrun(models.Model):
    title = models.CharField(("Ürün Başlık"), max_length=50)
    text = models.TextField(("Ürün Açıklama"), max_length=100)
    image = models.FileField(("Ürün Resmi"), upload_to='', max_length=100)
    price = models.FloatField(("Ürün Fiyatı"),null=True)
    def __str__(self):
        return self.title
class Referans(models.Model):
    name = models.CharField(("İsim"), max_length=50)
    image = models.FileField(("Logo"), upload_to='', max_length=100)
    def __str__(self):
        return self.name
class Comment(models.Model):
    card = models.ForeignKey(SatilikUrun, verbose_name=("Yorum yapılan ürün"), on_delete=models.CASCADE)
    user = models.CharField(("Yorum yapan kişi"), max_length=50)
    text = models.TextField(("yorum"))
    date_now = models.DateTimeField(("yorum yapılan saat"), auto_now_add=True)
    