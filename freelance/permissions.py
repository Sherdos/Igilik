from rest_framework import permissions

all_method = ('GET', 'HEAD', 'OPTIONS')

class IsServiceUserOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in all_method:
            return True
        
        return obj.user == request.user