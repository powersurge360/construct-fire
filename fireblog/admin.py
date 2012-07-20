from django.contrib import admin
from fireblog.models import Entry


class EntryAdmin(admin.ModelAdmin):
    exclude = ("slug", "markup", "author",)
    list_display = ("title", "date", "published",)

    def save_model(self, request, obj, form, change):
        obj.author = request.user

        super(EntryAdmin, self).save_model(request, obj, form, change)

admin.site.register(Entry, EntryAdmin)
