from django.http import request
from django.http.response import HttpResponse, HttpResponseRedirect
from FBV_app.models import User
from FBV_app.forms import UserInfoForm
from django.shortcuts import render
from django.views.generic.base import RedirectView, TemplateView, View

# Create your views here.
class UserDisplayView(TemplateView):
    template_name= 'FBV_app/display.html'

    def get_context_data(self,*args,**kwargs):
        context=super().get_context_data(**kwargs)
        fm=UserInfoForm()
        std=User.objects.all()
        context={'form':fm,'std':std}
        return context
    
    def post(self,request):
        fm=UserInfoForm(request.POST,request.FILES)
        if fm.is_valid():
            # nm=fm.cleaned_data['name']
            # em=fm.cleaned_data['email']
            # mob=fm.cleaned_data['mob_number']
            # img=fm.cleaned_data['image']

            # obj=User(name=nm,email=em,mob_number=mob,image=img)
            # obj.save()
            fm.save()
            return HttpResponseRedirect("/")


# def display(request):
#     if request.method=='POST':
#         fm=UserInfoForm(request.POST, request.FILES)
#         if fm.is_valid():
#             nm=fm.cleaned_data['name']
#             em=fm.cleaned_data['email']
#             mob=fm.cleaned_data['mob_number']
#             img=fm.cleaned_data['image']

#             obj=User(name=nm,email=em,mob_number=mob,image=img)
#             obj.save()
#             fm=UserInfoForm()
#     else:
#         fm=UserInfoForm()
#     std=User.objects.all()
#     return render(request,'FBV_app/display.html',{'form':fm,'std':std})


class UserUpdateView(View):
    def get(self,request,id):
        std=User.objects.get(id=id)
        fm=UserInfoForm(instance=std)
        return render(request,'FBV_app/update.html',{'form':fm,'id':id})
    
    def post(self,request,id):
        std=User.objects.get(id=id)
        fm=UserInfoForm(request.POST,request.FILES,instance=std)
        if fm.is_valid():
            fm.save()
        return HttpResponseRedirect("/")



# def update_data(request,id):
#     std=User.objects.get(pk=id)
#     if request.method=='POST':
#         fm=UserInfoForm(request.POST,request.FILES,instance=std)
#         if fm.is_valid():
#             fm.save()
#             return HttpResponseRedirect('/')
#     else:
#         fm=UserInfoForm(instance=std)
#         return render(request,'FBV_app/update.html',{'form':fm,'id':id})


class UserDeleteView(RedirectView):
    url='/'

    def get_redirect_url(self,*args,**kwargs):
        std=User.objects.get(id=kwargs['id'])
        std.delete()
        return super().get_redirect_url(*args,**kwargs)



# def delete_data(request,id):
#     if request.method=='POST':
#         std=User.objects.get(pk=id)
#         std.delete()
#         return HttpResponseRedirect('/')