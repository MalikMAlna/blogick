from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin)


# Code Citation: https://www.youtube.com/watch?v=eCeRC7E8Z7Y


class AccountManager(BaseUserManager):
    def create_user(self, email, username, age, password=None):
        if not email:
            raise ValueError("Users must provide an email address!")
        if not username:
            raise ValueError("Users must provide a username!")
        if not age:
            raise ValueError("Users must provide their age!")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            age=age,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, age, password):
        if not email:
            raise ValueError("Superusers must provide an email address!")
        if not username:
            raise ValueError("Superusers must provide a username!")
        if not age:
            raise ValueError("Superusers must provide their age!")

        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            age=age,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    username = models.CharField(max_length=25, unique=True)
    display_name = models.CharField(max_length=25, unique=True)
    homepage = models.URLField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    date_joined = models.DateTimeField(
        verbose_name='date-joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last-login', auto_now=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['email', 'age']

    objects = AccountManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


# Profile for Account
class Profile(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')

    def __str__(self):
        if self.account.display_name:
            return f"{self.account.display_name.title()}'s Profile"
        return f"{self.account.username.title()}'s Profile"

