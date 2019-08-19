from django.db import models

class User(models.Model):
    login = models.CharField(max_length=30, help_text="Enter login", verbose_name="Login",blank=False)
    first_name = models.CharField(max_length=30, help_text="Enter first name", verbose_name="First name",blank=False)
    last_name = models.CharField(max_length=30, help_text="Enter last name", verbose_name="Last name",blank=False)
    mail = models.CharField(max_length=30, help_text="Enter mail", verbose_name="Mail",blank=False)
    phone = models.CharField(max_length=30, help_text="Enter phone", verbose_name="Phone",blank=False)

class UserPasswd(models.Model):
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    is_current_password = models.BooleanField(verbose_name="Is current password?", blank=False)
    hash_password = models.BinaryField(editable=True)
    salt = models.BinaryField(editable=True)

# Create your models here.
