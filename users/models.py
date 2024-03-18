# application/users/models.py
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

# This class is a custom user manager that likely handles user creation and management in a Python
# application.
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """
        The function creates a user with a specified email, password, and additional fields.
        
        :param email: The `create_user` method is a common method used in Django for creating a new user
        object. The parameters for the method are as follows:
        :param password: The `password` parameter in the `create_user` method is used to set the
        password for the user being created. It is an optional parameter, meaning that if no password is
        provided, it will default to `None`. If a password is provided, it will be set for the user
        using the
        :return: The `create_user` method is returning the user object that has been created and saved
        in the database.
        """
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        The function `create_superuser` creates a superuser with the specified email, password, and
        additional fields if provided.
        
        :param email: The `create_superuser` method is a custom method for creating a superuser in a
        Django project. It takes the email and password as required parameters, and any additional
        fields can be passed as keyword arguments in the `extra_fields` parameter
        :param password: The `create_superuser` method is a custom method for creating a superuser in a
        Django project. It takes the email and password as required parameters, and any additional
        fields can be passed as keyword arguments in the `extra_fields` parameter
        :return: The `create_superuser` method is returning the result of calling the `create_user`
        method with the provided `email`, `password`, and any additional `extra_fields` that were passed
        in. The `is_staff` and `is_superuser` fields in the `extra_fields` dictionary are set to `True`
        if they are not already present.
        """
        if not extra_fields.get('is_staff'):
            extra_fields['is_staff'] = True
        if not extra_fields.get('is_superuser'):
            extra_fields['is_superuser'] = True
        return self.create_user(email, password, **extra_fields)

# The above class is a custom user model in Python that inherits from AbstractBaseUser.
class User(AbstractBaseUser):
    username = models.CharField(max_length=150, blank=True, null=True)
    email = models.EmailField(max_length=255, unique=True)

    first_name = models.CharField(max_length=150, blank=True, null=True)
    middle_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    # The class Meta defines a database table name for the users class in Python.
    class Meta:
        db_table = 'users'

    def __str__(self):
        """
        The above function is a Python special method that returns the email attribute as a string
        representation of the object.
        :return: The `email` attribute of the object is being returned as a string.
        """
        return self.email
