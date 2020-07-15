from django.db import models
from django.conf import settings
from multiselectfield import MultiSelectField

class Blog (models.Model):
    user = models.CharField(max_length=120,null=True, blank=True)
    title = models.CharField(max_length=120,null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add =True)

    def __str__(self):
        return self.user


SYMPTOMS_CHOICES= (
              ('No_symptoms', 'No symptoms'),
              ('shortness_of_breadth', 'shortness of breadth'),
              ('nasal_congestion', 'nasal congestion'),
              ('dry_cough', 'dry cough'),
              ('feaver', 'feaver'),
              ('sore_throat', 'sore throat'),
              ('runny_nose', 'runny nose'),
              ('diarrhea', 'diarrhea'),
              ('abdomnal_pain', 'abdomnalnpain'),
              ('fatigue', 'fatigue'),
              ('pressure_in_the_chest', 'pressure in the chest'),
              )

class Report (models.Model):
    FILLING_CHOICES =(
        ('Some One Else', 'Some One Else'),
        ('My Self', 'My Self')

         )
    TITLE_CHOICES = (
        ('MR', 'MR'),
        ('MRS', 'Mrs'),
        ('DR', 'DR'),
        ('MISS', 'MISS')
         )
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    Abuja ='FC'
    Abia = 'AB'
    Adamawa = 'AD'
    Akwa_Ibom = 'AK'
    Anambra = 'AN'
    Bauchi = 'BA'
    Bayelsa =  'BY'
    Benue ='BE'
    Borno ='BO'
    Cross_River ='CR'
    Delta ='DE'
    Ebonyi ='EB'
    Edo ='ED'
    Ekiti ='EK'
    Enugu ='EN'
    Gombe ='GO'
    Imo ='IM'
    Jigawa ='JI'
    Kaduna ='KD'
    Kano ='KN'
    Katsina ='KT'
    Kebbi ='KE'
    Kogi ='KO'
    Kwara ='KW'
    Lagos ='LA'
    Nassarawa = 'NA'
    Niger = 'NI'
    Ogun = 'OG'
    Ondo ='ON'
    Osun ='OS'
    Oyo =  'OY'
    Plateau = 'PL'
    Rivers = 'RI'
    Sokoto = 'SO'
    Taraba = 'TA'
    Yobe = 'YO'
    Zamfara = 'ZA'

    STATE_CHOICES = [
        (Abuja, 'abuja'),
        (Abia, 'abia'),
        (Adamawa, 'adamawa'),
        (Akwa_Ibom, 'akwa'),
        (Anambra, 'anambra'),
        (Bauchi, 'bauchi'),
        (Bayelsa, 'bayelsa'),
        (Benue, 'benue'),
        (Borno, 'borno'),
        (Cross_River, 'cross river'),
        (Delta, 'delta'),
        (Ebonyi, 'ebonyi'),
        (Edo, 'edo'),
        (Ekiti, 'ekiti'),
        (Enugu, 'enugu'),
        (Gombe, 'gombe'),
        (Imo, 'imo'),
        (Jigawa, 'jigawa'),
        (Kaduna, 'kaduna'),
        (Kano, 'kano'),
        (Katsina, 'katsina'),
        (Kebbi, 'kebbi'),
        (Kogi, 'kogi'),
        (Kwara, 'kwara'),
        (Lagos, 'lagos'),
        (Nassarawa, 'nassarawa'),
        (Niger, 'niger'),
        (Ogun, 'ogun'),
        (Ondo, 'ondo'),
        (Osun, 'osun'),
        (Oyo, 'oyo'),
        (Plateau, 'plateaue'),
        (Rivers, 'rivers') ,
        (Sokoto, 'sokoto'),
        (Taraba, 'taraba'),
        (Yobe, 'yobe'),
        (Zamfara, 'zamfara') ,
]

    filling_for_who = models.CharField(max_length=150, choices=FILLING_CHOICES)
    symptoms = MultiSelectField(choices=SYMPTOMS_CHOICES)
    title= models.CharField(max_length=10, choices=TITLE_CHOICES)
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    traveled = models.BooleanField(default=False)
    contact= models.BooleanField(default=False)
    treatment = models.BooleanField(default=False)
    state = models.CharField(max_length=2,choices=STATE_CHOICES,default=None)
    address = models.TextField()




    def __str__(self): #Show title as the identifier
        return self.title + " " +self.full_name + ' from '+self.address+" "+ self.state

    def get_user_summary(self):
        return 'name: '+self.full_name + " i am filling for "+ self.filling_for_who + " i experience " + self.symptoms + "my address is " + self.address
        if self.traveled:
            return 'i have traveled out recently'
        if self.contact:
            return 'i have  been in contact with a suspected patient'