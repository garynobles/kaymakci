from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Botany(models.Model):
    botany_id = models.AutoField(primary_key=True)
    sample_id = models.IntegerField(blank=True, null=True)
    area_easting = models.IntegerField(blank=True, null=True)
    area_northing = models.IntegerField(blank=True, null=True)
    context_number = models.IntegerField(blank=True, null=True)
    sample_number = models.IntegerField(blank=True, null=True)
    entry_date = models.DateTimeField(auto_now_add=True)
    analysis_date = models.DateTimeField(auto_now=True)
    analyst = models.CharField(max_length=200, default='')
    notes = models.CharField(max_length=600, default='')

    def __int__(self):
        return self.botany_id

    class Meta():
        managed=False
        db_table = 'samples\".\"botany'
        #ordering = ["orderby"]
        verbose_name_plural = "botany"


class Fraction(models.Model):
    fraction_id = models.AutoField(primary_key=True)
    botany_id = models.ForeignKey(Botany, db_column='botany_id', on_delete = models.PROTECT)
    proportion_analysed = models.DecimalField(max_digits=5, decimal_places=3)
    soil_volume = models.DecimalField(max_digits=15, decimal_places=4)
    sample_volume = models.DecimalField(max_digits=15, decimal_places=4)
    sample_weight = models.DecimalField(max_digits=15, decimal_places=4)


    def __int__(self):
        return self.fraction_id

    class Meta():
        managed=False
        db_table = 'samples\".\"fraction'
        #ordering = ["orderby"]
        #verbose_name_plural = "stores"

class FractionComposition(models.Model):

    fract_comp_id = models.AutoField(primary_key=True)
    fraction_id = models.ForeignKey(Fraction, db_column='fraction_id', on_delete = models.PROTECT)
    material_type = models.CharField(max_length=50, default='')
    fraction = models.CharField(max_length=50, default='')
    type_count = models.DecimalField(max_digits=15, decimal_places=4)
    whole_weight = models.DecimalField(max_digits=15, decimal_places=4)
    fragment_weight = models.DecimalField(max_digits=15, decimal_places=4)

    def __int__(self):
        return self.fract_comp_id

    class Meta():
        managed=False
        db_table = 'samples\".\"fraction_composition'
        #ordering = ["orderby"]
        #verbose_name_plural = "stores"

class FractionMaterialsPresent(models.Model):

    material_id = models.AutoField(primary_key=True)
    fraction_id = models.ForeignKey(Fraction, db_column='fraction_id', on_delete = models.PROTECT)
    material = models.CharField(max_length=200, default='')

    def __int__(self):
        return self.material_id

    class Meta():
        managed=False
        db_table = 'samples\".\"materials_present'
        #ordering = ["orderby"]
        #verbose_name_plural = "stores"
