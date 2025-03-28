# Generated by Django 4.2.10 on 2025-03-28 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('linkedin', models.URLField(blank=True)),
                ('github', models.URLField(blank=True)),
                ('twitter', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution', models.CharField(max_length=200)),
                ('degree', models.CharField(max_length=200)),
                ('field_of_study', models.CharField(max_length=200)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('current', models.BooleanField(default=False)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['-end_date', '-start_date'],
            },
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=200)),
                ('position', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('current', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-end_date', '-start_date'],
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('icon', models.CharField(help_text='Font Awesome icon class', max_length=50)),
                ('category', models.CharField(choices=[('frontend', 'Frontend'), ('backend', 'Backend'), ('mobile', 'Mobile'), ('ai', 'AI/ML'), ('other', 'Other')], max_length=50)),
                ('proficiency', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
            ],
            options={
                'ordering': ['-proficiency', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, max_length=200, unique=True)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='projects/')),
                ('github_url', models.URLField(blank=True)),
                ('live_url', models.URLField(blank=True)),
                ('featured', models.BooleanField(default=False)),
                ('date_completed', models.DateField()),
                ('technologies', models.ManyToManyField(related_name='projects', to='portfolio.skill')),
            ],
            options={
                'ordering': ['-date_completed'],
            },
        ),
    ]
