# Generated by Django 3.2.5 on 2021-07-06 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tienda', '0002_rename_leermastarde_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.CharField(max_length=300),
        ),
    ]
