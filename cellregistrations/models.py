from django.db import models


class CommunityGroup(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class SubCommunity(models.Model):
    name = models.CharField(max_length=200)
    group = models.ForeignKey(CommunityGroup, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class MembersDetail(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]
    MARITAL_STATUS_CHOICES = (
    ('Single', 'Single'),
    ('Married', 'Married'),
    ('Divorced', 'Divorced'),
    ('Widowed', 'Widowed'),
    )
    
    AGE_CHOICES = [
        ('18-25', '18-25'),
        ('26-34', '26-34'),
        ('35-39', '35-39'),
        ('40-49', '40-49'),
        ('50 and above', '50 and above')
    ]
    
    YES = 'Y'
    NO = 'N'
    MEMBER_CHOICES = [
        (YES, 'Yes'),
        (NO, 'No'),
    ]

    YES = 'Y'
    NO = 'N'
    FIRST_TIME = [
        (YES, 'Yes'),
        (NO, 'No'),
    ]
    sub_community = models.ForeignKey(SubCommunity, on_delete=models.CASCADE)
    email = models.EmailField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    whatsapp_number = models.CharField(max_length=15, default='+234', verbose_name='WhatsApp Number')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='male')
    age = models.CharField(max_length=15, choices=AGE_CHOICES, default='', verbose_name='Age Bracket')
    marital_status = models.CharField(max_length=20, choices=MARITAL_STATUS_CHOICES, default='')
    city = models.CharField(max_length=50, default='')
    country = models.CharField(max_length=50, default='',verbose_name='Country of residence')
    is_member = models.CharField(max_length=1, choices=MEMBER_CHOICES, default='yes', verbose_name='Are you a DC Member?')
    center = models.CharField(max_length=50, blank=True, verbose_name='If yes, which DC center do you attend?')
    church = models.CharField(max_length=50, blank=True, verbose_name='If no, what church do you attend?')
    hear = models.CharField(max_length=50, blank=True, verbose_name='How did you hear about community group?')
    is_first = models.CharField(max_length=1, choices=FIRST_TIME, default='yes', verbose_name='Is this your first time joining the community group?')
    consent = models.BooleanField(default='', verbose_name='Kindly understand that by applying to the community Group you give consent to process and store your personal information and other data you provided.The use of the data is solely for report, analysis and insights related to the Community Groups.')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
 


