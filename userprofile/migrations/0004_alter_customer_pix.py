# Generated by Django 4.1 on 2022-08-16 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0003_alter_cart_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='pix',
            field=models.ImageField(blank=True, null=True, upload_to='customer'),
        ),
    ]
