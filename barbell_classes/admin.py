from django.contrib import admin
from .models import BarbellClass

class BarbellClassAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_posted')
    readonly_fields = ('author', 'date_posted')
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)
    
    def has_change_permission(self, request, obj=None):
        if obj is not None and request.user == obj.author:
            return True
        return super().has_change_permission(request, obj=obj)
    
    def has_delete_permission(self, request, obj=None):
        if obj is not None and request.user == obj.author:
            return True
        return super().has_delete_permission(request, obj=obj)
    
    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return []
        return ['author', 'date_posted']

admin.site.register(BarbellClass, BarbellClassAdmin)
