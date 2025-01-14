from rest_framework import permissions

class IsManager(permissions.BasePermission):
    edit_methods = ('PUT', 'PATCH')
    
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        
        return False
    
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        
        if request.method in permissions.SAFE_METHODS:
            return True
        
        if obj.author == request.user:
            return True
        
        if request.user.is_staff and request.user.groups.filter(name='Tutorial Manager').exists():
            return True
        
        return False

class IsAdminrPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_adminUser:
            return True
        return False

class IsGeneralManagerPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name='General Manager').exists():
            return True
        return False

class IsBlogManagerPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name='Blog Manager').exists():
            return True
        return False

class IsTutorialManagerPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name='Tutorial Manager').exists():
            return True
        return False

class IsAuthorPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        
        return False
    
    def has_object_permission(self, request, view, obj):
        if obj.author == request.user:
            return True
        
        if request.user.is_staff and request.user.groups.filter(name='Tutorial Manager').exists():
            return True
        
        return False

class IsDeliveryCrewPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name='Delivery Crew').exists():
            return True
        return False