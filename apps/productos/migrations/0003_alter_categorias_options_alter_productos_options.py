# Generated by Django 4.2.3 on 2023-07-16 03:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_alter_productos_nombre_categoria'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categorias',
            options={'verbose_name': 'Categoria', 'verbose_name_plural': 'Categorias'},
        ),
        migrations.AlterModelOptions(
            name='productos',
            options={'verbose_name': 'Producto', 'verbose_name_plural': 'Productos'},
        ),
    ]