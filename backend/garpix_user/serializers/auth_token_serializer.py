from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers
from rest_framework.authentication import authenticate

from garpix_user.models import UserSession


class AuthTokenSerializer(serializers.Serializer):
    username = serializers.CharField(label=_("Username"))
    password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        username = username.lower()

        if username and password:
            request = self.context.get('request')
            user = authenticate(request=request,
                                username=username, password=password)
            current_user_session = UserSession.get_from_request(request)
            print('current_user_session', current_user_session)
            if current_user_session:
                if (user_user_session := UserSession.objects.filter(
                        user=user).first()) and user_user_session != current_user_session:
                    current_user_session.delete()
                else:
                    current_user_session.user = user
                    current_user_session.recognized = UserSession.UserState.REGISTERED
                    current_user_session.save()
            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not user:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
