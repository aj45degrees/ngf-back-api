from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                        PermissionsMixin


class UserManager(BaseUserManager):
    """Customize the user model

    Args:
        BaseUserManager (object): django default user model
    """

    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new user

        Args:
            email (object): email object
            password (object, optional): password object. Defaults to None.

        Returns:
            user (object): contains user data
        """
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Creates and saves a new super user from cli

        Args:
            email ([type]): [description]
            password ([type]): [description]
        """
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that uses email instead of username

    Args:
        AbstractBaseUser ([type]): [description]
        PermissionsMixin ([type]): [description]
    """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
