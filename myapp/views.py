from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Product

# Index view to list all products
def index(request):
    products = Product.objects.all()
    return render(request, 'myapp/index.html', {'products': products})

# Show view to display a specific product by ID
def show(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'myapp/show.html', {'product': product})