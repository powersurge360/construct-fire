from django.contrib import admin
from fireblog.models import Entry


def publish_selected(modeladmin, request, queryset):
    queryset.update(published="p")

publish_selected.short_description = "Publish selected Entries"


class EntryAdmin(admin.ModelAdmin):
    exclude = ("slug", "markup", "author",)
    list_display = ("title", "date", "published",)
    actions = [publish_selected]

    def save_model(self, request, obj, form, change):
        obj.author = request.user

        super(EntryAdmin, self).save_model(request, obj, form, change)

admin.site.register(Entry, EntryAdmin)
