from django.db import models
#from django.contrib.auth.models import User

# Create your models here.

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

SELECTED_CHOICES = (
    ("Hand Selected", "Hand Selected"),
    ("Floatation", "Floatation"),
    ("Preflotation","Preflotation"),
    ("Sieve","Sieve"),
)



class Qnisp(models.Model):
    qnisp_id = models.AutoField(primary_key=True)
    area_easting = models.IntegerField(choices =  EASTING_CHOICES)
    area_northing = models.IntegerField(choices =  NORTHING_CHOICES)
    context_number = models.IntegerField()
    sample_number = models.IntegerField()
    collection_method = models.CharField(max_length=25, default='', choices =  SELECTED_CHOICES)
    mandible_with_teeth  = models.BooleanField(default=False)
    bt         = models.IntegerField(blank=True, null=True)
    ss         = models.IntegerField(blank=True, null=True)
    oc_tje     = models.IntegerField(blank=True, null=True)
    ch         = models.IntegerField(blank=True, null=True)
    oa         = models.IntegerField(blank=True, null=True)
    equid      = models.IntegerField(blank=True, null=True)
    cer        = models.IntegerField(blank=True, null=True)
    lp         = models.IntegerField(blank=True, null=True)
    meles      = models.IntegerField(blank=True, null=True)
    pesc       = models.IntegerField(blank=True, null=True)
    brd        = models.IntegerField(blank=True, null=True)
    canis      = models.IntegerField(blank=True, null=True)
    unio       = models.IntegerField(blank=True, null=True)
    cerastoderma   = models.IntegerField(blank=True, null=True)
    landsnail  = models.IntegerField(blank=True, null=True)
    shell_other    = models.IntegerField(blank=True, null=True)
    rodent     = models.IntegerField(blank=True, null=True)
    comments = models.TextField(max_length=500, default='', blank=True, null=True)
    ursus      = models.IntegerField(blank=True, null=True)
    big_feline_lynx_size = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.qnisp_id

    class Meta():
        managed=False
        db_table = 'samples\".\"faunal_qnisp'
        #ordering = ["orderby"]
        #verbose_name_plural = "stores"
