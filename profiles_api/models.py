from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
from django.conf import settings
# Create your models here.

class UserProfileManager(BaseUserManager):
    """manager for user profile"""

    def create_user(self,email,First_name,Last_name,password=None):
        """create new user profile"""
        Name = First_name + " " + Last_name
        if not email:
            raise ValueError('User must have an email address')
        email=self.normalize_email(email)
        user=self.model(email=email,name=Name,First_name=First_name,Last_name=Last_name)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,email,First_name,Last_name,password):
        """create super users"""
        user=self.create_user(email,First_name,Last_name,password)
        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db)
        return user

class UserProfile(AbstractBaseUser,PermissionsMixin):
    """Database model for users in the system"""
    email=models.EmailField(max_length=255,unique=True)
    First_name=models.CharField(max_length=255)
    Last_name = models.CharField(max_length=255)
    name=models.CharField(max_length=255,default="name")
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)

    objects=UserProfileManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['First_name','Last_name']

    def get_fullName(self):
        """return the full name of the user"""
        name=self.First_name+ " " + self.Last_name
        return name
    def get_shortName(self):
        """return a short name of the user"""
        return self.First_name
    def __str__(self):
        """return string representation"""
        return self.email

class ProfileFeedItem(models.Model):
    user_profile=models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    status_text=models.CharField(max_length=255)
    created_on=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.status_text