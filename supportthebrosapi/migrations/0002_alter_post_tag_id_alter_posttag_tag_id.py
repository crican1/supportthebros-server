# Generated by Django 4.1.3 on 2023-09-18 23:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('supportthebrosapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tag_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tag', to='supportthebrosapi.tag'),
        ),
        migrations.AlterField(
            model_name='posttag',
            name='tag_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post', to='supportthebrosapi.tag'),
        ),
    ]
