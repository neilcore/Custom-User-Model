from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.shortcuts import get_object_or_404


class CustomUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None):
        if not email:
            raise ValueError("Email is a must")
        if not first_name:
            raise ValueError("First Name is required")
        if not last_name:
            raise ValueError("Last Name is required")
        # Create User
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password):

        active_status = get_object_or_404(Status, status='Active')
        user = self.create_user(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.status = active_status
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, max_length=50, verbose_name='email')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, null=True, blank=True)

    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return f'{self.last_name} {self.first_name}'

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Employees'
