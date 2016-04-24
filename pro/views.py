from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from pro import models



def home(request):
    return render(request,'home.html',{})

def about(request):
    return render(request,'about.html',{})

def contact(request):
    return render(request,'contact.html',{})

def list_users(request):
    pro_users = models.pro_users.objects.all()
    return render(request, "MemberList.html", {"users": pro_users})

def user(request, uid):
    print(uid)
    user = get_object_or_404(models.pro_users, pk=uid)
    return render(request, "User.html", {"user": user})


def add_event(request):
    add_event = models.vstrecha.objects.all()
    for param in ["name","length","date"]:
        if param not in request.GET:
            return render(request, "home.html")
    print(request.GET["name"]+request.GET["date"]+request.GET["length"])
    new_meeting = models.vstrecha()
    new_meeting.name = request.GET["name"]
    new_meeting.date_of_meeting = request.GET["date"]
    new_meeting.length = request.GET["length"]
    new_meeting.save()
    '''
    user_list =new_meeting.user_id.split(",")

    for member in user_list:
        new_user_meeting = models.users_vstrecha
        new_user_meeting.vstrecha_obj = new_meeting
        new_user_meeting.user_obj = (models.pro_users.objects.get(id=member))
        print(dir(models.pro_users.objects.get(id=member)))
        new_user_meeting.save()
    '''
    return render(request, "add_event.html")



def time(timestr):
    sec = []
    timestr.replace('"', ':')
    sec = timestr.split(':')
    return int(sec[0])*3600+int(sec[1])*60+int(sec[2])

def MeetingsCalendar_render(request):
    return render(request, "events.html", {})


'''def meeting(request):
    t = 0;
    list = []
    for member'''