from django.db import models
# from agents.models import Agents

class State(models.Model):
    state_id = models.PositiveIntegerField()
    state_name = models.CharField(max_length=30)

class Party(models.Model):
    party_name = models.CharField(max_length=10)
    party_id = models.CharField(max_length=7, help_text="This field is automatically populated. But you can input your preferred value, if need be.")

    def __str__(self) -> str:
        return f"{self.party_name} - {self.party_id}"

    class Meta:
        verbose_name = "Party"
        verbose_name_plural = "Parties"


class LGA(models.Model):
    lga_name = models.CharField(max_length=30)
    lga_id = models.CharField(max_length=70, help_text="This field is automatically populated. But you can input your preferred value, if need be.")
    state_id = models.ForeignKey(State, related_name="state", verbose_name="State-Id", on_delete=models.CASCADE)
    lga_description = models.CharField(max_length=200)
    entered_by_user = models.CharField(max_length=70)
    date_entered = models.DateTimeField(auto_now_add=True)
    user_ip_address = models.CharField(max_length=50)

    # def user_ip_address(self):
    class Meta:
        verbose_name = "LGA"
        verbose_name_plural = "LGA's"

    def state(self):
        state_name = State.objects.get(state_id=self.state_id.state_id)
        return state_name.state_name
    state.short_description = "State"


class Ward(models.Model):
    ward_name = models.CharField(max_length=20)
    ward_id = models.CharField(max_length=10, help_text="This field is automatically populated. But you can input your preferred value, if need be.")
    lga_id= models.ForeignKey(LGA, on_delete=models.CASCADE, help_text="If you can't find the LGA, then add it, using the green plus button")
    ward_description = models.CharField(max_length=200)
    entered_by_user = models.CharField(max_length=70)
    date_entered = models.DateTimeField(auto_now_add=True, auto_now=False)
    user_ip_address = models.CharField(max_length=50)

    def lga(self):
        lga_name = LGA.objects.get(lga_id=self.lga_id.lga_id)
        return lga_name.lga_name
    lga.short_description = "LGA"


class PollingUnit(models.Model):
    polling_unit_name = models.CharField(max_length=70, null=True)
    polling_unit_id = models.PositiveIntegerField(null=False)
    polling_unit_number = models.CharField(max_length=15)
    polling_unit_description = models.CharField(max_length=200, null=True)
    ward_id = models.ForeignKey(Ward, on_delete=models.CASCADE, verbose_name="Ward-Id", help_text="If you can't find the Ward, then add it, using the green plus button")
    lga_id = models.ForeignKey(LGA, on_delete=models.CASCADE, verbose_name="LGA-Id", help_text="If you can't find the LGA, then add it, using the green plus button")
    lattitude = models.CharField(max_length=70, null=True)
    longitude = models.CharField(max_length=70, null=True)
    entered_by_user = models.CharField(max_length=70)

    date_entered = models.DateTimeField(auto_now_add=True)
    user_ip_address = models.CharField(max_length=70, verbose_name="User's IP-address", null=True)
    def lga(self):
        lga_name = LGA.objects.get(lga_id=self.lga_id.lga_id)
        return lga_name.lga_name
    lga.short_description = "LGA"

    def ward(self):
        ward = Ward.objects.filter(ward_id=self.ward_id.ward_id)
        return ward[0].ward_name
    ward.short_description = "Ward"
    class Meta:
        verbose_name = "Polling unit"
        verbose_name_plural = "Polling units"

    def __str__(self):
        return self.polling_unit_name