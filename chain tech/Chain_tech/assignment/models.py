from django.db import models

from django.db import models

class UserDetails(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    dob = models.DateField(null=True, blank=True)
    country = models.CharField(max_length=255)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])
    intern_status = models.CharField(max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')])

    def __str__(self):
        return self.name

