from django.contrib import admin

from website.models import New, Category, Ads


class NewAdmin(admin.ModelAdmin):
    exclude = ('audio', 'audio_rom', 'slug')


admin.site.register(New, NewAdmin)
admin.site.register(Category)
admin.site.register(Ads)


