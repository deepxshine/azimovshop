# Generated by Django 4.2.7 on 2023-12-14 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория'},
        ),
        migrations.RenameField(
            model_name='parametersinproduct',
            old_name='unit',
            new_name='value',
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(upload_to='category/'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Название категории'),
        ),
        migrations.AlterField(
            model_name='parametersinproduct',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='param', to='goods.product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='product/'),
        ),
    ]
