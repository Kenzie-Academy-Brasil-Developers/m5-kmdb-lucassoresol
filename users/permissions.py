from rest_framework.views import Request, View
from rest_framework.permissions import BasePermission


class IsAdminUserList(BasePermission):
    def has_permission(self, req: Request, view: View):
        if req.method != "GET":
            return True

        return req.user.is_superuser


class IsAdminUserCreate(BasePermission):
    def has_permission(self, req: Request, view: View):
        if req.method != "POST":
            return True

        return req.user.is_superuser


class IsUserCreateReview(BasePermission):
    def has_permission(self, req: Request, view: View):
        if req.method != "POST":
            return True

        return req.user.is_superuser or req.user.is_authenticated and req.user.is_critic
