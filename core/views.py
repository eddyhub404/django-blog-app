from django.shortcuts import render,redirect
from blog.models import Post, Category
from .models import ContactMessage
from django.contrib import messages

def home(request):
    latest_posts = Post.objects.filter(
        is_published=True
    ).order_by('-created_at')[:3]

    categories = Category.objects.all()

    return render(request, 'core/home.html', {
        'latest_posts': latest_posts,
        'categories': categories
    })
    
def about(request):
    return render(request, 'core/about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        ContactMessage.objects.create(
            name=name,
            email=email,
            message=message
        )

        messages.success(request, "Message sent successfully!")
        return redirect("core:contact")

    return render(request, "core/contact.html")