from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from products.models.product import Product


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.is_staff = False
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    """
        AbstractUser method because django provide default user login with username and password
        but requirment is user authanticate with his email and password.
        So, hear username filed none set email field with unique and extra field add link phone number and gender.
    """

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    email = models.EmailField(verbose_name='email address', max_length=255, unique=True, error_messages={
                              'unique': 'A user with that email already exists.'})
    username = models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150,
                                verbose_name='username', blank=True, null=True, default=None, unique=True)
    phone_number = models.CharField(
        verbose_name='phone number', max_length=20, blank=True, null=True)
    gender = models.CharField(verbose_name='gender', blank=True, default='M', max_length=1, choices=GENDER_CHOICES, error_messages={
                              'invalid_choice': 'Choise any one gender.'})

    wishlist_product = models.ManyToManyField(Product, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'user'

    def __str__(self):
        return self.email


class EmailSubscribe(models.Model):
    """EmailSubscribe model

    Args:
        models (method): [django model method]

    Returns:
        [string]: [email]
    """
    email = models.EmailField(max_length=255)

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'email_subscribe'
