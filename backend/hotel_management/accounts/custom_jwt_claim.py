from django.utils import timezone
from django.contrib.auth.signals import user_logged_in
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.exceptions import AuthenticationFailed


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)

        # Send login signal
        user_logged_in.send(
            sender=self.user.__class__,
            request=self.context['request'],
            user=self.user
        )

        refresh = self.get_token(self.user)

        # Tokens
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        # Basic user info
        data['id'] = self.user.id
        data['username'] = self.user.username
        data['is_admin'] = self.user.is_staff
        data['is_active'] = self.user.is_active

        # ----- ROLE FIX -----
        role = self.user.role
        if role:
            data['role'] = {
                "id": role.id,
                "name": role.name,
                "description": role.description,
                "permissions": list(
                    role.role_permissions.values_list("permission_id", flat=True)
                )
            }
        else:
            data['role'] = None
        # ----------------------

        return data


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        try:
            response = super().post(request, *args, **kwargs)
        except AuthenticationFailed as e:
            if getattr(request, 'axes_locked_out', False):
                raise AuthenticationFailed(
                    detail='Due to unsuccessful attempts, the system is locked'
                )
            else:
                raise e
        return response
