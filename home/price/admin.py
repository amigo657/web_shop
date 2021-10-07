from django.contrib import admin
from price.models import Kit, Comments


class AdminKit(admin.ModelAdmin):
    list_display = ("title", "text")


class AdminComments(admin.ModelAdmin):
    list_display = ("auther",)


admin.site.register(Kit, AdminKit)
admin.site.register(Comments, AdminComments)