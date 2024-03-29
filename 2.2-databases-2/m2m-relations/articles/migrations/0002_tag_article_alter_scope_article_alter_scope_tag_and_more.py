# Generated by Django 4.1.7 on 2023-03-21 19:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='article',
            field=models.ManyToManyField(related_name='tags', through='articles.Scope', to='articles.article'),
        ),
        migrations.AlterField(
            model_name='scope',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scopes', to='articles.article', verbose_name='Тематики статьи'),
        ),
        migrations.AlterField(
            model_name='scope',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scopes', to='articles.tag', verbose_name='Раздел'),
        ),
        migrations.RemoveField(
            model_name='tag',
            name='name',
        ),
        migrations.AddField(
            model_name='tag',
            name='name',
            field=models.CharField(default='#', max_length=20, verbose_name='Тэг'),
        ),
    ]
