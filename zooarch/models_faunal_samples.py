from django.db import models
from django.contrib.auth.models import User

TRUE_FALSE_CHOICES = (
    (True, 'Yes'),
    (False, 'No')
)
EASTING_CHOICES = (
    (99, 99),
    (108, 108),
    (109, 109)
)
NORTHING_CHOICES = (
    (523, 523),
    (526, 526),
)
ELEMENT_CHOICES = (
(1,2),
)
PORTION_CHOICES = (
(1,2),
)
SIDE_CHOICES = (
(1,2),
)
SEX_CHOICES = (
(1,2),
)
TAX_CHOICES = (
(1,2),
)
FUSION_CHOICES = (
(1,2),
)
AGE_CHOICES = (
(1,2),
)
TOOTH_WEAR_CHOICES = (
(1,2),
)
STATUS_CHOICES = (
(1,2),
)

class Zooarch(models.Model):
    area_easting = models.IntegerField()
    area_northing = models.IntegerField()
    context_number = models.IntegerField()
    sample_number = models.IntegerField()
    element = models.CharField(max_length=100, default='', blank=False, null=False, choices =  ELEMENT_CHOICES)
    portion = models.CharField(max_length=100, default='', blank=False, null=False, choices =  PORTION_CHOICES)
    side = models.CharField(max_length=25, default='', blank=False, null=False, choices =  SIDE_CHOICES)
    sex = models.CharField(max_length=25, default='', blank=False, null=False, choices =  SEX_CHOICES)
    taxonomic_description = models.CharField(max_length=100, default='', blank=False, null=False, choices =  TAX_CHOICES)
    fusion = models.CharField(max_length=50, default='', blank=False, null=False, choices =  FUSION_CHOICES)

    age_estimation = models.CharField(max_length=50, default='', blank=True, null=True, choices =  AGE_CHOICES)
    tooth_wear = models.CharField(max_length=25, default='', blank=True, null=True, choices =  TOOTH_WEAR_CHOICES)
    status = models.CharField(max_length=30, default='', blank=True, null=True, choices =  STATUS_CHOICES)

    # def __str__(self):
    #     return self.qnisp_id

    class Meta():
        managed=False
        db_table = 'samples\".\"faunal_samples'
        #ordering = ["orderby"]
        #verbose_name_plural = "stores"
