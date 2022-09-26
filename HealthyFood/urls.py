"""HealthyFood URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, re_path

from HealthyFoodApp.views import sing_upPage,sing_inPage,forgotPage,landingpagePage,breakfastPage,profilPage,aboutusPage,\
    quizPage,resetpasswordPage,newpasswordPage,lunchPage,dinnerPage,dessertsPage,certificatePage,eggsPage,omlettePage,\
    wrapPage,nuttyPage,steakPage,spaghettiPage,mushroomsPage,chiaPage,browniesPage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sing_up/', sing_upPage, name="sing_up"),
    path('forgot/', forgotPage, name="forgot"),
    path('resetpassword/', resetpasswordPage, name="resetpassword"),
    path('newpassword/', newpasswordPage, name="newpassword"),
    path('', sing_inPage, name="index"),
    path('landingpage/', landingpagePage, name="landingpage"),
    path('profilpage/', profilPage, name="profilpage"),
    path('aboutuspage/', aboutusPage, name="aboutuspage"),
    path('quizpage/', quizPage, name="quizpage"),
    path('breakastPage/', breakfastPage, name="breakfastPage"),
    path('lunchPage/', lunchPage, name="lunchPage"),
    path('dinnerPage/', dinnerPage, name="dinnerPage"),
    path('dessertsPage/', dessertsPage, name="dessertsPage"),
    path('certificatePage/', certificatePage, name="certificatePage"),
    path('eggsPage', eggsPage, name='eggsPage'),
    path('omlettePage', omlettePage, name='omlettePage'),
    path('wrapPage', wrapPage, name='wrapPage'),
    path('nuttyPage', nuttyPage, name='nuttyPage'),
    path('steakPage', steakPage, name='steakPage'),
    path('spaghettiPage', spaghettiPage, name='spaghettiPage'),
    path('mushroomsPage', mushroomsPage, name='mushroomsPage'),
    path('chiaPage', chiaPage, name='chiaPage'),
    path('browniesPage', browniesPage, name='browniesPage'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

