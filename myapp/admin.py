from django.contrib import admin
from myapp.models import PersonalDetails
from myapp.models import Education
from myapp.models import Experiences
from myapp.models import AppointmentModel,AchivementsModel


class MyModelAdmin(admin.ModelAdmin):
  list_display = ('name', 'address', 'email','profile')

class MyModelEducation(admin.ModelAdmin):
  list_display = ('year','name','location')

class ExperienceModel(admin.ModelAdmin):
  list_display = ('name','designation','timePeriod')

class AppointMentSection(admin.ModelAdmin):
  list_display = ("name","email","subject",'date',"time")

class Achivement(admin.ModelAdmin):
  list_display = ("name","year","location")

admin.site.register(PersonalDetails, MyModelAdmin)
admin.site.register(Education,MyModelEducation)
admin.site.register(Experiences,ExperienceModel)
admin.site.register(AppointmentModel,AppointMentSection)
admin.site.register(AchivementsModel,Achivement)
