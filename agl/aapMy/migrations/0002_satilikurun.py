# Generated by Django 4.1.3 on 2023-02-04 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aapMy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SatilikUrun',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Ürün Başlık')),
                ('text', models.TextField(verbose_name='Ürün Açıklama')),
                ('image', models.FileField(upload_to='', verbose_name='Ürün Resmi')),
            ],
        ),
    ]
