from django.contrib import admin
from django.contrib.admin.sites import site
from addfaculty.models import addfaculty , allreview

class addfacultymyAdmin(admin.ModelAdmin):
    list_display=('Faculty_Name','Position','Address','Imgs')
    
admin.site.register(addfaculty,addfacultymyAdmin)    

    
class allreviewAdmin(admin.ModelAdmin):
    list_display=('Faculty_Name','Position','Student_Name','Title','Description','Suggetion','Rating','Subject')
    
admin.site.register(allreview,allreviewAdmin)    

    