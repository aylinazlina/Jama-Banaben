from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from .models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import JsonResponse
import json
from .decorators import unauthenticated_user,allowed_users,admin_only
from django.contrib.auth.models import Group

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

@unauthenticated_user
def Registration(request):

    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='customer')
            user.groups.add(group)
            messages.success(request, "Account was created for " + username)
            return redirect('loginPage')

    context = {
        'form': form,
    }
    return render(request, template_name='Registration.html', context=context)


@unauthenticated_user
def loginPage(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, "username or password incorrect")

    context = {

    }
    return render(request, template_name='login.html', context=context)


def logoutuser(request):
    logout(request)
    return redirect('loginPage')


@login_required(login_url='loginPage')
@admin_only
def home(request):
    items = Items.objects.all()
    context ={
        'item':  items,
    }
    return render(request,template_name='home.html',context=context)

def createItem(request):
    form = ItemsForm()
    if request.method == 'POST':
        form =ItemsForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    context ={
        'form': form,
    }
    return render(request,template_name='create_item.html',context=context)

def updateItem(request,pk):
    update =Items.objects.get(id=pk)
    form = ItemsForm(instance=update)
    if request.method == 'POST':
        form =ItemsForm(request.POST,request.FILES,instance=update)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form,
    }
    return render(request, template_name='create_item.html', context=context)

def deleteItem(request,pk):
    delete = Items.objects.get(id=pk)
    if request.method == "POST":
        delete.delete()
        return redirect('/')
    context = {
        'item': delete,
    }
    return render(request, template_name='delete.html', context=context)







 # item_details page

def itemDetails(request, pk):
    iDet = Items.objects.get(id=pk)
    context ={
        'iDetails':  iDet,
    }
    return render(request,template_name='item_details.html',context=context)


# products

# @login_required(login_url='login')
def women(request):
    wo = ProductWomen.objects.all()
    context ={
        'won':  wo,
    }
    return render(request,template_name='women.html',context=context)


def womenDetails(request, pk):
    wDet = ProductWomen.objects.get(id=pk)
    context ={
        'wDetails':  wDet,
    }
    return render(request,template_name='product_details_women.html',context=context)

# @login_required(login_url='login')
def men(request):
    man = Men.objects.all()
    context ={
        'mann':  man,
    }
    return render(request,template_name='men.html',context=context)
def MenDetails(request, pk):
    mDet =Men.objects.get(id=pk)
    context ={
        'm_Details':  mDet,
    }
    return render(request,template_name='product_details_men.html',context=context)






# designer page
def designer(request):
    return render(request, template_name='designer.html')


# cart page


# contact_us page
def contact(request):
    return render(request,template_name='contact_us.html')

@login_required(login_url='loginPage')
#coustomer
@allowed_users(allowed_roles=['customer'])
def userPage(request):
    items = Items.objects.all()
    context = {
        'item': items,
    }

    return render(request,template_name='user.html',context=context)

@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['customer'])

@login_required
def userProfile_add(request):

    if request.method == 'POST':
        form = userProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.username = request.user.username  # Prefill username
            form.save()
            return redirect('userProfile')
    else:
        # Prefill the username field with the username of the logged-in user
        form = userProfileForm(initial={'username': request.user.username})

    context = {
        'form': form
    }
    return render(request,template_name='UserProfileForm.html', context=context)


def userProfile(request):
    try:
        profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        profile = None

    context = {
        'profile': profile
    }
    return render(request, template_name='UserProfile.html', context=context)


def edit_profile(request):
    profile_instance = request.user.userprofile
    form = userProfileForm(instance=profile_instance)

    if request.method == 'POST':
        form = userProfileForm(request.POST, request.FILES, instance=profile_instance)
        if form.is_valid():
            form.save()
            return redirect('userProfile')  # Redirect to the profile page after editing

    context = {
        'form': form
    }
    return render(request, template_name='UserProfileForm.html', context=context)
@login_required(login_url='login')
def cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    context = {
        'cart_items': cart_items,
    }
    #total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request,template_name='cart.html', context=context)


def add_to_cart(request, product_id):
    iDet = Items.objects.get(pk=product_id)
    cart_item, created = Cart.objects.get_or_create(product=iDet, user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart')


def remove_from_cart(request, item_id):
    cart_item = Cart.objects.get(id=item_id)
    cart_item.delete()
    return redirect('cart')

def orders(request):
    order = Order.objects.filter(user=request.user)
    context = {
        'order': order,
    }

    return  render(request,template_name='orders.html',context=context)


def add_orders(request):
    if request.method =='POST':
        form = orderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('orders')
    else:
        # Get the product ID from the query parameters
        product_id = request.GET.get('product_id')
        if product_id:
            # Retrieve the product object based on the ID
            product_obj = get_object_or_404(Items, id=product_id)
            # Pre-fill the form with product details
            initial_data = {
                'product': product_obj,

            }
            form = orderForm(initial=initial_data)
        else:
            form = orderForm()

    context = {
        'form': form
    }
    return render(request, template_name='orderForm.html', context=context)