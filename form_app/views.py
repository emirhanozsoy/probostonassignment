from django.shortcuts import render
from .forms import AppForm
from ares_util.ares import call_ares

# Create your views here.
def form_app(request):

    form=AppForm()
    

    if request.method=='POST':
        forminstance=AppForm(request.POST)
        if forminstance.is_valid():
            if call_ares(request.POST.get('ico')):
                forminstance.save()
                context={'form':form,'success':1}
            else:
                context={'form':form,'error':1}
        else:
            context={'form':form,'error':1}

            
        return render(request,'form_app/form_app.html',context)

    context={'form':form}
    return render(request,'form_app/form_app.html',context)
