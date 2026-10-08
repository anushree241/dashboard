from django.shortcuts import render
from django.db.models import Sum, Max
from .models import Product
def dashboard(request):
    products = Product.objects.all()
    context = {
    'total_products': products.count(),
    'total_categories': products.values('category').distinct().count(),
    'total_value': products.aggregate(Sum('price'))['price__sum'] or 0,
    'highest_price': products.aggregate(Max('price'))['price__max'] or 0,
    }
    return render(request, 'dashboard.html', context)