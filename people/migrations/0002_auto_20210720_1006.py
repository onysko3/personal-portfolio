# Generated by Django 3.2.5 on 2021-07-20 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='person',
            name='resume',
            field=models.FileField(blank=True, null=True, upload_to='resume/'),
        ),
    ]