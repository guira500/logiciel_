from django.contrib.auth.backends import BaseBackend
from .models import administrateur, employe

""" class EmailBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = administrateur.objects.get(email=email)
            if user.check_password(password):
                return user
        except administrateur.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return administrateur.objects.get(pk=user_id)
        except administrateur.DoesNotExist:
            return None """


class EmailBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        user = None

        # Rechercher dans le modèle employe
        try:
            user = employe.objects.get(email=email)
            if user.check_password(password):
                return user
        except employe.DoesNotExist:
            pass

        # Rechercher dans le modèle Administrateur si non trouvé
        try:
            user = administrateur.objects.get(email=email)
            if user.check_password(password):
                return user
        except administrateur.DoesNotExist:
            pass

        return None

    def get_user(self, user_id):
        try:
            return employe.objects.get(pk=user_id)
        except employe.DoesNotExist:
            try:
                return administrateur.objects.get(pk=user_id)
            except administrateur.DoesNotExist:
                return None