from django.contrib import admin

from .models import News, Ticket


class TicketAdmin(admin.ModelAdmin):
    fields = (
        "id", "name", "phone",
    )
    list_display = (
        "id", "name", "phone",
    )
    search_fields = (
        "id", "name", "phone",
    )
    readonly_fields = (
        "id",
    )



class NewsAdmin(admin.ModelAdmin):
    fields = (
        "id", "title", "description", "preview"
    )
    list_display = (
        "id", "title", "created_at", "updated_at"
    )
    search_fields = (
        "id", "title", "description", "created_at", "updated_at"
    )
    readonly_fields = (
        "id",
    )


admin.site.register(News, NewsAdmin)
admin.site.register(Ticket, TicketAdmin)
