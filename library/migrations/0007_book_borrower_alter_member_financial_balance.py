# Generated by Django 4.2.6 on 2023-10-12 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_member_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='borrower',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='library.member'),
        ),
        migrations.AlterField(
            model_name='member',
            name='financial_balance',
            field=models.IntegerField(default=0),
        ),
    ]
