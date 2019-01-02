# Generated by Django 2.1.3 on 2018-12-29 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_camping_tracking'),
    ]

    operations = [
        migrations.CreateModel(
            name='VisaInquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visa_name', models.CharField(max_length=30)),
                ('visa_mobile', models.IntegerField(blank=True, null=True)),
                ('visa_email', models.EmailField(max_length=20)),
                ('visa_course', models.CharField(max_length=60)),
                ('visa_country', models.CharField(max_length=60)),
            ],
        ),
    ]
