# products/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm
from django.contrib import messages

def product_list(request):
    query = request.GET.get("q", "")
    products = Product.objects.filter(name__icontains=query)
    return render(request, 'products/list.html', {'products': products, 'query': query})

def product_create(request):
    form = ProductForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Produk berhasil ditambahkan.")
        return redirect('product_list')
    return render(request, 'products/form.html', {'form': form})

def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(request.POST or None, request.FILES or None, instance=product)
    if form.is_valid():
        form.save()
        messages.success(request, "Produk berhasil diperbarui.")
        return redirect('product_list')
    return render(request, 'products/form.html', {'form': form})

def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        messages.success(request, "Produk berhasil dihapus.")
        return redirect('product_list')
    return render(request, 'products/confirm_delete.html', {'product': product})
