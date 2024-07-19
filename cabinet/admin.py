from django.contrib import admin

from cabinet.models import News, Contract, Finance, DataBase


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'picture',)


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'create_date',)


@admin.register(Finance)
class FinanceAdmin(admin.ModelAdmin):
    list_display = ['title', 'balance', 'contract', ]


@admin.register(DataBase)
class DataBaseAdmin(admin.ModelAdmin):
    list_display = ['title', 'create_date', 'contract', ]
