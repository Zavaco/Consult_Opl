# Generated by Django 3.1.2 on 2020-10-24 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home_Page', '0002_student_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='level',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
