from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate, views as auth_views
from django.contrib.auth.forms import UserCreationForm
from cookiez.Customer import insertCustomer, retrieveCustomer
from django.shortcuts import render, redirect
from django.template import RequestContext
from django.core.context_processors import csrf
from cookiez.models import Cookie
from .forms import AddCartForm



# Create your views here.

def index(request):
    cookies = Cookie.objects.all()
    return(render(request, 'index.html', {'cookies':cookies}))

def signup(request):
    insertCustomer()
    return(HttpResponse('done'))
    
def test(request):
    customer = retrieveCustomer()
    return(HttpResponse('done'))
    
def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form}, context_instance = RequestContext(request))

def cart(request):
    return (render(request, 'cart.html'))

#def sign_in(request):
 #   return (render(request, 'sign_in.html'))
    
def add_cart(request):
    print('cums')
    return HttpResponse()
    '''
    print("im here")
    if request.method == 'POST':
        form = AddCartForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thanks/')
    else:
        form = AddCartForm()
    args = {}
    args.update(csrf(request))
    args['form'] = form
    print("im here")
    return render('index.html', args)
    '''
'''
def updateCart(request, customerID):
    #add number from form to corresponding cookie id and customerID
    return HttpResponse()
'''