from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Разрешает редактирование и удаление только автору поста.
    """

    def has_permission(self, request, view):
        # Разрешаем доступ для GET запросов всем пользователям
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Разрешаем редактировать и удалять только автору
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        return obj.author == request.user