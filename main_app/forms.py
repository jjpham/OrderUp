from django.forms import ModelForm
from .models import Menu_Item

class Menu_ItemForm(ModelForm):
    class Meta:
        model = Menu_Item
        fields = ['name','price','description']
