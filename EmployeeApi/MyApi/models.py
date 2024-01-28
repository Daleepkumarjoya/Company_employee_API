from django.db import models


# Create your models here.

class Company(models.Model):
    Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Location = models.CharField(max_length=100)
    About = models.TextField()
    type = models.CharField(max_length=100,
                            choices=(('IT', 'IT'), ('Non-IT', 'Non-IT'), ('Mobile Phones', 'Mobile Phones')))
    JoinDate = models.DateField(auto_now=True)
    Active = models.BooleanField(default=False)

    def __str__(self):
        return self.Name


class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    MobileNumber = models.CharField(max_length=11)
    about = models.TextField()
    position = models.CharField(max_length=100, choices=(
    ('Manager', 'Manager'), ('Software Developer', 'SD'), ('Project Leader', 'PL')))
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='name')

    def __str__(self):
        return self.name
