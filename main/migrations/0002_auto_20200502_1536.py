# Generated by Django 3.0.5 on 2020-05-02 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='answer_question',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='main.Questions'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='answer',
            name='answer_corectly',
            field=models.TextField(),
        ),
    ]