# Generated by Django 4.0.6 on 2022-07-12 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_remove_color_color_scheme_colorscheme_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_type',
            field=models.CharField(choices=[('P', 'Person Project'), ('O', 'Other')], default='P', max_length=1),
        ),
    ]
