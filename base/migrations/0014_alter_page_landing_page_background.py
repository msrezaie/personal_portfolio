# Generated by Django 4.1.5 on 2023-01-30 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_alter_profile_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='landing_page_background',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
