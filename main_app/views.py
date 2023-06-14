from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Restaurant, Order, Menu_Item
from django.urls import reverse_lazy
from .forms import Menu_ItemForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
def home(request):
    return render(request, 'home.html')

def restaurants_index(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'restaurants/index.html', {
        'restaurants': restaurants
    })

def restaurants_detail(request, restaurant_id):
    restaurant = Restaurant.objects.get(id=restaurant_id)
    menu_item_form = Menu_ItemForm()

    return render(request,'restaurants/detail.html',{
        'restaurant':restaurant, 'menu_item_form':menu_item_form,
    })
@login_required
def add_menu_item(request, restaurant_id):
    form =Menu_ItemForm(request.POST)
    if form.is_valid():
        new_menu_item = form.save(commit=False)
        new_menu_item.restaurant_id= restaurant_id
        new_menu_item.user = request.user
        new_menu_item.save()
    return redirect('detail',restaurant_id=restaurant_id)

class RestaurantCreate(LoginRequiredMixin, CreateView):
    model = Restaurant
    fields = ['name', 'food_type', 'address','phone_number']
    def form_valid(self, form):
        form.instance.user = self.request.user 
        return super().form_valid(form)
        
class RestaurantUpdate(LoginRequiredMixin, UpdateView):
    model = Restaurant
    fields = ['food_type','address','phone_number']

class RestaurantDelete(LoginRequiredMixin, DeleteView):
    model = Restaurant
    success_url = '/restaurants'

class Menu_itemUpdate(LoginRequiredMixin, UpdateView):
    model = Menu_Item
    fields = ['name','price','description']

class Menu_itemDelete(LoginRequiredMixin, DeleteView):
    model = Menu_Item
    def get_success_url(self):
        restaurant_id = self.object.restaurant_id
        success_url = reverse_lazy('detail', kwargs={'restaurant_id': restaurant_id})
        return success_url
    
def signup(request):
  error_message = ''
  if request.method == 'POST':

    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)