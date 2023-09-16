# Generated by Django 4.2.1 on 2023-09-15 11:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LGA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lga_name', models.CharField(max_length=30)),
                ('lga_id', models.CharField(help_text='This field is automatically populated. But you can input your preferred value, if need be.', max_length=70)),
                ('lga_description', models.CharField(max_length=200)),
                ('entered_by_user', models.CharField(max_length=70)),
                ('date_entered', models.DateTimeField(auto_now_add=True)),
                ('user_ip_address', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'LGA',
                'verbose_name_plural': "LGA's",
            },
        ),
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('party_name', models.CharField(max_length=10)),
                ('party_id', models.CharField(help_text='This field is automatically populated. But you can input your preferred value, if need be.', max_length=7)),
            ],
            options={
                'verbose_name': 'Party',
                'verbose_name_plural': 'Parties',
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_id', models.PositiveIntegerField()),
                ('state_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Ward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ward_name', models.CharField(max_length=20)),
                ('ward_id', models.CharField(help_text='This field is automatically populated. But you can input your preferred value, if need be.', max_length=10)),
                ('ward_description', models.CharField(max_length=200)),
                ('entered_by_user', models.CharField(max_length=70)),
                ('date_entered', models.DateTimeField(auto_now_add=True)),
                ('lga_id', models.ForeignKey(help_text="If you can't find the LGA, then add it, using the green plus button", on_delete=django.db.models.deletion.CASCADE, to='polling_units.state')),
            ],
        ),
        migrations.CreateModel(
            name='PollingUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('polling_unit_name', models.CharField(max_length=70, null=True)),
                ('polling_unit_id', models.PositiveIntegerField(unique=True)),
                ('polling_unit_number', models.PositiveIntegerField(default=0)),
                ('polling_unit_description', models.CharField(max_length=200, null=True)),
                ('lattitude', models.CharField(max_length=70, null=True)),
                ('longitude', models.CharField(max_length=70, null=True)),
                ('entered_by_user', models.CharField(max_length=70)),
                ('date_entered', models.DateTimeField(auto_now_add=True)),
                ('user_ip_address', models.CharField(max_length=70, null=True, verbose_name="User's IP-address")),
                ('lga_id', models.ForeignKey(help_text="If you can't find the LGA, then add it, using the green plus button", on_delete=django.db.models.deletion.CASCADE, to='polling_units.lga', verbose_name='LGA-Id')),
                ('ward_id', models.ForeignKey(help_text="If you can't find the Ward, then add it, using the green plus button", on_delete=django.db.models.deletion.CASCADE, to='polling_units.ward', verbose_name='Ward-Id')),
            ],
            options={
                'verbose_name': 'Polling unit',
                'verbose_name_plural': 'Polling units',
            },
        ),
        migrations.AddField(
            model_name='lga',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='state', to='polling_units.state', verbose_name='State-Id'),
        ),
    ]
