from django.contrib import admin
from .models import AboutPage, BlogPost, BlogCategory, ContactMessage,CounsellorMessage, CountryPage,AboutDetail, AboutStat, TeamMember, Testimonial, WhyChooseUsPoint
from .models import Service
admin.site.register(BlogPost)
admin.site.register(BlogCategory)
admin.site.register(CounsellorMessage)
admin.site.register(ContactMessage)
admin.site.register(CountryPage)
admin.site.register(AboutDetail)
admin.site.register(AboutStat)
admin.site.register(TeamMember)
admin.site.register(Testimonial)
admin.site.register(WhyChooseUsPoint)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    list_filter = ('category',)
    prepopulated_fields = {'slug': ('name',)}

@admin.register(AboutPage)
class AboutPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'updated_at')











