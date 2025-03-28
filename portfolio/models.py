# portfolio/models.py
from django.db import models
from django.utils.text import slugify


class Skill(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=50, help_text="Font Awesome icon class")
    category = models.CharField(max_length=50, choices=[
        ('frontend', 'Frontend'),
        ('backend', 'Backend'),
        ('mobile', 'Mobile'),
        ('ai', 'AI/ML'),
        ('other', 'Other')
    ])
    proficiency = models.IntegerField(choices=[(i, i) for i in range(1, 6)])

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-proficiency', 'name']


class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True)
    technologies = models.ManyToManyField(Skill, related_name='projects')
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    featured = models.BooleanField(default=False)
    date_completed = models.DateField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-date_completed']


class Education(models.Model):
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    field_of_study = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    current = models.BooleanField(default=False)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.degree} - {self.institution}"

    class Meta:
        ordering = ['-end_date', '-start_date']


class Experience(models.Model):
    company = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    current = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.position} at {self.company}"

    class Meta:
        ordering = ['-end_date', '-start_date']


class Contact(models.Model):
    email = models.EmailField()
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    twitter = models.URLField(blank=True)

    def __str__(self):
        return self.email