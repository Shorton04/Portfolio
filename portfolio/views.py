# portfolio/views.py
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, FormView
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Project, Skill, Education, Experience, Contact
from .forms import ContactForm


def home_view(request):
    featured_projects = Project.objects.filter(featured=True)[:3]
    skills = Skill.objects.all()
    frontend_skills = skills.filter(category='frontend')
    backend_skills = skills.filter(category='backend')
    mobile_skills = skills.filter(category='mobile')
    ai_skills = skills.filter(category='ai')

    context = {
        'featured_projects': featured_projects,
        'frontend_skills': frontend_skills,
        'backend_skills': backend_skills,
        'mobile_skills': mobile_skills,
        'ai_skills': ai_skills,
    }
    return render(request, 'index.html', context)


def about_view(request):
    education = Education.objects.all()
    experience = Experience.objects.all()

    context = {
        'education': education,
        'experience': experience,
    }
    return render(request, 'about.html', context)


class ProjectListView(ListView):
    model = Project
    template_name = 'projects.html'
    context_object_name = 'projects'
    paginate_by = 6


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'project_detail.html'
    context_object_name = 'project'
    slug_url_kwarg = 'project_slug'


class ContactFormView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')

    def form_valid(self, form):
        form.send_email()
        messages.success(self.request, 'Your message has been sent. I will get back to you soon!')
        return super().form_valid(form)