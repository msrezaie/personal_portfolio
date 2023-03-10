# Generated by Django 4.1.5 on 2023-01-30 22:47

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_rename_desc_project_long_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='resume',
            field=models.FileField(blank=True, null=True, upload_to='static/uploads/'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
