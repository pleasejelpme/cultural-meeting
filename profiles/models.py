from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class PerfilManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Los usuarios deben tener un email') 
        if not username:
            raise ValueError('Los usuarios deben tener un nombre de usuario') 

        user = self.model(
            email = self.normalize_email(email),
            username = username
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, username, password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username
        )
        user.set_password(password)
        user.is_admin = True
        user.is_staff = True           
        user.is_superuser = True   
        user.save(using=self._db)
        return user        
           

class Perfil(AbstractBaseUser):
    username        = models.CharField(max_length=50, unique=True)
    email           = models.EmailField(verbose_name='email' ,max_length=100, unique=True)
    fecha_creado    = models.DateTimeField(auto_now_add=True)
    is_admin        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=True)
    is_staff        = models.BooleanField(default=False)
    is_superuser    = models.BooleanField(default=False)
    avatar          = models.ImageField(null=True, blank=True)        
    intereses       = models.ManyToManyField('meetings.Categoria') 
    ciudad_origen   = models.ForeignKey(
        'meetings.Ciudad', 
        null=True, 
        on_delete=models.SET_NULL
        )
    
    objects = PerfilManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'

    def __str__(self):
        return self.username
    
    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    