import os
import random
from django.shortcuts import render, redirect
from fitnessproapp.models import *
from datetime import datetime,date,timedelta
from django.http import HttpResponse, HttpResponseRedirect
from django. contrib import messages
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import auth, User
from django.contrib.auth import authenticate
from django.db.models import Q
from fitnesspro.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
# Create your views here.



# login page

def login(request):

    if request.method == 'POST':
        email  = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email,password=password)
        if user is not None:
            request.session['SAdm_id'] = user.id
            return redirect( 'admhome')

        elif user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'],status="admin").exists():
                
                member=user_registration.objects.get(email=request.POST['email'], password=request.POST['password'])
                request.session['Tnr_id'] = member.id
                mem=user_registration.objects.filter(id= member.id)
                
                return render(request,'maintra.html',{'mem':mem})

        elif user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'],status="user").exists():
                
                member=user_registration.objects.get(email=request.POST['email'], password=request.POST['password'])
                request.session['Tne_id'] = member.id
                mem1=user_registration.objects.filter(id= member.id)
                
                return render(request,'index.html',{'mem1':mem1})
        else:
            context = {'msg_error': 'Invalid data'}
            return render(request, 'login.html', context)
    return render(request,'login.html')





#  Forgot password






# signup page

def signup(request):
    if request.method == 'POST':
        acc = user_registration()
        acc.firstname = request.POST['first_name']
        acc.lastname = request.POST['last_name']
        acc.username = request.POST['username']
        acc.email = request.POST['email']
        acc.photo = request.FILES['file']
        acc.password = request.POST['password']
        acc.save()
    return render(request,'signup.html')




# user side functions(trainee)



def index(request):
	if 'Tne_id' in request.session:
		if request.session.has_key('Tne_id'):
			Tne_id = request.session['Tne_id']
		else:
			return redirect('/')
		mem1 = user_registration.objects.filter(id=Tne_id)
		return render(request, 'index.html',{'mem1':mem1})
	else:
		return redirect('/')	


def user_view(request):
	if 'Tne_id' in request.session:
		if request.session.has_key('Tne_id'):
			Tne_id = request.session['Tne_id']
		else:
			return redirect('/')
		users = User.objects.filter(id=Tne_id)
		timetable=batch.objects.all()
		data={'timetable':timetable,'users':users}
		return render(request, 'userview.html',data)
	else:
		return redirect('/')









def Trainee_logout(request):
    if 'Tne_id' in request.session:
        request.session.flush()
        return redirect('/')
    else:
        return redirect('/')		

# user side end
  


# admin side functions



	





def maint(request):
	if 'Tnr_id' in request.session:
		if request.session.has_key('Tnr_id'):
			Tnr_id = request.session['Tnr_id']
		else:
			return redirect('/')
		mem = user_registration.objects.filter(id=Tnr_id)
		return render(request, 'maintra.html',{'mem':mem})
	else:
		return redirect('/')	


def admin_view_timetablee(request):
	if 'Tnr_id' in request.session:
		if request.session.has_key('Tnr_id'):
			Tnr_id = request.session['Tnr_id']
		else:
			return redirect('/')
		users = User.objects.filter(id=Tnr_id)
		timetable=batch.objects.all()
		data={'timetable':timetable,'users':users}
		return render(request, 'adminview.html',data)
	else:
		return redirect('/')


def admin_edit_timetablee(request,i_id):
	if 'Tnr_id' in request.session:
		if request.session.has_key('Tnr_id'):
			Tnr_id = request.session['Tnr_id']
		else:
			return redirect('/')
		users = User.objects.filter(id=Tnr_id)
		timet=batch.objects.get(id=i_id)
		
		return render(request, 'admin_edit.html',{'timet':timet,'users':users})
	else:
		return redirect('/')

def admin_editpagee(request,timet_id):
	if 'Tnr_id' in request.session:
		if request.session.has_key('Tnr_id'):
			Tnr_id = request.session['Tnr_id']
		else:
			return redirect('/')
		users = User.objects.filter(id=Tnr_id)
		if request.method=='POST':
			table = batch.objects.get(id=timet_id)
			table.vnum=request.POST.get('vnum')
			table.vtype=request.POST.get('vtype')
			table.vmodel=request.POST.get('vmodel')
			table.vdes=request.POST.get('vdes')
			table.save()
			return redirect('admin_view_timetablee')
		return render(request, 'admin_edit.html',{'users':users})
	else:
		return redirect('/')







def Trainer_logout(request):
    if 'Tnr_id' in request.session:
        request.session.flush()
        return redirect('/')
    else:
        return redirect('/')	


# trainer side end



#superadmin side functions



def admhome(request):
	if 'SAdm_id' in request.session:
		if request.session.has_key('SAdm_id'):
			SAdm_id = request.session['SAdm_id']
		else:
			return redirect('/')
		users = User.objects.filter(id=SAdm_id)
		return render(request, 'adm_home.html',{'users':users})
	else:
		return redirect('/')





def admreg(request):
	if 'SAdm_id' in request.session:
		if request.session.has_key('SAdm_id'):
			SAdm_id = request.session['SAdm_id']
		else:
			return redirect('/')
		users = User.objects.filter(id=SAdm_id)
		det=user_registration.objects.all()
		data={'det':det,'users':users}
		return render(request, 'adm_reg.html',data)
	else:
		return redirect('/')		





def admregedit(request,i_id):
	if 'SAdm_id' in request.session:
		if request.session.has_key('SAdm_id'):
			SAdm_id = request.session['SAdm_id']
		else:
			return redirect('/')
		users = User.objects.filter(id=SAdm_id)
		reg=user_registration.objects.get(id=i_id)
		return render(request, 'adm_regedit.html',{'reg':reg,'users':users})
	else:
		return redirect('/')		






def admregistration(request,reg_id):
	if 'SAdm_id' in request.session:
		if request.session.has_key('SAdm_id'):
			SAdm_id = request.session['SAdm_id']
		else:
			return redirect('/')
		users = User.objects.filter(id=SAdm_id)
		if request.method=='POST':
			regs=user_registration.objects.get(id=reg_id)
			regs.firstname=request.POST.get('first_name')
			regs.lastname=request.POST.get('last_name')
			regs.email=request.POST.get('email')
			regs.status=request.POST.get('status')
			regs.save()
			return redirect('admreg')

		return render(request,'adm_regedit.html',{'users':users})
	else:
		return redirect('/')






def admintimetable(request):
	if 'SAdm_id' in request.session:
		if request.session.has_key('SAdm_id'):
			SAdm_id = request.session['SAdm_id']
		else:
			return redirect('/')
		users = User.objects.filter(id=SAdm_id)
		if request.method=='POST':
			d=request.POST['vnum']
			vt=request.POST['vtype']
			w=request.POST['vmodel']
			wc=request.POST['vdes']
			batch.objects.create(vnum=d,vtype=vt,vmodel=w,vdes=wc)
		return render(request, 'adm_timetable.html',{'users':users})
	else:
		return redirect('/')		






def admin_view_timetable(request):
	if 'SAdm_id' in request.session:
		if request.session.has_key('SAdm_id'):
			SAdm_id = request.session['SAdm_id']
		else:
			return redirect('/')
		users = User.objects.filter(id=SAdm_id)
		timetable=batch.objects.all()
		data={'timetable':timetable,'users':users}
		return render(request, 'adm_view_timetable.html',data)
	else:
		return redirect('/')






def admin_edit_timetable(request,i_id):
	if 'SAdm_id' in request.session:
		if request.session.has_key('SAdm_id'):
			SAdm_id = request.session['SAdm_id']
		else:
			return redirect('/')
		users = User.objects.filter(id=SAdm_id)
		timet=batch.objects.get(id=i_id)
		return render(request, 'adm_edit_timetable.html',{'timet':timet,'users':users})
	else:
		return redirect('/')		





def admin_editpage(request,timet_id):
	if 'SAdm_id' in request.session:
		if request.session.has_key('SAdm_id'):
			SAdm_id = request.session['SAdm_id']
		else:
			return redirect('/')
		users = User.objects.filter(id=SAdm_id)
		if request.method=='POST':
			table = batch.objects.get(id=timet_id)
			table.vnum=request.POST.get('vnum')
			table.vtype=request.POST.get('vtype')
			table.vmodel=request.POST.get('vmodel')
			table.vdes=request.POST.get('vdes')
			table.save()
			return redirect('admin_view_timetable')
		return render(request, 'adm_edit_timetable.html',{'users':users})
	else:
		return redirect('/')






def delete_batch(request,p_id):
	products=batch.objects.get(id=p_id)
	products.delete()
	return redirect('admin_view_timetable')











def SuperAdmin_logout(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        request.session.flush()
        return redirect("/")
    else:
        return redirect('/')