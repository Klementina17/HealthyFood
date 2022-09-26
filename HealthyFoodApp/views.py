from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import login, authenticate

# Create your views here.
def sing_inPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Username OR password is incorrect.')

    context = {}
    return render(request, 'sing_in.html', context)
def sing_upPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
    if form.is_valid():
        form.save()
        user = form.cleaned_data.get('username')
        messages.success(request, 'Account was created for ' + user)
        return redirect('index')
    context = {'form': form}
    return render(request, 'sing_up.html', context)
def forgotPage(request):
    return render(request, 'forgot.html')
def resetpasswordPage(request):
    return render(request, 'resetpassword.html')
def newpasswordPage(request):
    return render(request, 'newpassword.html')
def landingpagePage(request):
    return render(request, 'landingpage.html')
def profilPage(request):
    return render(request, 'profil.html')
def aboutusPage(request):
    return render(request, 'aboutus.html')
def quizPage(request):
    return render(request, 'quiz.html')
def breakfastPage(request):
    return render(request, 'breakfast.html')
def lunchPage(request):
    return render(request, 'lunch.html')
def dinnerPage(request):
    return render(request, 'dinner.html')
def dessertsPage(request):
    return render(request, 'desserts.html')
def certificatePage(request):
    return render(request, 'certificate.html')
def eggsPage(request):
    return render(request, 'eggsbread.html')
def omlettePage(request):
    return render(request, 'omlette.html')
def wrapPage(request):
    return render(request, 'veggiewrap.html')
def nuttyPage(request):
    return render(request, 'nuttychicken.html')
def steakPage(request):
    return render(request, 'steak.html')
def spaghettiPage(request):
    return render(request, 'spaghetti.html')
def mushroomsPage(request):
    return render(request, 'mushroom.html')
def chiaPage(request):
    return render(request, 'chia.html')
def browniesPage(request):
    return render(request, 'brownies.html')
