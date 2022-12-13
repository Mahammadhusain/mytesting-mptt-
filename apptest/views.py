from django.shortcuts import render
from .models import CategoryModel


# Create your views here.
def infoView(request):
    data = CategoryModel.objects.all()
    p = data.get_ancestors(include_self=False)
    context = {'data':data,'p':p}
    return render(request,'info.html',context)

def resultView(request):
    myrequest = request.GET
    p = list(myrequest.values())
    for i in p:
        data = CategoryModel.objects.filter(parent_attr = i)
    context = {'data':data,}
    return render(request,'result.html',context)