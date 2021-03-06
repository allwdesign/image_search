from django.urls import path
from .views import PhotoUploadView, SearchResultsView

app_name = 'app'

urlpatterns = [
    path('', PhotoUploadView.as_view(), name='upload'),
    path('results/', SearchResultsView.as_view(), name='results'),
]
