from django.views.generic import ListView

from fireblog.models import Entry


class EntryListView(ListView):
    template_name = "fireblog/entries.html"
    queryset = Entry.objects.filter(published="p")
    context_object_name = "entries"
    paginate_by = 10
