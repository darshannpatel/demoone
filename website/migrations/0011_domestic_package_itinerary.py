# Generated by Django 2.1.3 on 2018-12-31 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_passport'),
    ]

    operations = [
        migrations.AddField(
            model_name='domestic',
            name='package_itinerary',
            field=models.FileField(default='website/itinerary/newbalaji.pdf', upload_to='website/itinerary'),
        ),
    ]
