from django.urls import path

from cabinet.apps import NewsConfig
from cabinet.views import NewsListView

app_name = NewsConfig.name

urlpatterns = [
    path('cabinet/', NewsListView.as_view(), name='cabinet')
]
