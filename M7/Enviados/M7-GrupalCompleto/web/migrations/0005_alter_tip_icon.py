# Generated by Django 4.0.4 on 2022-05-04 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_rename_t_icon_tip_icon_rename_t_text_tip_text_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tip',
            name='icon',
            field=models.CharField(choices=[('agua', 'fa-solid fa-droplet'), ('comida', 'fa-solid fa-wheat-awn'), ('deporte', 'fa-solid fa-person-running'), ('medicamento', 'fa-solid fa-comment-medical'), ('otros', 'fa-solid fa-comment')], max_length=100),
        ),
    ]