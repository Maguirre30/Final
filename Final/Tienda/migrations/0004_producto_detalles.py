# Generated by Django 3.2.5 on 2021-07-06 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tienda', '0003_alter_producto_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='detalles',
            field=models.CharField(default=1, max_length=2000),
            preserve_default=False,
        ),
    ]
