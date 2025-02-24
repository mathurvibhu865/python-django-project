# Generated by Django 5.0.6 on 2024-05-26 03:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectName', models.CharField(max_length=30)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('clientId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.client')),
                ('createdBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Created_by_User', to=settings.AUTH_USER_MODEL)),
                ('user', models.ManyToManyField(related_name='Name_of_User', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
