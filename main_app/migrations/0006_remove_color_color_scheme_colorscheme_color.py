# Generated by Django 4.0.6 on 2022-07-10 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_alter_color_color_scheme'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='color',
            name='color_scheme',
        ),
        migrations.AddField(
            model_name='colorscheme',
            name='color',
            field=models.ManyToManyField(blank=True, to='main_app.color'),
        ),
    ]
