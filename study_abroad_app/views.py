from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib import messages
from django.db.models import Q
from .forms import ContactForm, CounsellorMessageForm

# Create your views here.

def index(request):
    return render(request,'study_abroad_app/index.html')

def about(request):
    about_data = AboutPage.objects.first()  # Fetch first (only) record
    return render(request, 'study_abroad_app/about.html', {'about_data': about_data})


def blog(request):
    return render(request,'study_abroad_app/blog.html')

def courses(request):
    return render(request,'study_abroad_app/courses.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully.")
            return redirect('contact')  # Use redirect after POST (recommended)
    else:
        form = ContactForm()
    return render(request, 'study_abroad_app/contact.html', {'form': form})

def counsellor_form(request):
    if request.method == 'POST':
        form = CounsellorMessageForm(request.POST)
        if form.is_valid():
            instance = form.save()
            
            # Send email to admin
            subject = 'New Counsellor Enquiry'
            admin_email = 'youradmin@example.com'
            message = f"""
Name: {instance.first_name} {instance.last_name}
Email: {instance.email}
Phone: {instance.phone}
City: {instance.city}
State: {instance.state}
Target Country: {instance.target_country}
Target Intake: {instance.target_intake}
Message: {instance.message}
            """
            send_mail(subject, message, 'noreply@yourdomain.com', [admin_email])

            messages.success(request, '✅ Thank you! Our counsellors will contact you soon.')
            return redirect('counsellors')
    else:
        form = CounsellorMessageForm()

    return render(request, 'study_abroad_app/counsellors.html', {'form': form})

from django.shortcuts import redirect
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib import messages
from .forms import CounsellingPopupForm

def counselling_popup(request):
    if request.method == 'POST':
        form = CounsellingPopupForm(request.POST)
        if form.is_valid():
            instance = form.save()

            # Send email to admin
            subject = 'New Popup Counselling Request'
            message = render_to_string('study_abroad_app/contactmail.html', {
                'name': instance.name,
                'phoneno': instance.phone,
                'email': instance.email,
                'message': instance.message,
            })
            send_mail(subject, message, 'noreply@gocosys.com', ['jeenav.valsan@gmail.com'])

            messages.success(request, '✅ Thank you! We will contact you shortly.')
            return redirect('index')  # or any page you want to reload
    return redirect('index')

   

from django.shortcuts import render, get_object_or_404
from .models import AboutPage, BlogPost, BlogCategory, CountryPage,  Service

def blog_list(request):
    posts = BlogPost.objects.all().order_by('-published_date')
    recent_posts = BlogPost.objects.order_by('-published_date')[:5]  # last 5 posts
    return render(request, 'study_abroad_app/blog.html', {
        'posts': posts,
        'recent_posts': recent_posts,
    })
def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    recent_posts = BlogPost.objects.exclude(slug=slug).order_by('-published_date')[:5]
    return render(request, 'study_abroad_app/blog_detail.html', {'post': post, 'posts': recent_posts})

def search_view(request):
    query = request.GET.get('q')
    results = []

    if query:
        blog_posts = BlogPost.objects.filter(title__icontains=query)
        countries = CountryPage.objects.filter(name__icontains=query)
        services = Service.objects.filter(name__icontains=query)

        # Add a 'type' attribute for template to distinguish
        results = []
        for blog in blog_posts:
            blog.type = 'blog'
            results.append(blog)
        for country in countries:
            country.type = 'country'
            results.append(country)
        for service in services:
            service.type = 'service'
            results.append(service)

    return render(request, 'study_abroad_app/search_results.html', {
        'query': query,
        'results': results,
    })

def about_details(request):
    return render(request, 'study_abroad_app/about-details.html')



def country_detail(request, slug):
    country = CountryPage.objects.get(slug=slug)
    return render(request, 'study_abroad_app/country_detail.html', {'country': country})

def country_list(request):
    return {'countries': CountryPage.objects.all()}

def service_detail(request, slug):
    service = get_object_or_404(Service, slug=slug)
    return render(request, 'study_abroad_app/service_detail.html', {'service': service})