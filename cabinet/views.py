from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView

from cabinet.models import News


def start_page(request):
    return HttpResponseRedirect(reverse('users:login'))


class NewsListView(LoginRequiredMixin, ListView):
    """Просмотр всех сущностей модели"""
    model = News

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Получение авторизованного пользователя
        current_user = self.request.user

        # Добавление информации о пользователе в контекст
        context['current_user'] = current_user

        return context
