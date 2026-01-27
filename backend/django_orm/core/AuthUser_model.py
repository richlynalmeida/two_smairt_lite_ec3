from django.db import models

class AuthUser(models.Model):
    id = models.AutoField(primary_key=True, db_column='id', verbose_name='User ID')
    password = models.CharField(max_length=128, db_column='password', verbose_name='Password')
    last_login = models.DateTimeField(null=True, blank=True, db_column='last_login', verbose_name='Last Login')
    is_superuser = models.BooleanField(db_column='is_superuser', verbose_name='Superuser Status')
    username = models.CharField(unique=True, max_length=150, db_column='username', verbose_name='Username')
    first_name = models.CharField(max_length=150, db_column='first_name', verbose_name='First Name')
    last_name = models.CharField(max_length=150, db_column='last_name', verbose_name='Last Name')
    email = models.EmailField(max_length=254, db_column='email', verbose_name='Email')
    is_staff = models.BooleanField(db_column='is_staff', verbose_name='Staff Status')
    is_active = models.BooleanField(db_column='is_active', verbose_name='Active')
    date_joined = models.DateTimeField(db_column='date_joined', verbose_name='Date Joined')

    class Meta:
        db_table = 'auth_user'
        app_label = 'core'
        managed = False
        verbose_name_plural = "User Management / A / Authorised User"
        # Force a real column for ordering so no one pulls in created_at:
        ordering = ['username']

    def __str__(self):
        return self.username

    def __label__(self):
        return f"{self.id} – {self.username}"

    def __repr__(self):
        return f"<AuthUser {self.id} - {self.username}>"
