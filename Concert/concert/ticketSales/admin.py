from django.contrib import admin
from ticketSales.models import concertModel
from ticketSales.models import locationModel
from ticketSales.models import timeModel
from ticketSales.models import ticketModel


# Register your models here.

class ConcertAdmin(admin.ModelAdmin):
    list_display=("Name","SingerName","lenght","Poster")

admin.site.register(concertModel,ConcertAdmin)
admin.site.register(locationModel)
admin.site.register(timeModel)
admin.site.register(ticketModel)