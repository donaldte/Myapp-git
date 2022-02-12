from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date

# Create your models here.

 #model banniere depuis la database
class PubHt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100, null=True, verbose_name="Titre")
    urls = models.URLField(null=False, verbose_name="Url")
    content = models.TextField(null=False, verbose_name="Contenu Pub")
    bannerHt = models.ImageField(
        upload_to="pub/", null=True, verbose_name="Pub Format 728x90")
    date_add = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['-date_add']
        verbose_name_plural = 'Publicité Format 728x90'


class PubGt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title_t = models.CharField(max_length=100, null=True, verbose_name="Titre")
    urls_t = models.URLField(null=False, verbose_name="Url")
    content_t = models.TextField(null=False, verbose_name="Contenu Pub")
    bannerGt = models.ImageField(
        upload_to="pub/", null=True, verbose_name="Pub Format 702x1029")
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title_t

    class Meta:
        ordering = ['-date_added']
        verbose_name_plural = 'Publicité Format 702x1029'


class logoOrganism(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    titl_lo = models.CharField(
        max_length=100, null=True, verbose_name="Titre du Logo")
    logos = models.ImageField(upload_to="logo/", verbose_name="Image Logo")
    date_Reg = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.titl_lo

    class Meta:
        ordering = ['-date_Reg']
        verbose_name_plural = 'Logo Organisme'


class Programmes_Semaine(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    titre = models.CharField(max_length=160, null=True,
                             verbose_name="TiTre du Programme")
    desc = models.TextField(null=True, verbose_name="Description")
    photo = models.ImageField(upload_to="programme/",
                              null=True, verbose_name="Format 700x435")
    dateReg = models.DateField(auto_now_add=False, auto_now=False, null=True)

    def __str__(self) -> str:
        return self.titre

    class Meta:
        ordering = ['-dateReg']
        verbose_name_plural = 'Programmes en Semaine'


class BannierePubGt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    titr = models.CharField(max_length=160, null=True,
                            verbose_name="TiTre du Programme")
    images = models.ImageField(
        upload_to="programme/", null=True, verbose_name="Format 800x500")
    dateRegister = models.DateField(
        auto_now_add=False, auto_now=False, null=True)

    def __str__(self) -> str:
        return self.titr

    class Meta:
        ordering = ['-dateRegister']
        verbose_name_plural = 'Banniere Grand format Pub'


class Versets(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    coran = models.CharField(max_length=50, null=True, verbose_name="Chapitre")
    vers_one = models.CharField(
        max_length=255, null=True, verbose_name="Verset 1")
    vers_two = models.CharField(
        max_length=255, null=True, verbose_name="Verset 2")
    dateRe = models.DateTimeField(
        auto_now_add=True, verbose_name="Date", null=True)

    def __str__(self) -> str:
        return self.coran

    class Meta:
        ordering = ['-dateRe']
        verbose_name_plural = 'Verset du Jour'
