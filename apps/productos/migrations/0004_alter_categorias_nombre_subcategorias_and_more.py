# Generated by Django 4.2.3 on 2023-07-17 15:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0003_alter_categorias_options_alter_productos_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorias',
            name='nombre',
            field=models.CharField(default='', max_length=50, null=True, verbose_name='Nombre'),
        ),
        migrations.CreateModel(
            name='SubCategorias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.ForeignKey(max_length=50, null=True, on_delete=django.db.models.deletion.SET_NULL, to='productos.categorias', verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Subcategoria',
                'verbose_name_plural': 'Subcategorias',
            },
        ),
        migrations.AddField(
            model_name='productos',
            name='nombre_subcategoria',
            field=models.ForeignKey(max_length=50, null=True, on_delete=django.db.models.deletion.SET_NULL, to='productos.subcategorias'),
        ),
    ]
