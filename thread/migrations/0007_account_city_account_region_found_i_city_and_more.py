# Generated by Django 4.2 on 2023-05-11 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thread', '0006_found_i_post_date_found_p_post_date_lost_i_post_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='city',
            field=models.CharField(choices=[('BD', 'Bahrdar'), ('AD', 'Adama'), ('AA', 'Addis Ababa'), ('JJ', 'Jigjiga')], default='Addis Abeba'),
        ),
        migrations.AddField(
            model_name='account',
            name='region',
            field=models.CharField(choices=[('AM', 'Amhara'), ('ORO', 'Oromia'), ('AA', 'Addis Abeba'), ('SUMA', 'Sumlia')], default='Addis Abeba'),
        ),
        migrations.AddField(
            model_name='found_i',
            name='city',
            field=models.CharField(choices=[('BD', 'Bahrdar'), ('AD', 'Adama'), ('AA', 'Addis Ababa'), ('JJ', 'Jigjiga')], default='Addis Abeba'),
        ),
        migrations.AddField(
            model_name='found_i',
            name='region',
            field=models.CharField(choices=[('AM', 'Amhara'), ('ORO', 'Oromia'), ('AA', 'Addis Abeba'), ('SUMA', 'Sumlia')], default='Addis Abeba'),
        ),
        migrations.AddField(
            model_name='found_p',
            name='city',
            field=models.CharField(choices=[('BD', 'Bahrdar'), ('AD', 'Adama'), ('AA', 'Addis Ababa'), ('JJ', 'Jigjiga')], default='Addis Abeba'),
        ),
        migrations.AddField(
            model_name='found_p',
            name='region',
            field=models.CharField(choices=[('AM', 'Amhara'), ('ORO', 'Oromia'), ('AA', 'Addis Abeba'), ('SUMA', 'Sumlia')], default='Addis Abeba'),
        ),
        migrations.AddField(
            model_name='lost_i',
            name='city',
            field=models.CharField(choices=[('BD', 'Bahrdar'), ('AD', 'Adama'), ('AA', 'Addis Ababa'), ('JJ', 'Jigjiga')], default='Addis Abeba'),
        ),
        migrations.AddField(
            model_name='lost_i',
            name='region',
            field=models.CharField(choices=[('AM', 'Amhara'), ('ORO', 'Oromia'), ('AA', 'Addis Abeba'), ('SUMA', 'Sumlia')], default='Addis Abeba'),
        ),
        migrations.AddField(
            model_name='lost_p',
            name='city',
            field=models.CharField(choices=[('BD', 'Bahrdar'), ('AD', 'Adama'), ('AA', 'Addis Ababa'), ('JJ', 'Jigjiga')], default='Addis Abeba'),
        ),
        migrations.AddField(
            model_name='lost_p',
            name='region',
            field=models.CharField(choices=[('AM', 'Amhara'), ('ORO', 'Oromia'), ('AA', 'Addis Abeba'), ('SUMA', 'Sumlia')], default='Addis Abeba'),
        ),
        migrations.AddField(
            model_name='matched_i',
            name='city',
            field=models.CharField(choices=[('BD', 'Bahrdar'), ('AD', 'Adama'), ('AA', 'Addis Ababa'), ('JJ', 'Jigjiga')], default='Addis Abeba'),
        ),
        migrations.AddField(
            model_name='matched_i',
            name='region',
            field=models.CharField(choices=[('AM', 'Amhara'), ('ORO', 'Oromia'), ('AA', 'Addis Abeba'), ('SUMA', 'Sumlia')], default='Addis Abeba'),
        ),
        migrations.AddField(
            model_name='matched_p',
            name='city',
            field=models.CharField(choices=[('BD', 'Bahrdar'), ('AD', 'Adama'), ('AA', 'Addis Ababa'), ('JJ', 'Jigjiga')], default='Addis Abeba'),
        ),
        migrations.AddField(
            model_name='matched_p',
            name='region',
            field=models.CharField(choices=[('AM', 'Amhara'), ('ORO', 'Oromia'), ('AA', 'Addis Abeba'), ('SUMA', 'Sumlia')], default='Addis Abeba'),
        ),
        migrations.AddField(
            model_name='wanted_p',
            name='city',
            field=models.CharField(choices=[('BD', 'Bahrdar'), ('AD', 'Adama'), ('AA', 'Addis Ababa'), ('JJ', 'Jigjiga')], default='Addis Abeba'),
        ),
        migrations.AddField(
            model_name='wanted_p',
            name='region',
            field=models.CharField(choices=[('AM', 'Amhara'), ('ORO', 'Oromia'), ('AA', 'Addis Abeba'), ('SUMA', 'Sumlia')], default='Addis Abeba'),
        ),
    ]