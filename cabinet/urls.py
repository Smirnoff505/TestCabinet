from django.urls import path

from cabinet.apps import NewsConfig
from cabinet.views import NewsListView, DataBaseView, DataBaseCreateView, DataBaseUpdateView, FinanceListView

app_name = NewsConfig.name

urlpatterns = [
    path('cabinet/', NewsListView.as_view(), name='cabinet'),
    path('db/', DataBaseView.as_view(), name='db'),
    path('db/create/', DataBaseCreateView.as_view(), name='create_db'),
    path('db/update/<int:pk>/', DataBaseUpdateView.as_view(), name='update_db'),
    path('finances/', FinanceListView.as_view(), name='finances'),
]
