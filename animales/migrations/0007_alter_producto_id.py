# Generated by Django 4.2.2 on 2023-06-20 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animales', '0006_alter_producto_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='id',
            field=models.CharField(max_length=2, primary_key=True, serialize=False, verbose_name='Id'),
        ),
    ]
