# Generated by Django 4.1 on 2022-08-16 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_phone_pix'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='pix',
            field=models.ImageField(default='avatar.png', upload_to='pix'),
        ),
    ]
