from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
)

class UserManager(BaseUserManager):
    """
    """
    def _create_user(self, email, password, **kwargs):
        if not email:
            raise ValueError("Users must have an Email")

        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)

        user.set_password(password)
        user.save()
        return user

    def create_user(self, email, password=None, **kwargs):
        return self._create_user(self, email, password, kwargs)

    def create_superuser(self, email, password, **kwargs):
        """
        Creates and saves a superuser with the given email and password.
        """
        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_superuser", True)
        kwargs.setdefault("is_active", True)

        return self.create_user(email, password, **kwargs)

class User(AbstractBaseUser, PermissionsMixin):
    """
    Модель пользователя.
    """

    # главнные поля для регистрации
    email = models.EmailField(
        verbose_name="Электронная почта", max_length=30, unique=True
    )
    first_name = models.CharField(verbose_name="Фамилия", max_length=22)
    last_name = models.CharField(verbose_name="Имя", max_length=22)

    # служебнные
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        """
        Строковое представление объекта
        """
        return self.email

    class Meta:
        ordering = ["email"]
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
