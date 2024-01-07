from django.shortcuts import render
from addfaculty.models import addfaculty
from addfaculty.models import allreview

def Home(request):
    alldata=addfaculty.objects.all()
    data={
        'alldata':alldata
    }
    return render(request,"index.html",data)

def reviews(request):
    if request.method=="POST":
        Student_Name=request.POST.get("Student_Name")
        Faculty_Name=request.POST.get("Faculty_Name")
        Title=request.POST.get("Title")
        Position=request.POST.get("Position")
        Description=request.POST.get("Description")
        Subject=request.POST.get("Subject")
        Suggetion=request.POST.get("Suggetion")
        Rating=request.POST.get("Rating")
        
        re=allreview(Student_Name=Student_Name,Faculty_Name=Faculty_Name,Title=Title,Position=Position,Description=Description,Suggetion=Suggetion,Rating=Rating,Subject=Subject)
        re.save()
        
    return render(request,"reviews.html")