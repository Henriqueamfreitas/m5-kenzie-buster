from rest_framework import permissions

class IsAdminUserOrSelf(permissions.BasePermission):
    # def has_object_permission(self, request, view, obj):
    #     return request.user.is_staff or obj == request.user
    def has_permission(self, request, view, user_id):
        print(request.user.id)
        print(user_id)
        return bool(request.user and request.user.is_staff)
                    

