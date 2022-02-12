from django.contrib import admin
from .models import PubGt, PubHt, logoOrganism, Programmes_Semaine, BannierePubGt, Versets

# Register your models here.

#Recup banniere depuis la database
@admin.register(PubHt)
class PubHtAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'bannerHt', 'urls', 'date_add']


@admin.register(PubGt)
class PubGtAdmin(admin.ModelAdmin):
    list_display = ['id', 'title_t', 'content_t',
                    'bannerGt', 'urls_t', 'date_added']


@admin.register(logoOrganism)
class logoOrganismAdmin(admin.ModelAdmin):
    list_display = ['id', 'titl_lo', 'logos', 'date_Reg']


@admin.register(Programmes_Semaine)
class Programmes_SemaineAdmin(admin.ModelAdmin):
    list_display = ['id', 'titre', 'desc', 'photo', 'dateReg']


@admin.register(BannierePubGt)
class BannierePubGtAdmin(admin.ModelAdmin):
    list_display = ['id', 'titr', 'images', 'dateRegister']


@admin.register(Versets)
class VersetAdmin(admin.ModelAdmin):
    list_display = ['id', 'coran', 'vers_one', 'vers_two', 'dateRe']
