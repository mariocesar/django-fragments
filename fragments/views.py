from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from fragments.models import Fragment
from fragments.forms import FragmentForm

class FragmentCreate(CreateView):
    model = Fragment
    form_class = FragmentForm

class FragmentDetail(DetailView):
    model = Fragment
    context_object_name = 'fragment'
    
class FragmentList(ListView):
    queryset = Fragment.objects.filter(is_private__exact=False)
    context_object_name = 'fragments'
    allow_empty = True

