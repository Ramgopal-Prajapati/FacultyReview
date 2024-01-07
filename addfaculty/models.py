from django.db import models

# Create your models here.
class addfaculty(models.Model):
    Faculty_Name=models.CharField(max_length=100)
    Position=models.CharField(max_length=100)
    Address=models.TextField(max_length=200)
    Imgs=models.FileField(upload_to="static")
    
  
    
    
class allreview(models.Model):
        Student_Name=models.CharField(max_length=100,blank=True, null=True)
        Faculty_Name=models.CharField(max_length=100)
        Title=models.CharField(max_length=100,blank=True, null=True)
        Position=models.CharField(max_length=100,blank=True, null=True)
        Description=models.TextField(max_length=500,blank=True, null=True)
        Suggetion=models.TextField(max_length=500,blank=True, null=True)
        Rating=models.TextField(max_length=500,blank=True, null=True)
        Subject=models.TextField(max_length=500,blank=True, null=True)
        
        
    
    