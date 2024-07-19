from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

from cabinet.models import News, Contract, Finance, DataBase


def start_page(request):
    return HttpResponseRedirect(reverse('users:login'))


class NewsListView(LoginRequiredMixin, ListView):
    """Просмотр всех сущностей модели"""
    model = News

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Получение авторизованного пользователя
        current_user = self.request.user

        # Получение информации о финансах и контракте
        contracts = Contract.objects.filter(owner=current_user)

        # Добавление информации о пользователе в контекст
        context['current_user'] = current_user
        context['contracts'] = contracts

        return context


class DataBaseView(LoginRequiredMixin, ListView):
    """Просмотр всех сущностей баз данных принадлежащих текущему пользователю."""
    model = DataBase

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Получаем все контракты связанные с текущим пользователем
        contracts = Contract.objects.filter(owner=self.request.user)

        # Фильтруем базы данных по контрактам
        list_db = DataBase.objects.filter(contract__in=contracts)

        # Добавляем список баз данных в контекст
        context['list_db'] = list_db
        context['current_user'] = self.request.user
        context['contracts'] = contracts

        return context


class DataBaseCreateView(LoginRequiredMixin, CreateView):
    """Создание сущности DataBase"""
    model = DataBase
    fields = ('title', 'contract',)
    success_url = reverse_lazy('cabinet:db')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['current_user'] = self.request.user

        return context


class DataBaseUpdateView(LoginRequiredMixin, UpdateView):
    """Обновление сущности DataBase"""
    model = DataBase
    fields = ('title', 'contract',)
    success_url = reverse_lazy('cabinet:db')


class FinanceListView(LoginRequiredMixin, ListView):
    """Просмотр всех сущностей Finance принадлежащих текущему пользователю."""

    model = Finance

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Получаем все контракты связанные с текущим пользователем
        contracts = Contract.objects.filter(owner=self.request.user)

        context['contracts'] = contracts
        context['current_user'] = self.request.user

        return context
