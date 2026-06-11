from django.shortcuts import render
from blog.models import Post, Category

def home(request):
    latest_posts = Post.objects.filter(
        is_published=True
    ).order_by('-created_at')[:3]

    categories = Category.objects.all()

    return render(request, 'core/home.html', {
        'latest_posts': latest_posts,
        'categories': categories
    })