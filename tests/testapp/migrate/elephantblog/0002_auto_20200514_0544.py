# Generated by Django 3.0.6 on 2020-05-14 05:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('elephantblog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='author',
            field=models.ForeignKey(limit_choices_to={'is_staff': True}, on_delete=django.db.models.deletion.CASCADE, related_name='elephantblog_entry_blogentries', to=settings.AUTH_USER_MODEL, verbose_name='author'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='categories',
            field=models.ManyToManyField(blank=True, related_name='elephantblog_entry_blogentries', to='elephantblog.Category', verbose_name='categories'),
        ),
    ]
