from django.db import models
#from django.contrib.auth.models import User

# Create your models here.
class Qnisp(models.Model):
    qnisp_id = models.AutoField(primary_key=True)
    area_easting = models.IntegerField()
    area_northing = models.IntegerField()
    context_number = models.IntegerField()
    sample_number = models.IntegerField()
    collection_method = models.CharField(max_length=10, default='')
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
    comments = models.TextField(max_length=500, default='')
    ursus      = models.IntegerField(blank=True, null=True)
    big_feline_lynx_size = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.qnisp_id

    class Meta():
        managed=False
        db_table = 'samples\".\"faunal_qnisp'
        #ordering = ["orderby"]
        #verbose_name_plural = "stores"
