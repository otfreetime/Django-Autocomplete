from django.db import models


class ListOfUsers(models.Model):
    emp_number = models.CharField(db_column='Emp_Number', primary_key=True, max_length=50, unique=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=40)  # Field name made lowercase.
    supervisor = models.CharField(db_column='Supervisor', max_length=40)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50, blank=False, null=False, unique=True)  # Field name made lowercase.


    class Meta:
        managed = False
        db_table = 'List of users'