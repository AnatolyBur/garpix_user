from garpix_user.models import GarpixUser


class User(GarpixUser):

    USERNAME_FIELDS = ('phone', 'email')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
