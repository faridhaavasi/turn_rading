from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class UserManager(BaseUserManager):
    def create_user(self, phone,fullname, file_number, password=None):


        user = self.model(
            phone = phone,
            fullname=fullname,
            file_number=file_number
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, fullname,file_number, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            phone=phone,
            password=password,
            fullname=fullname,
            file_number=file_number,

        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    fullname = models.CharField(max_length=50)
    file_number = models.CharField(max_length=55,unique=True, null=True,blank=True)
    phone = models.CharField(max_length=11, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['file_number','fullname']

    def __str__(self):
        return self.fullname

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
    
    
    class otp(models.Model):
        phone=models.CharField(max_length=11)
        code=models.CharField(max_length=4)
        expertion_date=models.DateTimeField(auto_now_add=True)
        
        class Meta:
            ordering=['phone']
            
        def __str__(self):
            return self.phone    
        