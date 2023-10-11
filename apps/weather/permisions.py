import os

from rest_framework import permissions
from dotenv import load_dotenv

load_dotenv()

X_TOKEN = os.environ.get('X_TOKEN')


class XToken(permissions.BasePermission):
    def has_permission(self, request, view):
        token = request.headers.get('X-Token')
        return token == X_TOKEN
