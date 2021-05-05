from django.http import HttpResponse
from django.shortcuts import render
from front_page.models import  University


# Create your views here.
def index(request):
    return render(request,'base_main.html')


def info_table(request):

    universities = University.objects.all().values( )
    print(universities)

    context = {'universities':universities,}
    return render(request,'info_table.html',context)





