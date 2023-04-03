from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

from utils.PhoneNumberValidation import phone_validator


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=13, validators=[phone_validator])
    image = models.ImageField(upload_to='avatars/', blank=True, null=True)
    is_premium = models.BooleanField(default=False)
    premium_date = models.DateTimeField(blank=True, null=True)
    header = models.CharField(max_length=255, blank=True, null=True)
    last_action = models.DateTimeField(default=timezone.now, blank=True, null=True)
    is_online = models.BooleanField(default=False, blank=True, null=True)

    REQUIRED_FIELDS=[]
    USERNAME_FIELD = "email"


    def __str__(self):
        return self.email
    
    class Meta:
        ordering = ['id']


class Position(models.Model):
    EMPLOYMENT_TYPE=(
        ('full employment','full employment'),
        ('part-time employment','part-time employment'),
        ('entrepreneur','entrepreneur'),
        ('freelance','freelance'),
        ('contract','contract'),
        ('internship','internship'),
        ('vocational training','vocational training'),
        ('Seasonal','Seasonal'),
    )

    JOB_TYPE=(
        ('office work','office work'),
        ('hybrid workflow','hybrid workflow'),
        ('remote work','remote work'),
    )

    user = models.ForeignKey(User, related_name='users_position', on_delete=models.CASCADE, unique=True)
    name = models.CharField(max_length=255)
    employment_type = models.CharField(max_length=200, choices=EMPLOYMENT_TYPE)
    company_name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    job_type = models.CharField(max_length=50, choices=JOB_TYPE)


    def __str__(self):
        return f'{self.user} {self.name} {self.company_name}'
    


class Skills(models.Model):
    user = models.ForeignKey(User, related_name='users_skills', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.user} {self.title}'
    

class EducationInformation(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,related_name='users_education')
    educational_institution=models.CharField(max_length=255)
    degree=models.CharField(max_length=200)
    specialization=models.CharField(max_length=255)
    start_date=models.DateField()
    end_date=models.DateField()
    average_score=models.PositiveIntegerField()
    activities_communities=models.CharField(max_length=255)


    def __str__(self):
        return f'{self.user}: {self.educational_institution}'
