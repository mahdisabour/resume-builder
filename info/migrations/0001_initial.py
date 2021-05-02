# Generated by Django 3.2 on 2021-04-16 15:20

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('userId', models.BigIntegerField(primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(auto_now_add=True, null=True)),
                ('date_modified', models.DateField(auto_now_add=True, null=True)),
                ('resumeTitle', models.CharField(blank=True, max_length=50, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resumes', to='info.owner')),
            ],
        ),
        migrations.CreateModel(
            name='WebsiteAndSocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(auto_now_add=True, null=True)),
                ('date_modified', models.DateField(auto_now_add=True)),
                ('label', models.CharField(blank=True, max_length=50)),
                ('link', models.CharField(max_length=50)),
                ('resumeId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='WSMedia_modified', to='info.resume')),
            ],
        ),
        migrations.CreateModel(
            name='skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(auto_now_add=True, null=True)),
                ('date_modified', models.DateField(auto_now_add=True)),
                ('skill', models.CharField(max_length=50)),
                ('level', models.IntegerField(default=5, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('resumeId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='skills_modified', to='info.resume')),
            ],
        ),
        migrations.CreateModel(
            name='PersonalInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_modified', models.DateField(auto_now_add=True)),
                ('wantedJobTitle', models.CharField(blank=True, max_length=50, null=True)),
                ('firstName', models.CharField(blank=True, max_length=50, null=True)),
                ('lastName', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(blank=True, max_length=100, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=250, null=True)),
                ('postalCode', models.CharField(blank=True, max_length=250, null=True)),
                ('nationality', models.CharField(blank=True, max_length=50, null=True)),
                ('placeOfBirth', models.CharField(blank=True, max_length=250, null=True)),
                ('dateOfBirth', models.DateField(blank=True, null=True)),
                ('personalSummary', models.TextField(blank=True, null=True)),
                ('resumeId', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='PI_modified', to='info.resume')),
            ],
        ),
        migrations.CreateModel(
            name='language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(auto_now_add=True, null=True)),
                ('date_modified', models.DateField(auto_now_add=True)),
                ('language', models.CharField(max_length=70)),
                ('level', models.CharField(blank=True, choices=[('1', 'Native Speaker'), ('2', 'Highly proficient'), ('3', 'Very goog command')], max_length=50)),
                ('resumeId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='languages_modified', to='info.resume')),
            ],
        ),
        migrations.CreateModel(
            name='EmploymentHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(auto_now_add=True, null=True)),
                ('date_modified', models.DateField(auto_now_add=True)),
                ('jobTitle', models.CharField(blank=True, max_length=50)),
                ('employer', models.CharField(blank=True, max_length=250)),
                ('startDate', models.DateField(blank=True, null=True)),
                ('endDate', models.DateField(blank=True, null=True)),
                ('city', models.CharField(blank=True, max_length=250, null=True)),
                ('description', models.TextField(blank=True)),
                ('resumeId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='EH_modified', to='info.resume')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(auto_now_add=True, null=True)),
                ('date_modified', models.DateField(auto_now_add=True)),
                ('school', models.CharField(blank=True, max_length=50)),
                ('degree', models.CharField(blank=True, max_length=250)),
                ('startDate', models.DateField(blank=True, null=True)),
                ('endDate', models.DateField(blank=True, null=True)),
                ('city', models.CharField(blank=True, max_length=250, null=True)),
                ('description', models.TextField(blank=True)),
                ('resumeId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Ed_modified', to='info.resume')),
            ],
        ),
        migrations.CreateModel(
            name='course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(auto_now_add=True, null=True)),
                ('date_modified', models.DateField(auto_now_add=True)),
                ('course', models.CharField(blank=True, max_length=50)),
                ('institution', models.CharField(blank=True, max_length=50)),
                ('startDate', models.DateField(blank=True, null=True)),
                ('endDate', models.DateField(blank=True, null=True)),
                ('resumeId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='courses_modified', to='info.resume')),
            ],
        ),
    ]