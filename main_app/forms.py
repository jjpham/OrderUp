from django.forms import ModelForm
from .models import Menu_Item, Order

class Menu_ItemForm(ModelForm):
    class Meta:
        model = Menu_Item
        fields = ['name','price','description']
class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['name','cost','phone_number']
