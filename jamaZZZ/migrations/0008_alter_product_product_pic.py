# Generated by Django 5.1.2 on 2024-11-01 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jamaZZZ', '0007_alter_design_design_pic_alter_items_item_pic_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_pic',
            field=models.ImageField(blank=True, default='images/Default_pic.jpg', null=True, upload_to='images/'),
        ),
    ]
