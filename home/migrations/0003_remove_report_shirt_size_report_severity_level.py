# Generated by Django 5.0.6 on 2024-05-26 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_report_shirt_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='shirt_size',
        ),
        migrations.AddField(
            model_name='report',
            name='severity_level',
            field=models.CharField(choices=[('1', 'Level1'), ('2', 'Level2'), ('3', 'Level3'), ('4', 'Level4'), ('5', 'Level5')], default=1, max_length=1),
            preserve_default=False,
        ),
    ]
