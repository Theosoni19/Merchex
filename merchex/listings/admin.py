from django.contrib import admin
from listings.models import Band, Listing

class BandAdmin(admin.ModelAdmin):
    list_display= ('name', 'genre', 'year_formed')

class ListAdmin(admin.ModelAdmin):
    list_display= ('title', 'year', 'band')


admin.site.register(Band, BandAdmin)
admin.site.register(Listing, ListAdmin)