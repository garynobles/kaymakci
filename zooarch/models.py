from django.db import models
from django.contrib.auth.models import User

TRUE_FALSE_CHOICES = (
    (True, 'Yes'),
    (False, 'No')
)
EASTING_CHOICES = (
    ('',''),
    (99, 99),
    (108, 108),
    (109, 109)
)
NORTHING_CHOICES = (
    ('',''),
    (523, 523),
    (526, 526),

)

SELECTED_CHOICES = (
    ('',''),
    ("Hand Selected", "Hand Selected"),
    ("Floatation", "Floatation"),
    ("Preflotation","Preflotation"),
    ("Sieve","Sieve"),
)


class Zooarch(models.Model):

    #container_id = models.ForeignKey(Container, db_column='container_id', on_delete = models.PROTECT)
    #sample_id = models.AutoField(primary_key=True)

    #container_id = models.IntegerField()

    area_easting = models.IntegerField()
    area_northing = models.IntegerField()
    context_number = models.IntegerField()
    sample_number = models.AutoField(primary_key=True)

    material = models.CharField(max_length=25)
    specific_material = models.CharField(max_length=50, blank=True, null=True)
    exterior_color_hue = models.CharField(max_length=6, blank=True, null=True)
    exterior_color_lightness_value = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    exterior_color_chroma = models.IntegerField(blank=True, null=True)
    interior_color_hue = models.CharField(max_length=6, blank=True, null=True)
    interior_color_lightness_value = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    interior_color_chroma = models.IntegerField(blank=True, null=True)
    weight_kilograms = models.DecimalField(max_digits=6, decimal_places=4, blank=True, null=True)
    sample_description = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=25, blank=True, null=True)
    subcategory = models.CharField(max_length=50, blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    current_location = models.CharField(max_length=50)
    recovery_type = models.CharField(max_length=25)
    problems = models.CharField(max_length=300, blank=True, null=True)
    image_files = models.CharField(max_length=50, blank=True, null=True)
    number_3d_files = models.CharField(db_column='3d_files', max_length=50, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    chronology = models.CharField(max_length=100, blank=True, null=True)
    analysis_request = models.CharField(max_length=50, blank=True, null=True)
    detailed_sample_description = models.TextField(blank=True, null=True)
    bureaucratic_status = models.CharField(max_length=25, blank=True, null=True)
    subjective_significance = models.NullBooleanField()
    museum_inventory_number = models.IntegerField(blank=True, null=True)
    bureaucratic_status_identifier = models.CharField(max_length=100, blank=True, null=True)

    #VirtualField
    # necs = CompositeForeignKey(
    # #necs = CompositeOneToOneField(
    #     Container,
    #     on_delete=DO_NOTHING,
    #     #related_name='containers',
    #     related_name='samples',
    #     to_fields={
    #         "area_easting": "area_easting",
    #         "area_northing": "area_northing",
    #         "context_number": "context_number",
    #         "sample_number": "sample_number" })

    #sample_id = models.AutoField(unique=True)

    def __int__(self):
        return self.sample_number

    class Meta:
        db_table = 'samples\".\"samples'
        #ordering = ["sample_id"]
        managed = False
        #verbose_name_plural = "samples"
        #unique_together = (('area_easting', 'area_northing', 'context_number', 'sample_number'),)




class Qnisp(models.Model):
    qnisp_id = models.AutoField(primary_key=True)
    area_easting = models.IntegerField(choices =  EASTING_CHOICES)
    area_northing = models.IntegerField(choices =  NORTHING_CHOICES)
    context_number = models.IntegerField()
    sample_number = models.IntegerField()
    collection_method = models.CharField(max_length=25, default='', choices =  SELECTED_CHOICES)
    mandible_with_teeth  = models.BooleanField(default=False, choices =  TRUE_FALSE_CHOICES)
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
        ordering = ["-qnisp_id"]
        #verbose_name_plural = "stores"
