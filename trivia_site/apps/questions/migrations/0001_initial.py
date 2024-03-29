# Generated by Django 4.2.3 on 2023-07-19 04:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255, verbose_name='question')),
                ('details', models.TextField(blank=True)),
                ('difficulty', models.CharField(blank=True, choices=[('E', 'Easy'), ('M', 'Medium'), ('H', 'Hard')], max_length=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Question',
                'verbose_name_plural': 'Quiz Questions',
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100, verbose_name='choice')),
                ('is_correct', models.BooleanField(default=False)),
                ('details', models.TextField(blank=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='questions.question')),
            ],
        ),
    ]
