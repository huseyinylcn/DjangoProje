# Generated by Django 4.1.3 on 2023-02-04 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aapMy', '0003_referans'),
    ]

    operations = [
        migrations.AlterField(
            model_name='satilikurun',
            name='text',
            field=models.TextField(max_length=100, verbose_name='Ürün Açıklama'),
        ),
        migrations.AlterField(
            model_name='urun',
            name='text',
            field=models.TextField(max_length=300, verbose_name='Ürün Tanıtım Açıklama'),
        ),
    ]
