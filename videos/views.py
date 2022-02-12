from django.shortcuts import get_object_or_404, render
from videos.models import Videos
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# import your views MyApp.
from MyApp.views import home

# Fonction recup data MyApp


def videos(request):
    return home(request)


def videos(request):
    videos_list = Videos.objects.all()
    paginator = Paginator(videos_list, 6)
    page = request.GET.get('page')

    # Config de la pagination
    try:
        videos = paginator.page(1)
    except PageNotAnInteger:
        videos = paginator.page(paginator.num_pages)
    context = {
        'videos': videos,
        'page': page
    }

    return render(request, 'videos/index.html', context)


def video_list(request):
    videos_list = Videos.objects.all()
    context = {
        'videos': videos_list,
    }
    return render(request, 'videos/category_vid.html', context)
