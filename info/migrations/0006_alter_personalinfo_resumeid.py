# Generated by Django 3.2 on 2021-04-18 10:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0005_alter_personalinfo_resumeid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalinfo',
            name='resumeId',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='PI_modified', to='info.resume'),
        ),
    ]
