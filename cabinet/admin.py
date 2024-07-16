from django.contrib import admin

from cabinet.models import News, Contract


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'picture',)


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'create_date',)
