from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import About, Product, Contact
from django.shortcuts import render, get_object_or_404
from .models import Product, ProductDetails

def home(request):
    return render(request, 'index.html')

def about(request):
    about_data = About.objects.all()
    return render(request, 'about.html', {'about_data': about_data})


def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_success')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def contact_success(request):
    return render(request, 'contact_success.html')

def product_details(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product_details = get_object_or_404(ProductDetails, product=product)
    return render(request, 'product_details.html', {'product': product, 'product_details': product_details})