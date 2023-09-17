from django.db import models
from polling_units.models import (
    LGA,
    PollingUnit
)

class AnnouncedLGAResult(models.Model):
    lga_name = models.ForeignKey(LGA, on_delete=models.RESTRICT)
    party_abbreviation = models.CharField(max_length=4)
    party_score = models.PositiveBigIntegerField()
    user_ip_address = models.CharField(max_length=50)
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField(auto_now_add=True)
 
    class Meta:
        verbose_name = "Announced LGA Result"
        verbose_name_plural = "Announced LGA Results"

    def lga(self):
        lga_name = LGA.objects.filter(lga_id=self.lga_name.lga_id)
        return lga_name[0].lga_name
    lga.short_description = "LGA"


class AnnouncedPUResult(models.Model):
    polling_unit_uniqueid = models.ForeignKey(LGA, on_delete=models.RESTRICT)
    party_abbreviation = models.CharField(max_length=4)
    user_ip_address = models.CharField(max_length=50)
    party_score = models.PositiveBigIntegerField()
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Announced Pollin-units Result"
        verbose_name_plural = "Announced Pollin-units Results"

    def lga(self):
        polling_unit = PollingUnit.objects.filter(lga_id=self.polling_unit_uniqueid.lga_id)
        return polling_unit[0].polling_unit_name
    lga.short_description = "Polling unit"

class AnnouncedWardResult(models.Model):
    ward_name = models.ForeignKey(LGA, on_delete=models.RESTRICT)
    party_abbreviation = models.CharField(max_length=4)
    user_ip_address = models.CharField(max_length=50)
    party_score = models.PositiveBigIntegerField()
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Announced Ward Result"
        verbose_name_plural = "Announced Ward Results"

class AnnouncedStateResult(models.Model):
    state = models.ForeignKey(LGA, on_delete=models.RESTRICT)
    party_abbreviation = models.CharField(max_length=4)
    user_ip_address = models.CharField(max_length=50)
    party_score = models.PositiveBigIntegerField()
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Announced State Result"
        verbose_name_plural = "Announced State Results"