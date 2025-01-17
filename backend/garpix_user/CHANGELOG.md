### 3.4.0 (07.03.2023)

- Release fixes to pypi.org.

### 3.4.0-rc1-3.4.0-rc4 (01.03.2023)

- Bugs fixed

### 3.3.1-3.3.2 (28.02.2023)

- Localization error fixed
- Email lowercase error fixed

### 3.3.0 (24.02.2023)

- Localization error fixed
- Registration error fixed
- Delete user error fixed

### 3.2.1 (07.02.2023)

- Log in error fixed

### 3.2.0 (06.02.2023)

- Russian localization updated
- Restore password bugs fixed
- UserSession bugs fixed
- Registration bugs fixed
- Method `set_user_session` added to `User` model (see `Readme.md`)

### 3.1.0 (18.01.2023)

- Russian localization added
- `change_password` endpoint added
- Restore password logic updated

### 3.0.1 (07.11.2022)

- Tokens related names updated

### 3.0.0 (03.11.2022)

- Release on pypi.org.

### 3.0.0-rc5 - 3.0.0-rc6 (26.10.2022)

- Исправлена регистрация через подтверждение email и номера телефона
- Добавлен базовый класс для админ.панели (смотрите `Readme.md`)
- Исправлена связка моделей `User` и `UserSession`.
- Исправлены и дополнены автотесты

### 3.0.0-rc4 (21.10.2022)

- Удален миксин для `UserSession`
- Все миксины добавлены в модели из коробки, теперь все регулируется только настройками в `settings.py`
- Добавлена возможность настраивать список полей, используемых в `CustomAuthenticationBackend` качестве `username` (смотрите `Readme.md`)
- Исправлено swagger-документирование эндпоинтов
- Эндпоинт на восстановление пароля теперь принимает `username`.
- Добавлена настройка `REGISTRATION_SERIALIZER` - расширение сериалайзера регитсрации (смотрите `Readme.md`)

### 3.0.0-rc1 - 3.0.0-rc3 (05.10.2022)

- Проект преобразован в `garpix_user`
- Добавлена модель `UserSession` для работы с неавторизованным пользователем
- Добавлен функционал подтверждения номера телефона, email, восстановления и смены пароля (смотрите `Readme.md`)
- Добавлен функционал реферральных ссылок (смотрите `Readme.md`)
- Все настройки для модуля вынесены в единый объект в `settings.py`

### 2.2.0 (07.10.2021)

- Исправлен баг в CustomBackend.
- Добавлена модель AccessToken - создайте миграции!
- Теперь user - ForeignKey (а не OneToOneField) для AccessToken и RefreshToken. Это позволит при выходе с одного устройства не терять токен на другом.

### 2.1.0 (21.09.2021)

- Продление, а не изменение токена при протухании, если был рефреш. Без этого часто возникала ситуация, что с
разных браузеров пропадал доступ.

### 2.0.2 (14.09.2021)

- Исправлена ошибка при получении истекшего токена.

### 2.0.1 (19.08.2021)

- Добавлен permission `IsAuthenticated` для `LogoutView`. 

### 2.0.0 (18.08.2021)

- Изменен keyword с `Token` на более правильный - `Bearer` (см. https://datatracker.ietf.org/doc/html/rfc6750#section-1.2).
- Оптимизирована функция получения пользователя в токене.
- Добавлено протухание токена (если указано значение `GARPIX_ACCESS_TOKEN_TTL_SECONDS = 0`, то не протухает).
- Добавлен RefreshToken и возвращаемые данные при получении токена.
- Добавлена конечная точка для обновления токена, если он протух (через RefreshToken).
- В obtain_token переименовано поле `token` на `access_token`.

### 1.1.1 (16.06.2021)

- Исправлена ошибка с выключенными урлами для 'authorize'.

### 1.1.0 (16.06.2021)

- Добавлены тесты и логика переписана логика на django form.

### 1.0.1 (29.05.2021)

- Fixed README.

### 1.0.0 (29.05.2021)

- Release on pypi.org.
