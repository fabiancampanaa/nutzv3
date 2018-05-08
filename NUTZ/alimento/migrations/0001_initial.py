# Generated by Django 2.0.5 on 2018-05-08 22:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('cho', models.IntegerField()),
                ('lipidos', models.IntegerField()),
                ('proteinas', models.IntegerField()),
                ('azucares', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TipoAlimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('cho_prom', models.IntegerField()),
                ('lipidos_prom', models.IntegerField()),
                ('proteinas_prom', models.IntegerField()),
                ('azucares_prom', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='alimento',
            name='tipo_alimento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aliemntos', to='alimento.TipoAlimento'),
        ),
    ]