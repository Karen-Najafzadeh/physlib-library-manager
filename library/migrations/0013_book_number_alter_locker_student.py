# Generated by Django 4.2.6 on 2023-10-16 16:43

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0012_alter_member_student_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='number',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(99)]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='locker',
            name='student',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lockers', to='library.member'),
        ),
    ]