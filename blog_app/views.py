from django.shortcuts import render
from .models import Blogdb
from django.utils import timezone

# Create your views here.
def post_list(request):
    posts=Blogdb.objects.filter(published_date=timezone.now()).order_by('published_date')
    return render(request,'post_list.html',{'posts':posts})