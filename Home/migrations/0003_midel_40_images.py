# Generated by Django 4.2.6 on 2023-11-01 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_top_banner_images_delete_banner_images'),
    ]

    operations = [
        migrations.CreateModel(
            name='Midel_40_Images',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('new', models.CharField(blank=True, max_length=100, null=True)),
                ('new_fashion', models.CharField(blank=True, max_length=100, null=True)),
                ('description_40', models.TextField(blank=True, max_length=500, null=True)),
                ('image', models.ImageField(upload_to='productimg')),
            ],
        ),
    ]
