from rest_framework.views import Request, View
from rest_framework.permissions import BasePermission
import ipdb


class IsAdminUserList(BasePermission):
    def has_permission(self, req: Request, view: View):
        if req.method != "GET":
            return True

        return req.user.is_superuser
