# Generated by Django 4.0.3 on 2022-05-15 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('truecar', '0004_hatchback_sedan_suv'),
    ]

    operations = [
        migrations.CreateModel(
            name='Allcars',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=50)),
                ('category', models.CharField(default='', max_length=50)),
                ('sub_category', models.CharField(default='', max_length=50)),
                ('make', models.IntegerField(default=0)),
                ('desc', models.CharField(max_length=300)),
                ('pub_date', models.DateField()),
                ('image', models.ImageField(default='', upload_to='allcars/images')),
            ],
        ),
        migrations.DeleteModel(
            name='register',
        ),
    ]
