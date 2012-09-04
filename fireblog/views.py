from django.views.generic import ListView, DetailView

from fireblog.models import Entry


class EntryListView(ListView):
    queryset = Entry.objects.filter(published="p")
    context_object_name = "entries"
    paginate_by = 10


class EntryDetailView(DetailView):
    queryset = Entry.objects.filter(published="p")
    context_object_name = "entry"
