# Generated by Django 3.2.5 on 2021-07-03 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_project_draft'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='pages.project'),
        ),
    ]
