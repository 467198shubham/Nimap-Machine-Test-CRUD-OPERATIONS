from django.shortcuts import render,HttpResponseRedirect
from .forms import ClientRegistration
from .models import User

# Create your views here.
# This function for Fetch data and Show Data.
def fetch_show(request):
    if request.method=='POST':
        fm = ClientRegistration(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['clientname']
            reg=User(clientname=nm)
            reg.save()
            fm= ClientRegistration()
    else:
        fm= ClientRegistration()
    clt=User.objects.all()
        
    return render(request,'RegisterClients/fetchandshow.html',{'form':fm,'clnt':clt})
# This function will Update data.

def update_data(request,id):
    if request.method == 'POST':
          dl=User.objects.get(pk=id)
          fm= ClientRegistration(request.POST,instance=dl)
          if fm.is_valid():
              fm.save()
    else:
        dl=User.objects.get(pk=id)
        fm= ClientRegistration(instance=dl)
        
              
        
    return render(request,'RegisterClients/update.html',{'form':fm})

# This function will Delete data.
def delete_data(request,id):
    if request.method == 'POST':
        dl=User.objects.get(pk=id)
        dl.delete()
        return HttpResponseRedirect('/')
    