from django.shortcuts import render
from datetime import datetime
from .models import PubGt, PubHt, logoOrganism, Programmes_Semaine, BannierePubGt, Versets

# Fonction du model video (app)
from videos.models import Videos

# Create your views here.

def bar(request, *args, **kwargs):
    BanPub = BannierePubGt.objects.all()[:3]
    return render(request, 'MyApp/barnier.html', {'barnier':BanPub})

def home(request):
    #Recup banniere depuis la database
    Pubht = PubHt.objects.all()[:1]
    
    Pubgt = PubGt.objects.all()[:1]
    Publog = logoOrganism.objects.all()
    PgreSemaine = Programmes_Semaine.objects.all()[:5]
    
    versets = Versets.objects.all()[:1]

    date = datetime.today()
    context = {
        'PubData': Pubht,
        'PubGt': Pubgt,
        'C_log': Publog,
        'Pweek': PgreSemaine,
        'vers': versets,
        'date': date,
    }
    return render(request, 'MyApp/index.html', context)
