from django.shortcuts import render
from .models import Product, Category, Tag

def product_list(request):
    products = Product.objects.select_related("category").prefetch_related("tags")
    categories = Category.objects.all()
    tags = Tag.objects.all()

    search_query = request.GET.get("search", "").strip()
    selected_category = request.GET.get("category", "")
    selected_tags = request.GET.getlist("tags")

    if search_query:
        products = products.filter(description__icontains=search_query)

    if selected_category:
        products = products.filter(category__id=selected_category)

    if selected_tags:
        products = products.filter(tags__id__in=selected_tags).distinct()

    context = {
        'products': products,
        'categories': categories,
        'tags': tags,
        'search_query': search_query,
        'selected_category': selected_category,
        'selected_tags': selected_tags
    }
    return render(request, 'products/product_list.html', context)

 
