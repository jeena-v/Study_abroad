from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class AboutPage(models.Model):
    title = models.CharField(max_length=255)  # Page title
    about_content = models.TextField()  # Main About Us content
    mission = models.TextField(blank=True, null=True)
    vision = models.TextField(blank=True, null=True)
    why_choose_us = models.TextField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)  # Auto-update timestamp

    class Meta:
        verbose_name = "About Page Content"
        verbose_name_plural = "About Page Content"

    def __str__(self):
        return self.title

class BlogCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    content = models.TextField()
    category = models.ForeignKey(BlogCategory, on_delete=models.SET_NULL, null=True, blank=True)
    published_date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

from django.db import models
class CounsellorMessage(models.Model):
    STATE_CHOICES = [
        ('', 'Select State'),  # 👈 Added placeholder
        ('Andhra Pradesh', 'Andhra Pradesh'),
        ('Arunachal Pradesh', 'Arunachal Pradesh'),
        ('Assam', 'Assam'),
        ('Bihar', 'Bihar'),
        ('Chhattisgarh', 'Chhattisgarh'),
        ('Goa', 'Goa'),
        ('Gujarat', 'Gujarat'),
        ('Haryana', 'Haryana'),
        ('Himachal Pradesh', 'Himachal Pradesh'),
        ('Jharkhand', 'Jharkhand'),
        ('Karnataka', 'Karnataka'),
        ('Kerala', 'Kerala'),
        ('Madhya Pradesh', 'Madhya Pradesh'),
        ('Maharashtra', 'Maharashtra'),
        ('Manipur', 'Manipur'),
        ('Meghalaya', 'Meghalaya'),
        ('Mizoram', 'Mizoram'),
        ('Nagaland', 'Nagaland'),
        ('Odisha', 'Odisha'),
        ('Punjab', 'Punjab'),
        ('Rajasthan', 'Rajasthan'),
        ('Sikkim', 'Sikkim'),
        ('Tamil Nadu', 'Tamil Nadu'),
        ('Telangana', 'Telangana'),
        ('Tripura', 'Tripura'),
        ('Uttar Pradesh', 'Uttar Pradesh'),
        ('Uttarakhand', 'Uttarakhand'),
        ('West Bengal', 'West Bengal'),
        # Union Territories
        ('Andaman and Nicobar Islands', 'Andaman and Nicobar Islands'),
        ('Chandigarh', 'Chandigarh'),
        ('Dadra and Nagar Haveli and Daman and Diu', 'Dadra and Nagar Haveli and Daman and Diu'),
        ('Delhi', 'Delhi'),
        ('Jammu and Kashmir', 'Jammu and Kashmir'),
        ('Ladakh', 'Ladakh'),
        ('Lakshadweep', 'Lakshadweep'),
        ('Puducherry', 'Puducherry'),
    ]

    COUNTRY_CHOICES = [
        ('', 'Select Country'),  # 👈 Added placeholder
        ('USA', 'USA'),
        ('UK', 'UK'),
        ('Canada', 'Canada'),
        ('Australia', 'Australia'),
        ('France', 'France'),
        ('Ireland', 'Ireland'),
        ('Germany', 'Germany'),
        ('Newzealand', 'Newzealand'),
        ('UAE', 'UAE'),
        ('Other', 'Other'),
    ]

    INTAKE_CHOICES = [
        ('', 'Select Intake'),  # 👈 Added placeholder
        ('Jan 2025', 'Jan 2025'),
        ('May 2025', 'May 2025'),
        ('Sep 2025', 'Sep 2025'),
        ('Jan 2026', 'Jan 2026'),
        ('May 2026', 'May 2026'),
        ('Sep 2026', 'Sep 2026'),
        ('Other', 'Other'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100, choices=STATE_CHOICES, blank=True)
    target_country = models.CharField(max_length=100, choices=COUNTRY_CHOICES, blank=True)
    target_intake = models.CharField(max_length=100, choices=INTAKE_CHOICES, blank=True)
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class CounsellingPopup(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return self.name
    
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    subject = models.CharField(max_length=150)
    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name    

from django.db import models
from django.utils.text import slugify



class Service(models.Model):
    CATEGORY_CHOICES = [
        ('counselling', 'Counselling'),
        ('testprep', 'Test Prep'),
        ('other', 'Other Services'),
    ]

    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    about_text = models.TextField(blank=True)
    benefits_text = models.TextField(blank=True)
    why_choose_text = models.TextField(blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)



class CountryPage(models.Model):
    name = models.CharField(max_length=100)  # e.g. "Study in UK"
    slug = models.SlugField(unique=True)     # e.g. "study-in-uk"
    about_text = models.TextField()
    benefits_text = models.TextField()
    why_choose_text = models.TextField()

    def __str__(self):
        return self.name

