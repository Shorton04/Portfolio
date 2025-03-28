# portfolio/admin.py
from django.contrib import admin
from django.utils.html import format_html
from .models import Project, Skill, Education, Experience, Contact
from django.urls import path
from django.template.response import TemplateResponse
from django.db.models import Count


class PortfolioAdminSite(admin.AdminSite):
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('portfolio-dashboard/', self.admin_view(self.dashboard_view), name='portfolio-dashboard'),
        ]
        return custom_urls + urls

    def dashboard_view(self, request):
        # Get portfolio statistics
        context = {
            'projects_count': Project.objects.count(),
            'featured_projects': Project.objects.filter(featured=True).count(),
            'skills_by_category': Skill.objects.values('category').annotate(count=Count('id')),
            'total_skills': Skill.objects.count(),
            'title': "Portfolio Dashboard",
            **self.each_context(request),
        }
        return TemplateResponse(request, "admin/portfolio_dashboard.html", context)

    def index(self, request, extra_context=None):
        """Override the default index to add custom statistics."""
        extra_context = extra_context or {}
        extra_context['projects_count'] = Project.objects.count()
        extra_context['featured_projects'] = Project.objects.filter(featured=True).count()
        extra_context['skills_count'] = Skill.objects.count()
        return super().index(request, extra_context=extra_context)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_image', 'date_completed', 'featured')
    list_filter = ('featured', 'technologies')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('technologies',)

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" />', obj.image.url)
        return "No Image"

    display_image.short_description = 'Preview'


class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'proficiency')
    list_filter = ('category', 'proficiency')
    search_fields = ('name',)


class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institution', 'start_date', 'end_date', 'current')
    list_filter = ('current',)
    search_fields = ('degree', 'institution')


class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('position', 'company', 'start_date', 'end_date', 'current')
    list_filter = ('current',)
    search_fields = ('position', 'company')


class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'linkedin', 'github', 'twitter')


# Register models with custom admin classes
admin.site.register(Project, ProjectAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Contact, ContactAdmin)

# Customize admin site header and title
admin.site.site_header = "Marc Dexter Portfolio Admin"
admin.site.site_title = "Portfolio Admin Panel"
admin.site.index_title = "Welcome to Your Portfolio Manager"