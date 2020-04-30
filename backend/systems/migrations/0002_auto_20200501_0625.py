# Generated by Django 3.0.2 on 2020-04-30 22:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('systems', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='roles',
        ),
        migrations.AddField(
            model_name='role',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth.Group', verbose_name='group'),
        ),
    ]
