# Generated by Django 2.2.5 on 2020-07-13 23:06

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200517_1841'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filling_for_who', models.CharField(choices=[('Some One Else', 'Some One Else'), ('My Self', 'My Self')], max_length=150)),
                ('symptoms', multiselectfield.db.fields.MultiSelectField(choices=[('No_symptoms', 'No symptoms'), ('shortness_of_breadth', 'shortness of breadth'), ('nasal_congestion', 'nasal congestion'), ('dry_cough', 'dry cough'), ('feaver', 'feaver'), ('sore_throat', 'sore throat'), ('runny_nose', 'runny nose'), ('diarrhea', 'diarrhea'), ('abdomnal_pain', 'abdomnalnpain'), ('fatigue', 'fatigue'), ('pressure_in_the_chest', 'pressure in the chest')], max_length=142)),
                ('title', models.CharField(choices=[('MR', 'MR'), ('MRS', 'Mrs'), ('DR', 'DR'), ('MISS', 'MISS')], max_length=10)),
                ('full_name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('traveled', models.BooleanField(default=False)),
                ('contact', models.BooleanField(default=False)),
                ('treatment', models.BooleanField(default=False)),
                ('state', models.CharField(choices=[('FC', 'abuja'), ('AB', 'abia'), ('AD', 'adamawa'), ('AK', 'akwa'), ('AN', 'anambra'), ('BA', 'bauchi'), ('BY', 'bayelsa'), ('BE', 'benue'), ('BO', 'borno'), ('CR', 'cross river'), ('DE', 'delta'), ('EB', 'ebonyi'), ('ED', 'edo'), ('EK', 'ekiti'), ('EN', 'enugu'), ('GO', 'gombe'), ('IM', 'imo'), ('JI', 'jigawa'), ('KD', 'kaduna'), ('KN', 'kano'), ('KT', 'katsina'), ('KE', 'kebbi'), ('KO', 'kogi'), ('KW', 'kwara'), ('LA', 'lagos'), ('NA', 'nassarawa'), ('NI', 'niger'), ('OG', 'ogun'), ('ON', 'ondo'), ('OS', 'osun'), ('OY', 'oyo'), ('PL', 'plateaue'), ('RI', 'rivers'), ('SO', 'sokoto'), ('TA', 'taraba'), ('YO', 'yobe'), ('ZA', 'zamfara')], default=None, max_length=2)),
                ('address', models.TextField()),
            ],
        ),
    ]
