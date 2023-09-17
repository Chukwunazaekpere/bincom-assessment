from django.contrib.auth.models import (
    AbstractBaseUser, 
    BaseUserManager,
    PermissionsMixin
)
# from django.contrib.auth.models import PermissionsMixin
from django.db import models

from polling_units.models import PollingUnit


class BaseUserModelManager(BaseUserManager):
    def create_user(self, firstname, lastname, email, phone, password, **kwargs):
        try:
            if not firstname:
                raise ValueError("Firstname is required.")
            if not lastname:
                raise ValueError("Lastname is required.")
            if not email:
                raise ValueError("Email is required")
            
            email = self.normalize_email(email)
            new_user = self.model(firstname=firstname, lastname=lastname, email=email, phone=phone, **kwargs)
            new_user.set_password(password)
            new_user.save(using=self._db)
            return new_user
        except Exception as error:
            print("\n\t Create user error: ", error)
            return error

    def create_superuser(self, email, firstname, lastname, password, **kwargs):
        try:
            kwargs.setdefault("is_active", True)
            kwargs.setdefault("is_staff", True)
            kwargs.setdefault("is_superuser", True)

            new_superuser = self.create_user(
                email=email,
                firstname=firstname,
                lastname=lastname,
                password=password,
                **kwargs
            )
            return new_superuser
        except Exception as error:
            print("\n\t Create super-user error: ", error)
            return error



class Agents(AbstractBaseUser, PermissionsMixin):
    name_id = models.PositiveIntegerField(unique=True, null=False)
    firstname = models.CharField(max_length=25, null=False)
    lastname = models.CharField(max_length=25, null=False)
    password = models.CharField(max_length=200, help_text="Enter 1 for password")
    email = models.EmailField()
    phone = models.CharField(max_length=13, null=False, unique=True)
    is_anonymous = models.BooleanField(default=True)
    is_authenticated = models.BooleanField(default=False)
    last_login = models.DateTimeField(auto_now_add=False, auto_now=True)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    polling_unit = models.ForeignKey(PollingUnit, on_delete=models.PROTECT, null=True)

    USERNAME_FIELD = "name_id" 
    objects = BaseUserModelManager()
    REQUIRED_FIELDS = ['firstname', 'lastname', 'email', 'phone']

    def agents_fullname(self):
        return f"{self.firstname} {self.lastname}"
    agents_fullname.short_description = "Agents fullname"

    def __str__(self):
        return self.agents_fullname()

    
    # def save(self, using):
    #     agents = Agents()
    #     queryset = agents.objects.get_queryset()
    #     print("\n\t queryset: ", queryset)
    #     queryset_length = len(queryset)
    #     self.name_id = queryset_length+1
    #     self.save()

    class Meta:
        verbose_name = "Agent"
        verbose_name_plural = "Agents"
        unique_together = ["firstname", "lastname"]