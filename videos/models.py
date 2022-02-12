from django.db import models
from django.contrib.auth.models import User
from embed_video.fields import EmbedVideoField
# Create your models here.


class Category(models.Model):
    organism = models.CharField(max_length=150, null=True,
                                verbose_name="Nom Organisme")
    auteur = models.CharField(max_length=50, null=True, verbose_name="Auteur")
    profil = models.ImageField(
        upload_to="profil/", null=True, verbose_name="Profil")
    cel = models.CharField(max_length=20, null=True,
                           verbose_name="Contact Whatsapp")

    def __str__(self) -> str:
        return self.organism

    class Meta:
        verbose_name_plural = 'Catégorie des Videos'


class Videos(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    titleV = models.CharField(
        null=False, verbose_name="Titre Video", max_length=255, unique=True)
    content = models.TextField(null=True, verbose_name="Description Vidéo")
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name="Categories Videos")
    url = EmbedVideoField(unique=True)
    added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-added']
        verbose_name_plural = 'Nos Videos'

    def __str__(self):
        return self.titleV
