from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class UserManager(BaseUserManager):
    """Create custom user manager, for our custom user model

    Args:
        BaseUserManager ([type]): [description]
    """

    def create_user(self, email, password=None, **extra_fields):
        """Create a new user using email as username

        Args:
            email ([type]): [description]
            password ([type]): [description]
        """
        if not email:
            raise ValueError("Users must have an email address")
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Creates Django superuser. Will be used only through command line, so we don't need extra_fields

        Args:
            email ([str]): [email address]
            password ([sre]): [password]
        """
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom Django user model that supports naving email as an username. Assigns custom UserManager to objects of the model

    Args:
        AbstractBaseUser ([type]): [description]
        PermissionsMixin ([type]): [description]
    """

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = (
        UserManager()
    )  # creates a new custom UserManager and assigns to objects of the model

    USERNAME_FIELD = "email"  # default for this is 'username'
