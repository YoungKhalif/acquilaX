from django.shortcuts import render, redirect
from .models import BlogPost
from .models import ContactMessage
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, "index.html")

def blog_list(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, "blog.html", {"posts": posts})

def contact_view(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        
        ContactMessage.objects.create(name=name, email=email, message=message)
        messages.success(request, "Message sent successfully!")
        return redirect('contact')

    return render(request, "contact.html")
