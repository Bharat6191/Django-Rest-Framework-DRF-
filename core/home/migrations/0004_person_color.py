# Generated by Django 5.1.3 on 2024-11-09 09:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='color',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='color', to='home.color'),
        ),
    ]