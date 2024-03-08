from django.db import models

# Create your models here.

class PersonalDetails(models.Model):
    name = models.CharField(max_length = 50)
    address = models.CharField(max_length = 100)
    email = models.CharField(max_length = 70)
    profile = models.ImageField(upload_to="uploads/")
    about = models.CharField(max_length = 500, default = "MBA candidate transitioning from successful legal career to business and management. Established as diligent legal professional with extensive background and track record. Adept in drafting, research, and advocacy. Proficient in advising, negotiating, due diligence. Dedicated to achieving optimal outcomes for clients and organizations.")


class Education(models.Model):
    name = models.CharField(max_length = 200)
    year = models.BigIntegerField()
    location = models.CharField(max_length = 100)

class Experiences(models.Model):
    timePeriod = models.CharField(max_length=50)
    designation = models.CharField(max_length = 50)
    name = models.CharField(max_length = 200)

class AppointmentModel(models.Model):
    name = models.CharField(max_length = 50)
    email = models.CharField(max_length = 50)
    subject = models.CharField(max_length = 200)
    date = models.CharField(max_length = 10)
    time = models.CharField(max_length = 10)

class AchivementsModel(models.Model):
    name = models.CharField(max_length = 200)
    year = models.CharField(max_length = 5)
    location = models.CharField(max_length = 100)