from rest_framework import permissions
from django.conf import settings

from apis.accounts.models import User

class IsNewsCreator(permissions.BasePermission):

    def has_permission(self, request, view):
        print(request.user)
        return bool(request.user and request.user.role in [i for i, j in User.ROLES if j in ['Admin', 'Journalist']])