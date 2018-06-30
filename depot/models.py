from django.db import models
from django.contrib.auth.models import User


class Icon(models.Model):
    #icon_id              = models.AutoField(primary_key=True)
    icon_desc            = models.CharField(primary_key=True,max_length=50)
    #container_id         = models.IntegerField(blank=True, null=True)
    #location_id          = models.IntegerField(blank=True, null=True)
    #icon_id             = models.IntegerField(blank=True, null=True)
    icon                 = models.ImageField(upload_to='images/icons/')

    def __str__(self):
        return self.icon_desc

    class Meta:
        db_table = 'samples\".\"icon'
        #ordering = ["sample_id"]
        managed = False
        verbose_name_plural = "icons"

class Storage(models.Model):
    #id = models.IntegerField(default=0)
    store_id = models.AutoField(primary_key=True)
    store_name = models.CharField(max_length=200, default='')
    address_1 = models.CharField(max_length=200, default='')
    address_2 = models.CharField(max_length=200, default='')
    region = models.CharField(max_length=200, default='')
    city = models.CharField(max_length=200, default='')
    zip = models.CharField(max_length=200, default='')
    country = models.CharField(max_length=200, default="Turkey")
    created_by = models.CharField(max_length=200)
    #created_by = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    #created_timestamp = models.DateTimeField(auto_now_add=True)
    #modified_by = models.CharField(max_length=200,editable=True)
    #modified_timestamp = models.DateTimeField(auto_now=True)
    #default="user_not_defined"
    #icon_id             = models.IntegerField(blank=True, null=True)
    icon_desc = models.ForeignKey(Icon, db_column='icon_desc', on_delete = models.PROTECT)
    orderby = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.store_name

    class Meta():
        managed=False
        db_table = 'samples\".\"store'
        ordering = ["orderby"]
        verbose_name_plural = "stores"

class Location(models.Model):
    location_id = models.AutoField(primary_key=True)
    store_id = models.ForeignKey(Storage, db_column='store_id', on_delete = models.PROTECT)
    icon_desc = models.ForeignKey(Icon, db_column='icon_desc', on_delete = models.PROTECT, null=True, blank=True)

    location_identifier = models.IntegerField(blank=True, null=True)
    #store_id = models.IntegerField(blank=True, null=True)
    location_type = models.CharField(max_length=100, blank=True, null=True)
    current_location_tmp = models.CharField(max_length=100, blank=True, null=True)
    location_name = models.CharField(max_length=100, blank=True, null=True)

     #these should become an individual table outside of the main db
    orderby = models.IntegerField(blank=True, null=True)

    #ALTER TABLE samples."location" ADD CONSTRAINT fk_location_store FOREIGN KEY ( store_id ) REFERENCES samples.store( store_id );

    def __str__(self):
        return self.location_name

    class Meta():
        managed=False
        db_table = 'samples\".\"location'
        ordering = ["orderby"]
        verbose_name_plural = "locations"

class Container(models.Model):
    location_id = models.ForeignKey(Location, db_column='location_id', on_delete = models.PROTECT)
    icon_desc = models.ForeignKey(Icon, db_column='icon_desc', on_delete = models.PROTECT)
    container_id = models.AutoField(primary_key=True)
    container_name = models.CharField(max_length=50, blank=True, null=True)
    container_type = models.CharField(max_length=50, blank=True, null=True)




    def __str__(self):
        return self.container_name

    class Meta():
        managed=False
        db_table = 'samples\".\"container'
        ordering = ["container_name"]
        verbose_name_plural = "containers"
        #unique_together = [('area_easting', 'area_northing', 'context_number', 'sample_number'),]


class JoinSampleContainer(models.Model):
    id = models.AutoField(primary_key=True)
    area_easting = models.IntegerField()
    area_northing = models.IntegerField()
    context_number = models.IntegerField()
    sample_number = models.IntegerField()
    container_id = models.ForeignKey(Container, db_column='container_id', on_delete = models.PROTECT)
    #container_id = models.IntegerField()

    def __int__(self):
        return self.container_id

    class Meta():
        managed=False
        db_table = 'samples\".\"join_sample_container'
        #ordering = ["container_id","id"]
        #verbose_name_plural = "Sample Container Join"
        #unique_together = [('area_easting', 'area_northing', 'context_number', 'sample_number'),]


class Samples(models.Model):

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
