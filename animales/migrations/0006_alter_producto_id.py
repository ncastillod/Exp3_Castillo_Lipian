# Generated by Django 4.2.2 on 2023-06-19 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animales', '0005_alter_producto_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='id',
            field=models.PositiveIntegerField(primary_key=True, serialize=False, verbose_name='Id'),
        ),
    ]
