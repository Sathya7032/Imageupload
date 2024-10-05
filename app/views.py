from django.shortcuts import render
from .models import Category, Image


def index(request):
    categories = Category.objects.all()
    selected_category = request.GET.get('category')
    images = Image.objects.filter(category__id=selected_category) if selected_category else Image.objects.none()

    context = {
        'categories': categories,
        'images': images,
        'selected_category': selected_category,
    }
    return render(request, 'index.html', context)