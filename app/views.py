from django.views.generic import ListView, CreateView

from .models import Photo


class PhotoUploadView(CreateView):
    model = Photo
    fields = ['image']
    template_name = 'app/base.html'  # <app>/<model>_<viewtype>.html
    success_url = '/results/'  # /results/ if in url path('results/',...name='something')


class SearchResultsView(ListView):
    model = Photo
    template_name = 'app/results.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'results'