from django.contrib import admin
from fragments.models import Fragment

class FragmentAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'name', 'user', 'syntax', 'is_private', 'published')
    list_filter = ('is_private',)
    date_hierarchy = 'published'
    search_fields = ('name', 'description')
admin.site.register(Fragment, FragmentAdmin)
