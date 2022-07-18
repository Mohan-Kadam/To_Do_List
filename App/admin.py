from django.contrib import admin
from .models import Post

# Register your models here.
def change_status(modeladmin, request, queryset):
    queryset.update(Status=True)
change_status.short_description = 'Change Status Of Selected Task As Done'


def change_status_false(modeladmin, request, queryset):
    queryset.update(Status=False)
change_status_false.short_description = 'Change Status Of Selected Task As Not Done'



class Status_Display(admin.ModelAdmin):
    list_display = ('Task','Status')
    actions = [change_status, change_status_false]


admin.site.register(Post, Status_Display)