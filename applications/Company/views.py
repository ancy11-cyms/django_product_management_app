from django.shortcuts import render
from django.db.models import Q
from UserProfile.models import UserInfo 
from django.contrib.auth.models import User
# Create your views here.

def searchemp(request):
    if request.method == "GET":
        query = request.GET.get('q')
        results = UserInfo.objects.filter(Q(phone_number__icontains=query) )
    return render(request,"UserProfile/searchemp.html")
