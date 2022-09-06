# Generated by Django 4.0.6 on 2022-07-13 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_project_project_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='colorscheme',
            name='background',
            field=models.ManyToManyField(blank=True, related_name='background', to='main_app.color'),
        ),
        migrations.AddField(
            model_name='colorscheme',
            name='heading',
            field=models.ManyToManyField(blank=True, related_name='heading', to='main_app.color'),
        ),
        migrations.AlterField(
            model_name='colorscheme',
            name='color',
            field=models.ManyToManyField(blank=True, related_name='color', to='main_app.color'),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_type',
            field=models.CharField(choices=[('P', 'Personal Project'), ('O', 'Other')], default='P', max_length=1),
        ),
    ]