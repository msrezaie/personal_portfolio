# Generated by Django 4.1.5 on 2023-02-01 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0017_alter_project_demo_link_alter_project_source_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
