"""fitnesspro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import re_path, include

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import re_path
from fitnessproapp import views

urlpatterns = [
    re_path('admin/', admin.site.urls),

    re_path(r'^$', views.login, name='login'),
    
    re_path(r'^index/$', views.index, name='index'),
    
    re_path(r'^signup/$', views.signup, name='signup'), 
    
    re_path(r'^maint/$', views.maint, name='maint'),
    re_path(r'^admhome/$', views.admhome, name='admhome'),
    re_path(r'^admreg/$', views.admreg, name='admreg'),
    re_path(r'^admregedit/(?P<i_id>[0-9]+)/$', views.admregedit, name='admregedit'),
    re_path(r'^admregistration/(?P<reg_id>[0-9]+)/$', views.admregistration, name='admregistration'),
    re_path(r'^admintimetable/$', views.admintimetable, name='admintimetable'),
    re_path(r'^user_view/$', views.user_view, name='user_view'),
    re_path(r'^admin_view_timetable/$', views.admin_view_timetable, name='admin_view_timetable'),
    re_path(r'^admin_view_timetablee/$', views.admin_view_timetablee, name='admin_view_timetablee'),
    re_path(r'^admin_edit_timetable/(?P<i_id>[0-9]+)/$', views.admin_edit_timetable, name='admin_edit_timetable'),
    re_path(r'^admin_edit_timetablee/(?P<i_id>[0-9]+)/$', views.admin_edit_timetablee, name='admin_edit_timetablee'),
    re_path(r'^admin_editpage/(?P<timet_id>[0-9]+)/$', views.admin_editpage, name='admin_editpage'),
    re_path(r'^admin_editpagee/(?P<timet_id>[0-9]+)/$', views.admin_editpagee, name='admin_editpagee'),
    re_path(r'^delete_batch/(?P<p_id>[0-9]+)/$', views.delete_batch, name='delete_batch'),
    
    re_path(r'^Trainee_logout/$', views.Trainee_logout, name='Trainee_logout'),
    re_path(r'^Trainer_logout/$', views.Trainer_logout, name='Trainer_logout'),
    re_path(r'^SuperAdmin_logout/$', views.SuperAdmin_logout, name='SuperAdmin_logout'),
    


    


]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

