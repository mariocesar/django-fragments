from django import forms
from django.utils.translation import ugettext_lazy as _
from fragments.models import Fragment

class FragmentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea())
    
    class Meta:
        model = Fragment
        fields = ('name', 'description', 'syntax', 'is_private',)

