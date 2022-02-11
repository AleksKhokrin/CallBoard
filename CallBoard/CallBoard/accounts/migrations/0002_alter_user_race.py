# Generated by Django 3.2.2 on 2021-05-26 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='race',
            field=models.CharField(choices=[('HUM', 'Человек'), ('ORC', 'Орк'), ('UND', 'Нежеть'), ('NIE', 'Ночные эльфы')], default='HUM', max_length=3),
        ),
    ]