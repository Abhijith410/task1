from django.db import models

# Create your models here.
class Registration(models.Model):
    usertype = models.CharField(max_length=20)
    firstname = models.CharField(max_length=20, db_column='fname')
    lastname = models.CharField(max_length=20, db_column='lname')
    email = models.TextField(max_length=20, db_column='email')
    address = models.TextField(max_length=50, db_column='address')
    username = models.CharField(max_length=20, db_column='usname')
    password = models.CharField(max_length=20, db_column='pswd')
    confpassword = models.CharField(max_length=20, db_column='cnfpass')
    image = models.ImageField(upload_to='images/')

    class Meta:
        db_table = "registration"