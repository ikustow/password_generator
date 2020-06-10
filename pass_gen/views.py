from django.shortcuts import render
import random


# Create your views here.
def home(request):
    return render (request, 'pass_gen/home.html', {'password': 'aasdasdasd'})


def password(request):
    characters = list ('asdasdafdsfdscvxserwzfcx')
    lenght = int(request.GET.get('lenght'),12)
    if request.GET.get('uppercase'):
        characters.extend(list ('ABCDAHSAKLDNAASDASFASFGA'))
    if request.GET.get('special'):
        characters.extend(list ('*#%@&*!'))
    if request.GET.get ('numbers'):
        characters.extend (list ('123124235124523'))
    the_password = ''
    for x in range (lenght):
        the_password += random.choice (characters)

    return render (request, 'pass_gen/password.html', {'password': the_password})
