# Generated by Django 3.1.3 on 2022-06-08 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diarys', '0003_auto_20220608_0510'),
    ]

    operations = [
        migrations.AddField(
            model_name='routine',
            name='modelkey',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
