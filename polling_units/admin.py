from collections.abc import Sequence
from django.contrib import admin
from django.contrib.auth.models import Group
from django.http.request import HttpRequest
# from pre_data import data
from .models import (
    State,
    Ward,
    LGA,
    PollingUnit,
    Party
)
class PartyAdmin(admin.ModelAdmin):
    list_display = ["party_id", "party_name"]
    ordering = ['party_id']
    
    def get_list_display(self, request: HttpRequest) -> Sequence[str]:
        default_data = DefaultData()
        default_data.run_parties()
        return super().get_list_display(request)
admin.site.register(Party, PartyAdmin)


class StateAdmin(admin.ModelAdmin):
    list_display = ["state_id", "state_name"]
    ordering = ['state_id']
    
    def get_list_display(self, request: HttpRequest) -> Sequence[str]:
        default_data = DefaultData()
        default_data.run_states()
        return super().get_list_display(request)
admin.site.register(State, StateAdmin)


class LGAAdmin(admin.ModelAdmin):
    list_display = ["lga_id", "lga_name", "state", "lga_description", "entered_by_user", "user_ip_address", "date_entered"]
    ordering = ['lga_id']
 
    def get_list_display(self, request: HttpRequest) -> Sequence[str]:
        default_data = DefaultData()
        default_data.run_lgas()
        return super().get_list_display(request)
admin.site.register(LGA, LGAAdmin)



class WardAdmin(admin.ModelAdmin):
    list_display = ["ward_name", "ward_id", "lga", "ward_description", "entered_by_user"]
    ordering = ['ward_id']
 
    def get_list_display(self, request: HttpRequest) -> Sequence[str]:
        default_data = DefaultData()
        default_data.run_wards()
        return super().get_list_display(request)
admin.site.register(Ward, WardAdmin)

class PollingUnitAdmin(admin.ModelAdmin):
    list_display = ["polling_unit_name", "polling_unit_id", "lga", "ward", "polling_unit_description", "entered_by_user"]
    ordering = ['polling_unit_id']
 
    def get_list_display(self, request: HttpRequest) -> Sequence[str]:
        default_data = DefaultData()
        default_data.run_polling_unit()
        return super().get_list_display(request)
admin.site.register(PollingUnit, PollingUnitAdmin)



class DefaultData:
    def run_polling_unit(self) -> Sequence[str]:
        for polling_unit in PollingUnits:
            polling_unit_exists = PollingUnit.objects.filter(polling_unit_name=polling_unit[6])
            if not polling_unit_exists:
                new_polling_unit = PollingUnit()
                lga = LGA.objects.filter(lga_id=polling_unit[3])
                ward = Ward.objects.filter(lga_id=polling_unit[3])
                if lga and ward:
                    new_polling_unit.ward_id = ward[0]
                    new_polling_unit.lga_id = lga[0]
                    new_polling_unit.polling_unit_id = polling_unit[1]
                    new_polling_unit.polling_unit_number = polling_unit[5]
                    new_polling_unit.polling_unit_name = polling_unit[6]
                    new_polling_unit.polling_unit_description = polling_unit[7]
                    new_polling_unit.lattitude = polling_unit[8]
                    new_polling_unit.longitude = polling_unit[9]
                    new_polling_unit.entered_by_user = polling_unit[10]
                    new_polling_unit.user_ip_address = polling_unit[12]
                    new_polling_unit.save()

    def run_wards(self) -> Sequence[str]:
        for ward in WARDS:
            ward_exists = Ward.objects.filter(ward_name=ward[2])
            if not ward_exists:
                new_ward = Ward()
                lga = LGA.objects.filter(lga_id=ward[3])
                if lga:
                    new_ward.ward_id = int(ward[1])
                    new_ward.ward_name = ward[2]
                    new_ward.ward_description = ward[4]
                    new_ward.entered_by_user = ward[5]
                    new_ward.user_ip_address = ward[7]
                    new_ward.lga_id = lga[0]
                    new_ward.save()

    def run_lgas(self) -> Sequence[str]:
        for lga in LGAS:
            lga_exists = LGA.objects.filter(lga_name=lga[2])
            if not lga_exists:
                new_lga = LGA()
                state = State.objects.filter(state_id=lga[3])
                if state:
                    new_lga.lga_id = int(lga[1])
                    new_lga.lga_name = lga[2]
                    new_lga.lga_description = lga[4]
                    new_lga.entered_by_user = lga[5]
                    new_lga.user_ip_address = lga[7]
                    new_lga.state_id = state[0]
                    new_lga.save()

    def run_states(self) -> Sequence[str]:
        for state in STATES:
            state_exists = State.objects.filter(state_name=state[1])
            if not state_exists:
                new_state = State()
                new_state.state_id = int(state[0])
                new_state.state_name = state[1]
                new_state.save()

    def run_parties(self) -> Sequence[str]:
        for party in PARTIES:
            party_exists = Party.objects.filter(party_name=party[2])
            if not party_exists:
                new_party = Party()
                new_party.party_id = party[1]
                new_party.party_name = party[2]
                new_party.save()


PARTIES = [
    (1, 'PDP', 'PDP'),
(2, 'DPP', 'DPP'),
(3, 'ACN', 'ACN'),
(4, 'PPA', 'PPA'),
(5, 'CDC', 'CDC'),
(6, 'JP', 'JP'),
(7, 'ANPP', 'ANPP'),
(8, 'LABOUR', 'LABOUR'),
(9, 'CPP', 'CPP')
]
STATES = [
        ("1", 'Abuja'),
        ("2" , 'Abia'),
        ("3", 'Anambra'),
        ("4", 'Akwa Ibom'),
        ("5", 'Adamawa'),
        ("6", 'Bauchi'),
        ("7", 'Bayelsa'),
        ("8", 'Benue'),
        ("9", 'Borno'),
        ("10", 'Cross River'),
        ("12", 'Ebonyi'),
        ("13", 'Edo'),
        ("14", 'Ekiti'),
        ("15", 'Enugu'),
        ("16", 'Gombe'),
        ("17", 'Imo'),
        ("18", 'Jigawa'),
        ("19", 'Kaduna'),
        ("20", 'Kano'),
        ("21", 'Katsina'),
        ("22", 'Kebbi'),
        ("23", 'Kogi'),
        ("24", 'Kwara'),
        ("25", 'Delta'),
        ("26", 'Nasarawa'),
        ("27", 'Niger'),
        ("28", 'Ogun'),
        ("29", 'Ondo'),
        ("30", 'Osun'),
        ("31", 'Oyo'),
        ("32", 'Plateau'),
        ("33", 'Rivers'),
        ("34", 'Sokoto'),
        ("35", 'Taraba'),
        ("36", 'Yobe'),
        ("37", 'Zamfara'),
        ("251", 'Lagos')
    ]

LGAS = [
    (1, 1, 'Aniocha North', 25, 'Aniocha North', 'Bincom', '0000-00-00 00:00:00', '127.0.0.2'),
(2, 2, 'Aniocha - South', 25, 'Aniocha - South', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(3, 5, 'Ethiope East', 25, 'Ethiope East', 'Bincom', '0000-00-00 00:00:00', '127.0.0.5'),
(4, 6, 'Ethiope West', 25, 'Ethiope West', 'Bincom', '0000-00-00 00:00:00', '127.0.0.6'),
(5, 7, 'Ika North - East', 25, 'Ika North - East', 'Bincom', '0000-00-00 00:00:00', '127.0.0.8'),
(6, 8, 'Ika - South', 25, 'Ika - South', 'Bincom', '0000-00-00 00:00:00', '127.0.0.7'),
(7, 9, 'Isoko North', 25, 'Isoko North', 'Bincom', '0000-00-00 00:00:00', '127.0.0.9'),
(8, 10, 'Isoko South', 25, 'Isoko South', 'Bincom', '0000-00-00 00:00:00', '127.0.0.10'),
(9, 11, 'Ndokwa East', 25, 'Ndokwa East', 'Bincom', '0000-00-00 00:00:00', '127.0.0.11'),
(10, 12, 'Ndokwa West', 25, 'Ndokwa West', 'Bincom', '0000-00-00 00:00:00', '127.0.0.12'),
(11, 13, 'Okpe', 25, 'Okpe', 'Bincom', '0000-00-00 00:00:00', '127.0.0.13'),
(12, 14, 'Oshimili - North', 25, 'Oshimili - North', 'Bincom', '0000-00-00 00:00:00', '127.0.0.14'),
(13, 15, 'Oshimili - South', 25, 'Oshimili - South', 'Bincom', '0000-00-00 00:00:00', '127.0.0.15'),
(14, 16, 'Patani', 25, 'Patani', 'Bincom', '0000-00-00 00:00:00', '127.0.0.16'),
(15, 17, 'Sapele', 25, 'Sapele', 'Bincom', '0000-00-00 00:00:00', '127.0.0.17'),
(16, 18, 'Udu', 25, 'Udu', 'Bincom', '0000-00-00 00:00:00', '127.0.0.18'),
(17, 19, 'Ughelli North', 25, 'Ughelli North', 'Bincom', '0000-00-00 00:00:00', '127.0.0.19'),
(18, 20, 'Ughelli South', 25, 'Ughelli South', 'Bincom', '0000-00-00 00:00:00', '127.0.0.20'),
(19, 21, 'Ukwuani', 25, 'Ukwuani', 'Bincom', '0000-00-00 00:00:00', '127.0.0.21'),
(20, 22, 'Uvwie', 25, 'Uvwie', 'Bincom', '0000-00-00 00:00:00', '127.0.0.22'),
(21, 31, 'Bomadi', 25, 'Bomadi', 'Bincom', '0000-00-00 00:00:00', '127.0.0.3'),
(22, 32, 'Burutu', 25, 'Burutu', 'Bincom', '0000-00-00 00:00:00', '127.0.0.4'),
(23, 33, 'Warri North', 25, 'Warri North', 'Bincom', '0000-00-00 00:00:00', '127.0.0.23'),
(24, 34, 'Warri South', 25, 'Warri South', 'Bincom', '0000-00-00 00:00:00', '127.0.0.24'),
(25, 35, 'Warri South West', 25, 'Warri South West', 'Bincom', '0000-00-00 00:00:00', '127.0.0.25')

]

WARDS = [
    (1, 2, 'Aba - Unor', 2, 'Aba - Unor', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(2, 8, 'Ejeme', 2, 'Ejeme', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(3, 9, 'Isheagu - Ewulu', 2, 'Isheagu - Ewulu', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(4, 7, 'Nsukwa', 2, 'Nsukwa', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(5, 2, 'Ogwashi - Uku I', 2, 'Ogwashi - Uku I', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(6, 3, 'Ogwashi - Uku Ii', 2, 'Ogwashi - Uku Ii', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(7, 1, 'Ogwashi - Uku Village', 2, 'Ogwashi - Uku Village', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(8, 4, 'Ubulu - Uku I', 2, 'Ubulu - Uku I', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(9, 5, 'Ubulu - Uku Ii', 2, 'Ubulu - Uku Ii', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(10, 6, 'Ubulu - Unor', 2, 'Ubulu - Unor', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(11, 11, 'Ubulu Okiti', 2, 'Ubulu Okiti', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(12, 10, 'Ezi', 1, 'Ezi', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(13, 8, 'Idumuje - Unor', 1, 'Idumuje - Unor', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(14, 5, 'Issele - Azagba', 1, 'Issele - Azagba', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(15, 6, 'Issele Uku I', 1, 'Issele Uku I', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(16, 7, 'Issele Uku Ii', 1, 'Issele Uku Ii', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(17, 1, 'Obior', 1, 'Obior', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(18, 3, 'Obomkpa', 1, 'Obomkpa', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(19, 4, 'Onicha - Olona', 1, 'Onicha - Olona', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(20, 2, 'Onicha Ugbo', 1, 'Onicha Ugbo', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(21, 9, 'Ukwu - Nzu', 1, 'Ukwu - Nzu', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(22, 0, 'Akugbene', 31, 'Akugbene', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(23, 0, 'Akugbene Ii', 31, 'Akugbene', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(24, 0, 'Akugbene Iii', 31, 'Akugbene', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(25, 0, 'Bomadi', 31, 'Akugbene', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(26, 0, 'Kolafiogbene / Ekametagbene', 31, 'Akugbene', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(27, 0, 'Kpakiama', 31, 'Akugbene', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(28, 0, 'Ogbeinama / Okoloba', 31, 'Akugbene', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(29, 0, 'Ogo - Eze', 31, 'Akugbene', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(30, 0, 'Ogriagene', 31, 'Akugbene', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(31, 0, 'Syama', 31, 'Akugbene', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(32, 0, 'Bolou - Ndoro', 32, 'Akugbene', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(33, 0, 'Ngbilebiri', 32, 'Akugbene', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(34, 0, 'Ngbilebiri Ii', 32, 'Akugbene', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(35, 0, 'Obotebe', 32, 'Akugbene', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(36, 0, 'Ogbolubiri', 32, 'Akugbene', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(37, 0, 'Ogulagha', 32, 'Akugbene', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(38, 0, 'Seimbiri', 32, 'Akugbene', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(39, 0, 'Tamigbe', 32, 'Akugbene', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(40, 0, 'Torugbene', 32, 'Akugbene', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(41, 0, 'Tuomo', 32, 'Akugbene', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(42, 1, 'Abraka I', 5, 'Abraka I', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(43, 2, 'Abraka Ii', 5, 'Abraka Ii', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(44, 3, 'Abraka Iii', 5, 'Abraka Iii', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(45, 4, 'Agbon I', 5, 'Agbon I', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(46, 5, 'Agbon Ii', 5, 'Agbon Ii', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(47, 6, 'Agbon Iii', 5, 'Agbon Iii', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(48, 7, 'Agbon Iv', 5, 'Agbon Iv', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(49, 8, 'Agbon V', 5, 'Agbon V', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(50, 9, 'Agbon Vi', 5, 'Agbon Vi', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(51, 10, 'Agbon Vii', 5, 'Agbon Vii', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(52, 11, 'Agbon Viii', 5, 'Agbon Viii', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(53, 3, 'Jesse I', 6, 'Jesse I', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(54, 4, 'Jesse Ii', 6, 'Jesse Ii', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(55, 5, 'Jesse Iii', 6, 'Jesse Iii', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(56, 6, 'Jesse Iv', 6, 'Jesse Iv', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(57, 1, 'Mosogar I', 6, 'Mosogar I', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(58, 2, 'Mosogar Ii', 6, 'Mosogar Ii', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(59, 7, 'Oghara I', 6, 'Oghara I', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(60, 8, 'Oghara Ii', 6, 'Oghara Ii', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(61, 9, 'Oghara Iii', 6, 'Oghara Iii', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(62, 10, 'Oghara Iv', 6, 'Oghara Iv', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(63, 11, 'Oghara V', 6, 'Oghara V', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(64, 10, 'Abavo I', 8, 'Abavo I', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(65, 11, 'Abavo Ii', 8, 'Abavo Ii', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(66, 12, 'Abavo Iii', 8, 'Abavo Iii', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(67, 1, 'Agbor Town I', 8, 'Agbor Town I', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(68, 2, 'Agbor Town Ii', 8, 'Agbor Town Ii', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(69, 7, 'Boji - Boji I', 8, 'Boji - Boji I', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(70, 8, 'Boji - Boji Ii', 8, 'Boji - Boji Ii', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(71, 9, 'Boji - Boji Iii', 8, 'Boji - Boji Iii', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(72, 5, 'Ekuku - Agbor', 8, 'Ekuku - Agbor', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(73, 4, 'Ihiuiyase I', 8, 'Ihiuiyase I', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(74, 6, 'Ihuiyase Ii', 8, 'Ihuiyase Ii', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(75, 3, 'Ihuozomor ( Ozanogogo Alisimie )', 8, 'Ihuozomor ( Ozanogogo Alisimie )', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(76, 7, 'Akumazi', 7, 'Akumazi', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(77, 10, 'Idumuesah', 7, 'Idumuesah', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(78, 8, 'Igbodo', 7, 'Igbodo', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(79, 12, 'Mbiri', 7, 'Mbiri', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(80, 14, 'Otolokpo', 7, 'Otolokpo', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(81, 5, 'Owa V', 7, 'Owa V', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(82, 6, 'Owa Vi', 7, 'Owa Vi', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(83, 1, 'Owa I', 7, 'Owa I', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(84, 2, 'Owa Ii', 7, 'Owa Ii', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(85, 3, 'Owa Iii', 7, 'Owa Iii', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(86, 4, 'Owa Iv', 7, 'Owa Iv', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(87, 11, 'Umunede', 7, 'Umunede', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(88, 13, 'Ute - Ogbeje', 7, 'Ute - Ogbeje', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(89, 9, 'Ute - Okpu', 7, 'Ute - Okpu', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(90, 3, 'Ellu', 9, 'Ellu', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(91, 4, 'Emevor', 9, 'Emevor', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(92, 5, 'Iluelogbo', 9, 'Iluelogbo', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(93, 1, 'Iyede I', 9, 'Iyede I', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(94, 2, 'Iyede Ii', 9, 'Iyede Ii', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(95, 8, 'Okpe - Isoko', 9, 'Okpe - Isoko', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(96, 13, 'Otibio', 9, 'Otibio', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(97, 7, 'Ovrode', 9, 'Ovrode', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(98, 6, 'Owhe / Akiehwe', 9, 'Owhe / Akiehwe', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(99, 12, 'Oyede', 9, 'Oyede', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(100, 9, 'Ozoro I', 9, 'Ozoro I', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(101, 10, 'Ozoro Ii', 9, 'Ozoro Ii', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(102, 11, 'Ozoro Iii', 9, 'Ozoro Iii', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(103, 3, 'Aviara', 10, 'Aviara', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(104, 5, 'Emede', 10, 'Emede', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(105, 9, 'Enhwe / Okpolo', 10, 'Enhwe / Okpolo', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(106, 8, 'Erowa / Umeh', 10, 'Erowa / Umeh', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(107, 7, 'Igbide', 10, 'Igbide', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(108, 11, 'Irri Ii', 10, 'Irri Ii', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(109, 10, 'Irri I', 10, 'Irri I', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(110, 1, 'Oleh I', 10, 'Oleh I', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(111, 2, 'Oleh Ii', 10, 'Oleh Ii', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(112, 6, 'Olomoro', 10, 'Olomoro', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(113, 4, 'Uzere', 10, 'Uzere', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(114, 3, 'Abarra / Inyi / Onuaboh', 11, 'Abarra / Inyi / Onuaboh', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(115, 5, 'Aboh / Akarrai', 11, 'Aboh / Akarrai', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(116, 2, 'Afor / Obikwele', 11, 'Afor / Obikwele', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(117, 7, 'Ase', 11, 'Ase', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(118, 10, 'Ashaka', 11, 'Ashaka', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(119, 8, 'Ibedeni', 11, 'Ibedeni', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(120, 9, 'Ibrede / Igbuku / Onogbokor', 11, 'Ibrede / Igbuku / Onogbokor', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(121, 4, 'Okpai / Utchi / Beneku', 11, 'Okpai / Utchi / Beneku', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(122, 6, 'Onyia / Adiai / Otuoku / Umuolu', 11, 'Onyia / Adiai / Otuoku / Umuolu', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(123, 1, 'Ossissa', 11, 'Ossissa', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(124, 9, 'Abbi Ii', 12, 'Abbi Ii', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(125, 8, 'Abbi I', 12, 'Abbi I', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(126, 10, 'Emu', 12, 'Emu', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(127, 6, 'Ogume I', 12, 'Ogume I', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(128, 7, 'Ogume Ii', 12, 'Ogume Ii', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(129, 5, 'Onicha - Ukwani', 12, 'Onicha - Ukwani', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(130, 1, 'Utagba Ogbe', 12, 'Utagba Ogbe', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(131, 2, 'Utagba Uno I', 12, 'Utagba Uno I', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(132, 3, 'Utagba Uno Ii', 12, 'Utagba Uno Ii', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(133, 4, 'Utagba Uno Iii', 12, 'Utagba Uno Iii', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(134, 5, 'Aghalokpe', 13, 'Aghalokpe', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(135, 6, 'Aragba Town', 13, 'Aragba Town', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(136, 7, 'Mereje I', 13, 'Mereje I', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(137, 8, 'Mereje Ii', 13, 'Mereje Ii', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(138, 9, 'Mereje Iii', 13, 'Mereje Iii', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(139, 3, 'Oha I', 13, 'Oha I', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(140, 4, 'Oha Ii', 13, 'Oha Ii', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(141, 1, 'Orerokpe', 13, 'Orerokpe', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(142, 2, 'Oviri - Okpe', 13, 'Oviri - Okpe', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(143, 10, 'Ughoton', 13, 'Ughoton', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(144, 1, 'Akwukwu', 14, 'Akwukwu', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(145, 2, 'Ebu', 14, 'Ebu', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(146, 4, 'Ibusa I', 14, 'Ibusa I', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(147, 5, 'Ibusa Ii', 14, 'Ibusa Ii', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(148, 6, 'Ibusa Iii', 14, 'Ibusa Iii', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(149, 7, 'Ibusa Iv', 14, 'Ibusa Iv', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(150, 8, 'Ibusa V', 14, 'Ibusa V', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(151, 3, 'Illah', 14, 'Illah', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(152, 9, 'Okpanam', 14, 'Okpanam', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(153, 10, 'Ukala', 14, 'Ukala', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(154, 7, 'Agu', 15, 'Agu', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(155, 2, 'Anala - Amakom', 15, 'Anala - Amakom', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(156, 10, 'Cable Point I', 15, 'Cable Point I', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(157, 11, 'Cable Point Ii', 15, 'Cable Point Ii', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(158, 1, 'Ogbele / Akpako', 15, 'Ogbele / Akpako', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(159, 3, 'Okwe', 15, 'Okwe', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(160, 7, 'Ugbomanta Quarters', 15, 'Ugbomanta Quarters', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(161, 5, 'Umuaji', 15, 'Umuaji', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(162, 4, 'Umuezei', 15, 'Umuezei', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(163, 6, 'Umuonaje', 15, 'Umuonaje', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(164, 9, 'West End', 15, 'West End', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(165, 1, 'Abari', 16, 'Abari', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(166, 4, 'Agoloma', 16, 'Agoloma', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(167, 8, 'Bolou - Angiama', 16, 'Bolou - Angiama', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(168, 10, 'Odorubu / Adobu / Bolou Apelebri', 16, 'Odorubu / Adobu / Bolou Apelebri', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(169, 5, 'Patani Ii', 16, 'Patani Ii', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(170, 6, 'Patani Iii', 16, 'Patani Iii', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(171, 2, 'Patani I', 16, 'Patani I', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(172, 3, 'Taware / Kolowara Aven', 16, 'Taware / Kolowara Aven', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(173, 7, 'Toru - Angiama', 16, 'Toru - Angiama', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(174, 9, 'Uduophori', 16, 'Uduophori', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(175, 9, 'Amuokpe', 17, 'Amuokpe', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(176, 3, 'Sapele Urban Iii', 17, 'Sapele Urban Iii', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(177, 4, 'Sapele Urban Iv', 17, 'Sapele Urban Iv', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(178, 5, 'Sapele Urban V', 17, 'Sapele Urban V', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(179, 6, 'Sapele Urban Vi', 17, 'Sapele Urban Vi', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(180, 7, 'Sapele Urban Vii', 17, 'Sapele Urban Vii', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(181, 8, 'Sapele Urban Viii', 17, 'Sapele Urban Viii', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(182, 1, 'Sapele Urban I', 17, 'Sapele Urban I', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(183, 2, 'Sapele Urban Ii', 17, 'Sapele Urban Ii', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(184, 10, 'Aladja', 18, 'Aladja', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(185, 6, 'Ekete', 18, 'Ekete', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(186, 5, 'Opete / Assagba / Edjophe', 18, 'Opete / Assagba / Edjophe', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(187, 9, 'Orhuwerun', 18, 'Orhuwerun', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(188, 7, 'Ovwian I', 18, 'Ovwian I', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(189, 8, 'Ovwian Ii', 18, 'Ovwian Ii', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(190, 1, 'Udu I', 18, 'Udu I', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(191, 2, 'Udu Ii', 18, 'Udu Ii', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(192, 3, 'Udu Iii', 18, 'Udu Iii', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(193, 4, 'Udu Iv', 18, 'Udu Iv', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(194, 1, 'Agbarha', 19, 'Agbarha', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(195, 10, 'Agbarho I', 19, 'Agbarho I', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(196, 11, 'Agbarho Ii', 19, 'Agbarho Ii', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(197, 8, 'Evwreni', 19, 'Evwreni', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(198, 2, 'Ogor', 19, 'Ogor', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(199, 3, 'Orogun I', 19, 'Orogun I', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(200, 4, 'Orogun Ii', 19, 'Orogun Ii', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(201, 5, 'Ughelli I', 19, 'Ughelli I', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(202, 6, 'Ughelli Ii', 19, 'Ughelli Ii', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(203, 7, 'Ughelli Iii', 19, 'Ughelli Iii', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(204, 9, 'Uwheru', 19, 'Uwheru', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(205, 6, 'Effurun - Otor', 20, 'Effurun - Otor', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(206, 7, 'Ekakpamre', 20, 'Ekakpamre', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(207, 8, 'Jeremi I', 20, 'Jeremi I', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(208, 9, 'Jeremi Ii', 20, 'Jeremi Ii', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(209, 10, 'Jeremi Iii', 20, 'Jeremi Iii', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(210, 4, 'Olomu I', 20, 'Olomu I', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(211, 5, 'Olomu Ii', 20, 'Olomu Ii', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(212, 2, 'Akoku', 21, 'Akoku', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(213, 6, 'Amai', 21, 'Amai', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(214, 3, 'Ebedei', 21, 'Ebedei', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(215, 5, 'Eziokpor', 21, 'Eziokpor', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(216, 6, 'Ezionum', 21, 'Ezionum', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(217, 9, 'Obiaruku I', 21, 'Obiaruku I', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(218, 10, 'Obiaruku Ii', 21, 'Obiaruku Ii', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(219, 8, 'Umuebu', 21, 'Umuebu', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(220, 4, 'Umukwata', 21, 'Umukwata', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(221, 1, 'Umutu', 21, 'Umutu', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(222, 8, 'Army Barracks Area', 22, 'Army Barracks Area', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(223, 1, 'Effurun I', 22, 'Effurun I', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(224, 2, 'Effurun Ii', 22, 'Effurun Ii', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(225, 9, 'Ekpan I', 22, 'Ekpan I', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(226, 12, 'Ekpan Ii', 22, 'Ekpan Ii', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(227, 3, 'Enerhen I', 22, 'Enerhen I', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(228, 4, 'Enerhen Ii', 22, 'Enerhen Ii', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(229, 7, 'Ugbomro / Ugbolokposo', 22, 'Ugbomro / Ugbolokposo', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(230, 5, 'Ugborikoko', 22, 'Ugborikoko', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(231, 6, 'Ugboroke', 22, 'Ugboroke', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(232, 0, 'Ebrohimi', 33, 'Ebrohimi', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(233, 0, 'Eghoro', 33, 'Eghoro', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(234, 0, 'Gbokoda', 33, 'Gbokoda', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(235, 0, 'Isekelewu ( Egbema Ii )', 33, 'Isekelewu ( Egbema Ii )', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(236, 0, 'Koko I', 33, 'Koko I', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(237, 0, 'Koko Ii', 33, 'Koko Ii', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(238, 0, 'Ogbinbiri', 33, 'Ogbinbiri', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(239, 0, 'Ogbudugudu ( Egbema Iv )', 33, 'Ogbudugudu ( Egbema Iv )', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(240, 0, 'Ogheye', 33, 'Ogheye', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(241, 0, 'Opuama', 33, 'Opuama', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(242, 0, 'Bowen', 34, 'Bowen', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(243, 0, 'Edjeba', 34, 'Edjeba', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(244, 0, 'G.r.a', 34, 'G.r.a', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(245, 0, 'Igbudu', 34, 'Igbudu', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(246, 0, 'Obodo / Omadino', 34, 'Obodo / Omadino', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(247, 0, 'Ode - Itsekiri', 34, 'Ode - Itsekiri', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(248, 0, 'Ogunu / Ekurede - Urhobo', 34, 'Ogunu / Ekurede - Urhobo', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(249, 0, 'Okere', 34, 'Okere', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(250, 0, 'Okumagba', 34, 'Okumagba', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(251, 0, 'Okumagba Ii', 34, 'Okumagba Ii', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(252, 0, 'Pessu', 34, 'Pessu', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(253, 0, 'Ugbuwangue / Ekurede - Itsekiri', 34, 'Ugbuwangue / Ekurede - Itsekiri', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(254, 0, 'Aja - Udaibo', 35, 'Aja - Udaibo', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(255, 0, 'Akpikpa', 35, 'Akpikpa', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(256, 0, 'Gbaramatu', 35, 'Gbaramatu', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(257, 0, 'Isaba', 35, 'Isaba', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(258, 0, 'Madangho', 35, 'Madangho', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(259, 0, 'Ogbe - Ijoh', 35, 'Ogbe - Ijoh', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(260, 0, 'Ogidigben', 35, 'Ogidigben', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(261, 0, 'Oporoza', 35, 'Oporoza', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(262, 0, 'Orere', 35, 'Orere', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1'),
(263, 0, 'Ugborodo', 35, 'Ugborodo', 'Bincom', '0000-00-00 00:00:00', '127.0.0.1')

]

PollingUnits = [
    (8, 6, 8, 17, 181, 'DT1708006', 'Sapele Ward 8 PU _', "NULL", '5.59371889', '5.999311165', "NULL", "NULL", "NULL"),
(9, 4, 1, 19, 194, 'DT1901004', 'Primary School in Aghara', 'Primary School in Aghara', '5.599585986', '6.001336288', "NULL", "NULL", "NULL"),
(10, 5, 1, 19, 194, 'DT1401005', 'Ishere Primary School  Aghara', 'Ishere Primary School Aghara', '5.595722496', '5.99961724', "NULL", "NULL", "NULL"),
(11, 5, 3, 34, 244, 'DT3403005', 'Igini Primary School', ' Esisi Road', '5.602005475', '6.001611141', "NULL", "NULL", "NULL"),
(12, 1, 4, 21, 220, 'DT2104001', 'Umukwapa poll unit 1', "NULL", '5.596383741', '5.99023883', "NULL", "NULL", "NULL"),
(13, 16, 1, 22, 223, 'DT2201016', 'Church in Effurun1 Ovie', 'Church in Effurun1 Ovie', '5.59759314', '5.991187248', "NULL", "NULL", "NULL"),
(14, 6, 1, 19, 194, 'DT1901006', 'Ishere Primary School Aghara', "NULL", '5.90359853', '5.729595722', "NULL", "NULL", "NULL"),
(15, 13, 1, 22, 224, 'DT2201013', 'Effurun 2 in Uvwie', 'Effurun 2 in Uvwie', '5.904090609', '5.729854354', "NULL", "NULL", "NULL"),
(16, 5, 7, 7, 59, 'DT0607005', 'school in ethiope west', 'school in ethiope west', '5.895063582', '5.730405695', "NULL", "NULL", "NULL"),
(17, 9, 1, 34, 242, 'DT3401009', 'agbasa 1', 'agbasa 1', '5.904748983', '5.725361522', "NULL", "NULL", "NULL"),
(18, 7, 1, 22, 223, 'DT2201007', 'Customary Court P.t.i Road', 'Customary Court P.t.i Road', '5.904025184', '5.735836456', "NULL", "NULL", "NULL"),
(19, 11, 2, 22, 224, 'DT2202011', 'effurun 2', 'effurun 2', '5.903925673', '5.736211371', "NULL", "NULL", "NULL"),
(20, 1, 9, 35, 262, 'DT3501001', 'asumbo town hall1', 'asumbo town hall1', '5.879748019', '5.73172331', "NULL", "NULL", "NULL"),
(21, 3, 2, 22, 224, 'DT2202003', 'eki-otoi', "NULL", '5.876600455', '5.729696257', "NULL", "NULL", "NULL"),
(22, 3, 7, 6, 59, 'DT0607003', 'pollling 3 in agbara', 'pollling 3 in agbara', '5.900635513', '5.72786891', "NULL", "NULL", "NULL"),
(23, 6, 8, 6, 60, 'DT0608006', 'aghara ii', 'aghara ii', '5.879594849', '5.731894945', "NULL", "NULL", "NULL"),
(24, 4, 8, 6, 60, 'Dt0608004', 'aghara ii', 'aghara ii', '5.910613554', '5.768823319', "NULL", "NULL", "NULL"),
(25, 6, 9, 35, 262, 'DT3509006', 'obiteogbon quarters', 'obiteogbon quarters', '5.915854854', '5.775345359', "NULL", "NULL", "NULL"),
(26, 7, 9, 35, 262, 'DT3509007', 'okegbe quarter1', 'okegbe quarter1', '5.916066505', '5.775475401', "NULL", "NULL", "NULL"),
(27, 2, 7, 6, 59, 'DT0607002', 'agbasa 1', 'agbasa 1', '5.916323572', '5.775769489', "NULL", "NULL", "NULL"),
(28, 13, 3, 34, 244, 'DT340313', 'gra', 'gra', '5.916405598', '5.775643861', "NULL", "NULL", "NULL"),
(29, 14, 7, 6, 59, 'DT0607014', 'agbasa 1', 'agbasa 1', '5.976138434', '5.79185625', "NULL", "NULL", "NULL"),
(30, 8, 4, 1, 19, 'DT0104008', 'anocha north', 'anocha north', '5.976323443', '5.791971817', "NULL", "NULL", "NULL"),
(31, 12, 3, 34, 244, 'DT340312', 'gra ward', 'gra ward', '5.94474279', '5.749946582', "NULL", "NULL", "NULL"),
(32, 12, 7, 6, 59, 'DT0607012', 'school in ethiope west', 'school in ethiope west', '5.960247765', '5.787697717', "NULL", "NULL", "NULL"),
(33, 4, 3, 9, 90, 'DT0903004', 'ellu ', 'ellu ', '5.944916081', '5.749138498', "NULL", "NULL", "NULL"),
(34, 11, 9, 35, 262, 'DT3509011', 'emami quarter 2', 'emami quarter 2', '5.868711331', '5.753867466', "NULL", "NULL", "NULL"),
(35, 10, 9, 35, 262, 'DT3509010', 'emami quarter 1', 'emami quarter 1', '5.869546618', '5.752899868', "NULL", "NULL", "NULL"),
(36, 9, 9, 35, 262, 'DT3509009', 'oguanja quarters', 'oguanja quarters', '5.869563315', '5.753218155', "NULL", "NULL", "NULL"),
(37, 8, 9, 35, 262, 'DT3509008', 'okegbe quarters 2', 'okegbe quarters 2', '5.869457164', '5.753248025', "NULL", "NULL", "NULL"),
(38, 5, 9, 35, 262, 'DT3509005', 'obiteogbon quarters', 'obiteogbon quarters', '5.865254514', '5.754391377', "NULL", "NULL", "NULL"),
(39, 4, 9, 35, 262, 'DT3509004', 'ajudaibo primary school', 'ajudaibo primary school', '5.863768358', '5.754947902', "NULL", "NULL", "NULL"),
(40, 3, 9, 35, 262, 'DT3509003', 'ajudaibo primary school', 'ajudaibo primary school', '5.867018084', '5.750225876', "NULL", "NULL", "NULL"),
(41, 3, 4, 9, 91, 'DT0904003', 'isoko north', 'isoko north', '5.866359036', '5.746704932', "NULL", "NULL", "NULL"),
(42, 2, 9, 35, 262, 'DT3509002', 'hall 2', 'hall 2', '5.866407456', '5.746698042', "NULL", "NULL", "NULL"),
(43, 4, 7, 6, 59, 'DT0607004', 'school in ethiope west', 'school in ethiope west', '5.909925383', '5.794301233', "NULL", "NULL", "NULL"),
(44, 16, 2, 22, 224, 'DT220216', 'uvwie', 'uvwie', '5.878378164', '5.783819724', "NULL", "NULL", "NULL"),
(45, 6, 7, 6, 59, 'DT0607006', 'school in ethiope west', 'school in ethiope west', '5.861365948', '5.790962175', "NULL", "NULL", "NULL"),
(46, 14, 1, 19, 194, 'DT1901014', 'ughelli', 'ughelli', '5.861413666', '5.79088636', "NULL", "NULL", "NULL"),
(47, 2, 10, 15, 156, 'DT1510002', 'cable point i', 'cable point i', '5.861461099', '5.79080631', "NULL", "NULL", "NULL"),
(48, 3, 10, 15, 156, 'DT1510003', 'cable point i', 'cable point i', '5.880444551', '5.770730494', "NULL", "NULL", "NULL"),
(49, 4, 10, 15, 156, 'DT1510004', 'cable point i', 'cable point i', '5.878354903', '5.783820223', "NULL", "NULL", "NULL"),
(50, 5, 10, 15, 156, 'DT1510005', 'cable point i', 'cable point i', '5.878531591', '5.806744155', "NULL", "NULL", "NULL"),
(51, 6, 10, 15, 156, 'DT1510006', 'cable point i', 'cable point i', '5.878639525', '5.806654972', "NULL", "NULL", "NULL"),
(52, 7, 10, 15, 156, 'DT1510007', 'cable point i', 'cable point i', '5.878806006', '5.806560262', "NULL", "NULL", "NULL"),
(53, 8, 10, 15, 156, 'DT1510008', 'cable point i', 'cable point i', '5.879012412', '5.806466752', "NULL", "NULL", "NULL"),
(54, 9, 10, 15, 156, 'DT1510009', 'cable point i', 'cable point i', '5.867669536', '5.817836656', "NULL", "NULL", "NULL"),
(55, 10, 10, 15, 156, 'DT1510010', 'cable point i', 'cable point i', '5.867691306', '5.818044285', "NULL", "NULL", "NULL"),
(56, 11, 10, 15, 156, 'DT1510011', 'cable point i', 'cable point i', '5.867600201', '5.81823691', "NULL", "NULL", "NULL"),
(57, 15, 10, 15, 156, 'DT151015', 'cable point i', 'cable point i', '5.863066776', '5.830964841', "NULL", "NULL", "NULL"),
(58, 16, 10, 15, 156, 'DT151016', 'cable point i', 'cable point i', '5.873470151', '5.823753387', "NULL", "NULL", "NULL"),
(59, 17, 10, 15, 156, 'DT151017', 'cable point i', 'cable point i', '5.851069593', '5.836122533', 'Israel', '0000-00-00 00:00:00', '192.168.1.109'),
(60, 8, 8, 22, 222, 'DT2288', 'aka avenue', 'aka avenue', '5.851158986', '5.836175239', 'Israel', '0000-00-00 00:00:00', '192.168.1.109'),
(61, 8, 3, 17, 176, 'DT1738', 'sapele', 'sapele', '5.851270898', '5.836155212', 'Israel', '0000-00-00 00:00:00', '192.168.1.109'),
(62, 13, 7, 6, 59, 'DT6713', 'ethiope', 'ethiope', '5.85144335', '5.836146137', 'Israel', '0000-00-00 00:00:00', '192.168.1.109'),
(63, 5, 4, 1, 19, 'DT145', 'Aniocha North 4', 'Aniocha North 4', '5.863091905', '5.831179239', 'christian', '0000-00-00 00:00:00', '192.168.1.114'),
(64, 13, 3, 2, 6, 'DT2313', 'aniocha ward 3', 'aniocha ward 3', '5.866994163', '5.821855678', 'Israel', '0000-00-00 00:00:00', '192.168.1.109'),
(65, 6, 4, 1, 19, 'DT146', 'aniocha ward 4', 'aniocha ward 4', '5.867741304', '5.817980929', 'Israel', '0000-00-00 00:00:00', '192.168.1.109'),
(66, 21, 1, 22, 223, 'DT22121', 'uru standard junction off jakpa rd', 'uru standard junction off jakpa rd', '5.867601142', '5.818139328', 'Israel', '0000-00-00 00:00:00', '192.168.1.109'),
(67, 1, 11, 15, 157, 'DT15111', 'Oshimili', 'Oshimili South', '5.807821471', '5.797203767', 'Christopher', '0000-00-00 00:00:00', '192.168.1.109'),
(68, 2, 11, 10, 108, 'DT10112', 'Isoko', 'Isoko South', '5.807754862', '5.797288301', 'Christopher', '0000-00-00 00:00:00', '192.168.1.109'),
(69, 3, 11, 15, 157, 'DT15113', 'Oshimili', 'Oshimili', '5.842704983', '5.786380747', 'Christopher', '0000-00-00 00:00:00', '192.168.1.109'),
(70, 4, 11, 15, 157, 'DT15114', 'Oshimili', 'Oshimili South', '5.842790118', '5.786331657', 'Christopher', '0000-00-00 00:00:00', '192.168.1.109'),
(71, 5, 11, 15, 157, 'DT15115', 'Oshimili', 'Oshimili South', '5.842864681', '5.78625909', 'Christopher', '0000-00-00 00:00:00', '192.168.1.109'),
(72, 6, 11, 15, 157, 'DT15116', 'Oshimili', 'Oshimili South', '5.842019519', '5.831029509', 'Christopher', '0000-00-00 00:00:00', '192.168.1.109'),
(73, 7, 11, 15, 157, 'DT15117', 'Oshimili', 'Oshimili South', '5.842620963', '5.831811301', 'Christopher', '0000-00-00 00:00:00', '192.168.1.109'),
(74, 1, 5, 10, 104, 'DT105001', 'Isoko', 'Isoko South', '5.837696181', '5.812672375', 'Christopher', '0000-00-00 00:00:00', '192.168.1.109'),
(75, 13, 10, 21, 218, 'DT211013', 'Ukwuani', 'Ukwuani ', '5.835630792', '5.824939901', 'Christopher', '0000-00-00 00:00:00', '192.168.1.109'),
(76, 3, 4, 21, 220, 'DT2143', 'Ukwuani', 'Ukwuani', '5.835483357', '5.824884533', 'Christopher', '0000-00-00 00:00:00', '192.168.1.109'),
(77, 6, 1, 22, 223, 'DT2216', 'Effurun', 'Effurun', '5.829120073', '5.825480729', 'Christopher', '0000-00-00 00:00:00', '192.168.1.109'),
(78, 11, 10, 21, 218, 'DT211011', 'Ukwuani', 'Ukwuani', '5.822940228', '5.835938252', 'Christopher', '0000-00-00 00:00:00', '192.168.1.109'),
(79, 7, 4, 1, 19, 'DT147', 'aniocha', 'aniocha', '5.785890606', '5.829924057', 'Christopher', '0000-00-00 00:00:00', '192.168.1.109'),
(80, 3, 0, 31, 28, 'DT3103', 'Bomadi', 'Bomadi', '5.822974806', '5.835903908', 'Dare', '0000-00-00 00:00:00', '192.168.1.114'),
(81, 5, 0, 31, 28, 'DT3105', 'Bomadi', 'Bomadi', '5.813067872', '5.850975385', 'Dare', '0000-00-00 00:00:00', '192.168.1.114'),
(82, 1, 0, 31, 28, 'DT310001', 'Bomadi', 'Bomadi', '5.813128721', '5.851046574', 'Dare', '0000-00-00 00:00:00', '192.168.1.114'),
(83, 3, 6, 13, 135, 'DT1363', 'Udogbie Village', 'Udogbie Village', '5.795222618', '5.83904385', 'Israel', '0000-00-00 00:00:00', '192.168.1.109'),
(84, 8, 12, 22, 226, 'DT22128', 'aka avenue', 'aka avenue', '5.795293702', '5.839015885', 'Israel', '0000-00-00 00:00:00', '192.168.1.109'),
(85, 3, 9, 6, 61, 'DT693', 'ethiope west ', 'ethiope west ', '5.801800496', '5.895480998', 'Israel', '0000-00-00 00:00:00', '192.168.1.104'),
(86, 8, 8, 6, 60, 'DT688', 'ethiope', 'ethiope west ', '5.802012582', '5.895422869', 'Israel', '0000-00-00 00:00:00', '192.168.1.104'),
(87, 2, 8, 6, 60, 'DT682', 'ethiope', 'ethiope west ', '5.802052137', '5.895223879', 'Israel', '0000-00-00 00:00:00', '192.168.1.104'),
(88, 6, 10, 6, 62, 'DT6106', 'ethiope', 'ethiope west ', '5.800760234', '5.888332279', 'Israel', '0000-00-00 00:00:00', '192.168.1.104'),
(89, 12, 9, 6, 61, 'DT6912', 'ethiope unit 12', 'ethiope unit 12', '5.800857495', '5.888584717', 'Israel', '0000-00-00 00:00:00', '192.168.1.104'),
(90, 7, 0, 31, 26, 'DT3107', 'kolafiogbene', 'kolafio', '5.799316688', '5.892493172', 'Israel', '0000-00-00 00:00:00', '192.168.1.104'),
(91, 11, 0, 31, 26, 'DT31011', 'kolafiogbene', 'kolafio', '5.799247669', '5.892551277', 'Israel', '0000-00-00 00:00:00', '192.168.1.104'),
(92, 15, 0, 31, 26, 'DT31015', 'kolafiogbene', 'kolafiogbene', '5.949238684', '5.696328122', 'Israel', '0000-00-00 00:00:00', '192.168.1.104'),
(93, 16, 0, 31, 26, 'DT31016', 'kolafiogbene', 'kolafiogbene', '5.949328101', '5.696164548', 'Israel', '0000-00-00 00:00:00', '192.168.1.104'),
(94, 9, 0, 31, 30, 'DT3109', 'kolafiogbene', 'kolafiogbene', '5.948599325', '5.695844094', 'Israel', '0000-00-00 00:00:00', '192.168.1.104'),
(95, 8, 0, 31, 30, 'DT3108', 'kolafiogbene', 'kolafiogbene', '5.947600862', '5.72692069', 'Israel', '0000-00-00 00:00:00', '192.168.1.104'),
(96, 14, 0, 31, 26, 'DT31014', 'kolafiogbene', 'kolafiogbene', '5.9266113', '5.68939042', 'Israel', '0000-00-00 00:00:00', '192.168.1.104'),
(97, 18, 0, 31, 26, 'DT31018', 'kolafiogbene', 'kolafiogbene', '5.926621717', '5.689337411', 'Israel', '0000-00-00 00:00:00', '192.168.1.104'),
(98, 12, 0, 31, 26, 'DT31012', 'kolafiogbene', 'kolafiogbene', '5.926029293', '5.70101689', 'Israel', '0000-00-00 00:00:00', '192.168.1.104'),
(99, 4, 0, 31, 30, 'DT3104', 'kolafiogbene', 'kolafiogbene', '5.987535593', '5.77571573', 'Israel', '0000-00-00 00:00:00', '192.168.1.104'),
(100, 6, 0, 31, 30, 'DT3106', 'kolafiogbene', 'kolafiogbene', '5.964548939', '5.710539049', 'Israel', '0000-00-00 00:00:00', '192.168.1.104'),
(101, 10, 0, 31, 30, 'DT31010', 'kolafiogbene', 'kolafiogbene', '5.966931481', '5.714765312', 'Israel', '0000-00-00 00:00:00', '192.168.1.104'),
(102, 51, 0, 31, 30, 'DT31051', 'kolafiogbene', 'kolafiogbene', '5.98954208', '5.76373367', 'Israel', '0000-00-00 00:00:00', '192.168.1.104'),
(103, 21, 0, 31, 30, 'DT31021', 'kolafiogbene', 'kolafiogbene', '5.989685426', '5.76395642', 'Israel', '0000-00-00 00:00:00', '192.168.1.104'),
(104, 31, 0, 31, 30, 'DT31031', 'kolafiogbene', 'kolafiogbene', '5.970365586', '5.731097122', 'Israel', '0000-00-00 00:00:00', '192.168.1.104'),
(105, 5, 5, 11, 115, 'DT1155', 'Ndokwa east', 'Ndokwa east', '5.948545677', '5.696001704', 'Dare', '0000-00-00 00:00:00', '192.168.1.111'),
(106, 13, 0, 34, 244, 'DT34013', 'gra', 'gra', '5.953962649', '5.700047022', 'Israel', '0000-00-00 00:00:00', '192.168.1.108'),
(107, 12, 0, 34, 244, 'DT34012', 'gra', 'gra', '5.98539512', '5.764853605', 'Israel', '0000-00-00 00:00:00', '192.168.1.108'),
(108, 1, 0, 32, 38, 'DT3201', 'seimbiri', 'seimbiri', '5.989630887', '5.763867217', 'Israel', '0000-00-00 00:00:00', '192.168.1.108'),
(109, 6, 5, 11, 115, 'DT1156', 'ndokwa', 'ndokwa', '5.989745019', '5.764018125', 'Israel', '0000-00-00 00:00:00', '192.168.1.108'),
(110, 0, 0, 0, 0, '', '', '', '5.929650212', '5.671305704', '', '0000-00-00 00:00:00', ''),
(111, 0, 0, 0, 0, '', '', '', '5.940474487', '5.653550813', '', '0000-00-00 00:00:00', ''),
(112, 0, 0, 0, 0, '', '', '', '5.931835757', '5.662629319', '', '0000-00-00 00:00:00', ''),
(113, 0, 0, 0, 0, '', '', '', '5.936672207', '5.657853755', '', '0000-00-00 00:00:00', ''),
(114, 0, 0, 0, 0, '', '', '', '5.92859716', '5.662487453', '', '0000-00-00 00:00:00', ''),
(115, 0, 0, 0, 0, '', '', '', '5.935482454', '5.656266818', '', '0000-00-00 00:00:00', ''),
(116, 0, 0, 0, 0, '', '', '', '5.935635511', '5.656053666', '', '0000-00-00 00:00:00', ''),
(117, 0, 0, 0, 0, '', '', '', '5.931889364', '5.662557998', '', '0000-00-00 00:00:00', ''),
(118, 0, 0, 0, 0, '', '', '', '5.928599463', '5.662630333', '', '0000-00-00 00:00:00', ''),
(119, 0, 0, 0, 0, '', '', '', '5.928686275', '5.662599771', '', '0000-00-00 00:00:00', ''),
(120, 0, 0, 0, 0, '', '', '', '5.929439857', '5.671442497', '', '0000-00-00 00:00:00', ''),
(121, 0, 0, 0, 0, '', '', '', '5.931914231', '5.662599608', '', '0000-00-00 00:00:00', ''),
(122, 0, 0, 0, 0, '', '', '', '5.935866184', '5.669282335', '', '0000-00-00 00:00:00', ''),
(123, 0, 0, 0, 0, '', '', '', '5.92539952', '5.667627384', '', '0000-00-00 00:00:00', ''),
(124, 0, 0, 0, 0, '', '', '', '5.925370155', '5.667640993', '', '0000-00-00 00:00:00', ''),
(125, 0, 0, 0, 0, '', '', '', '5.928589515', '5.662627124', '', '0000-00-00 00:00:00', ''),
(126, 0, 0, 0, 0, '', '', '', '5.940710183', '5.653588629', '', '0000-00-00 00:00:00', ''),
(127, 0, 0, 0, 0, '', '', '', '5.946081392', '5.647803661', '', '0000-00-00 00:00:00', ''),
(128, 0, 0, 0, 0, '', '', '', '5.941149747', '5.653171959', '', '0000-00-00 00:00:00', ''),
(129, 0, 0, 0, 0, '', '', '', '5.941094329', '5.653358063', '', '0000-00-00 00:00:00', ''),
(130, 0, 0, 0, 0, '', '', '', '5.946948672', '5.648973495', '', '0000-00-00 00:00:00', ''),
(131, 0, 0, 0, 0, '', '', '', '5.947567485', '5.64427473', '', '0000-00-00 00:00:00', ''),
(132, 0, 0, 0, 0, '', '', '', '5.94746187', '5.639386229', '', '0000-00-00 00:00:00', ''),
(133, 0, 0, 0, 0, '', '', '', '5.947609958', '5.639598764', '', '0000-00-00 00:00:00', ''),
(134, 0, 0, 0, 0, '', '', '', '5.950207529', '5.637496454', '', '0000-00-00 00:00:00', ''),
(135, 0, 0, 0, 0, '', '', '', '5.951252982', '5.641761195', '', '0000-00-00 00:00:00', ''),
(136, 0, 0, 0, 0, '', '', '', '5.950150444', '5.637406656', '', '0000-00-00 00:00:00', ''),
(137, 0, 0, 0, 0, '', '', '', '5.941203333', '5.653033952', '', '0000-00-00 00:00:00', ''),
(138, 0, 0, 0, 0, '', '', '', '5.949614001', '5.632716541', '', '0000-00-00 00:00:00', ''),
(139, 0, 0, 0, 0, '', '', '', '5.949933268', '5.635520565', '', '0000-00-00 00:00:00', ''),
(140, 0, 0, 0, 0, '', '', '', '5.953090766', '5.628384606', '', '0000-00-00 00:00:00', ''),
(141, 0, 0, 0, 0, '', '', '', '5.953088726', '5.628069372', '', '0000-00-00 00:00:00', ''),
(142, 0, 0, 0, 0, '', '', '', '5.949714396', '5.632745447', '', '0000-00-00 00:00:00', ''),
(143, 0, 0, 0, 0, '', '', '', '5.952891222', '5.627623432', '', '0000-00-00 00:00:00', ''),
(144, 0, 0, 0, 0, '', '', '', '5.954259407', '5.583787026', '', '0000-00-00 00:00:00', ''),
(145, 0, 0, 0, 0, '', '', '', '5.954303954', '5.583822607', '', '0000-00-00 00:00:00', ''),
(146, 0, 0, 0, 0, '', '', '', '5.954366083', '5.583809093', '', '0000-00-00 00:00:00', ''),
(147, 0, 0, 0, 0, '', '', '', '5.952718605', '5.584089188', '', '0000-00-00 00:00:00', ''),
(148, 0, 0, 0, 0, '', '', '', '5.952705285', '5.584203464', '', '0000-00-00 00:00:00', ''),
(149, 0, 0, 0, 0, '', '', '', '5.952677451', '5.584250777', '', '0000-00-00 00:00:00', ''),
(150, 0, 0, 0, 0, '', '', '', '5.993656085', '5.600393512', '', '0000-00-00 00:00:00', ''),
(151, 0, 0, 0, 0, '', '', '', '6.032954865', '5.673289304', '', '0000-00-00 00:00:00', ''),
(152, 0, 0, 0, 0, '', '', '', '5.94980392', '5.632777333', '', '0000-00-00 00:00:00', ''),
(153, 0, 0, 0, 0, '', '', '', '6.032876093', '5.672959001', '', '0000-00-00 00:00:00', ''),
(154, 0, 0, 0, 0, '', '', '', '5.970593504', '5.695745246', '', '0000-00-00 00:00:00', ''),
(155, 0, 0, 0, 0, '', '', '', '5.970667837', '5.695321927', '', '0000-00-00 00:00:00', ''),
(156, 0, 0, 0, 0, '', '', '', '5.970679745', '5.69541788', '', '0000-00-00 00:00:00', ''),
(157, 0, 0, 0, 0, '', '', '', '6.000160473', '5.701034462', '', '0000-00-00 00:00:00', ''),
(158, 0, 0, 0, 0, '', '', '', '6.000113358', '5.701062694', '', '0000-00-00 00:00:00', ''),
(159, 0, 0, 0, 0, '', '', '', '5.999916692', '5.700983017', '', '0000-00-00 00:00:00', ''),
(160, 0, 0, 0, 0, '', '', '', '5.993273615', '5.69230046', '', '0000-00-00 00:00:00', ''),
(161, 0, 0, 0, 0, '', '', '', '6.032885641', '5.673210884', '', '0000-00-00 00:00:00', ''),
(162, 0, 0, 0, 0, '', '', '', '5.970624141', '5.695071124', '', '0000-00-00 00:00:00', ''),
(163, 0, 0, 0, 0, '', '', '', '6.000011696', '5.700996679', '', '0000-00-00 00:00:00', ''),
(164, 0, 0, 0, 0, '', '', '', '5.970676848', '5.695610689', '', '0000-00-00 00:00:00', ''),
(165, 0, 0, 0, 0, '', '', '', '6.18725973', '6.198803625', '', '0000-00-00 00:00:00', ''),
(166, 0, 0, 0, 0, '', '', '', '6.187342839', '6.198817779', '', '0000-00-00 00:00:00', ''),
(167, 0, 0, 0, 0, '', '', '', '6.187440365', '6.198925458', '', '0000-00-00 00:00:00', ''),
(168, 0, 0, 0, 0, '', '', '', '6.187057231', '6.198197231', '', '0000-00-00 00:00:00', ''),
(169, 0, 0, 0, 0, '', '', '', '6.187119111', '6.19791699', '', '0000-00-00 00:00:00', ''),
(170, 0, 0, 0, 0, '', '', '', '6.187080813', '6.197944332', '', '0000-00-00 00:00:00', ''),
(171, 0, 0, 0, 0, '', '', '', '6.187110602', '6.197851346', '', '0000-00-00 00:00:00', ''),
(172, 0, 0, 0, 0, '', '', '', '6.185416722', '6.204544183', '', '0000-00-00 00:00:00', ''),
(173, 0, 0, 0, 0, '', '', '', '6.185489112', '6.204394103', '', '0000-00-00 00:00:00', ''),
(174, 0, 0, 0, 0, '', '', '', '6.18526099', '6.204244005', '', '0000-00-00 00:00:00', ''),
(175, 0, 0, 0, 0, '', '', '', '6.160068192', '6.221072749', '', '0000-00-00 00:00:00', ''),
(176, 0, 0, 0, 0, '', '', '', '6.033867497', '6.286326012', '', '0000-00-00 00:00:00', ''),
(177, 0, 0, 0, 0, '', '', '', '6.208228494', '6.21998071', '', '0000-00-00 00:00:00', ''),
(178, 0, 0, 0, 0, '', '', '', '6.20812925', '6.219888143', '', '0000-00-00 00:00:00', ''),
(179, 0, 0, 0, 0, '', '', '', '6.208066871', '6.219797856', '', '0000-00-00 00:00:00', ''),
(180, 0, 0, 0, 0, '', '', '', '6.208009908', '6.219672376', '', '0000-00-00 00:00:00', ''),
(181, 0, 0, 0, 0, '', '', '', '6.207984832', '6.219578787', '', '0000-00-00 00:00:00', ''),
(182, 0, 0, 0, 0, '', '', '', '6.207490607', '6.227475833', '', '0000-00-00 00:00:00', ''),
(183, 0, 0, 0, 0, '', '', '', '6.207407669', '6.22745332', '', '0000-00-00 00:00:00', ''),
(184, 0, 0, 0, 0, '', '', '', '6.211155765', '6.227155738', '', '0000-00-00 00:00:00', ''),
(185, 0, 0, 0, 0, '', '', '', '6.211231425', '6.227203062', '', '0000-00-00 00:00:00', ''),
(186, 0, 0, 0, 0, '', '', '', '6.21127352', '6.227114903', '', '0000-00-00 00:00:00', ''),
(187, 0, 0, 0, 0, '', '', '', '6.206200305', '6.223128084', '', '0000-00-00 00:00:00', ''),
(188, 0, 0, 0, 0, '', '', '', '6.206259141', '6.223055902', '', '0000-00-00 00:00:00', ''),
(189, 0, 0, 0, 0, '', '', '', '6.20625521', '6.222902611', '', '0000-00-00 00:00:00', ''),
(190, 0, 0, 0, 0, '', '', '', '6.206260166', '6.222776676', '', '0000-00-00 00:00:00', ''),
(191, 0, 0, 0, 0, '', '', '', '6.253072655', '6.200481825', '', '0000-00-00 00:00:00', ''),
(192, 0, 0, 0, 0, '', '', '', '6.252989396', '6.200549159', '', '0000-00-00 00:00:00', ''),
(193, 0, 0, 0, 0, '', '', '', '6.252907166', '6.200403922', '', '0000-00-00 00:00:00', ''),
(194, 0, 0, 0, 0, '', '', '', '6.252902807', '6.200587063', '', '0000-00-00 00:00:00', ''),
(195, 0, 0, 0, 0, '', '', '', '6.251590407', '6.20135737', '', '0000-00-00 00:00:00', ''),
(196, 0, 0, 0, 0, '', '', '', '6.251557512', '6.20128579', '', '0000-00-00 00:00:00', ''),
(197, 0, 0, 0, 0, '', '', '', '6.251554219', '6.201170548', '', '0000-00-00 00:00:00', ''),
(198, 0, 0, 0, 0, '', '', '', '6.249277839', '6.198416483', '', '0000-00-00 00:00:00', ''),
(199, 0, 0, 0, 0, '', '', '', '6.251546267', '6.192148176', '', '0000-00-00 00:00:00', ''),
(200, 0, 0, 0, 0, '', '', '', '6.251589778', '6.192092584', '', '0000-00-00 00:00:00', ''),
(201, 0, 0, 0, 0, '', '', '', '6.251656927', '6.192145115', '', '0000-00-00 00:00:00', ''),
(202, 0, 0, 0, 0, '', '', '', '6.251690949', '6.192194209', '', '0000-00-00 00:00:00', ''),
(203, 0, 0, 0, 0, '', '', '', '6.242310887', '6.195543516', '', '0000-00-00 00:00:00', ''),
(204, 0, 0, 0, 0, '', '', '', '6.242411898', '6.19554119', '', '0000-00-00 00:00:00', ''),
(205, 0, 0, 0, 0, '', '', '', '6.242596022', '6.195522433', '', '0000-00-00 00:00:00', ''),
(206, 0, 0, 0, 0, '', '', '', '6.242786338', '6.195438814', '', '0000-00-00 00:00:00', ''),
(207, 0, 0, 0, 0, '', '', '', '6.242863907', '6.195510222', '', '0000-00-00 00:00:00', ''),
(208, 0, 0, 0, 0, '', '', '', '6.246382159', '6.190405162', '', '0000-00-00 00:00:00', ''),
(209, 0, 0, 0, 0, '', '', '', '6.24654691', '6.190480973', '', '0000-00-00 00:00:00', ''),
(210, 0, 0, 0, 0, '', '', '', '6.246624621', '6.190468404', '', '0000-00-00 00:00:00', ''),
(211, 0, 0, 0, 0, '', '', '', '6.246824452', '6.190578041', '', '0000-00-00 00:00:00', ''),
(212, 0, 0, 0, 0, '', '', '', '6.246974325', '6.190797731', '', '0000-00-00 00:00:00', ''),
(213, 0, 0, 0, 0, '', '', '', '6.227962894', '6.182785262', '', '0000-00-00 00:00:00', ''),
(214, 0, 0, 0, 0, '', '', '', '6.227838497', '6.182783176', '', '0000-00-00 00:00:00', ''),
(215, 0, 0, 0, 0, '', '', '', '6.227729315', '6.182759093', '', '0000-00-00 00:00:00', ''),
(216, 0, 0, 0, 0, '', '', '', '6.221966738', '6.201663891', '', '0000-00-00 00:00:00', ''),
(217, 0, 0, 0, 0, '', '', '', '6.221878943', '6.201806903', '', '0000-00-00 00:00:00', ''),
(218, 0, 0, 0, 0, '', '', '', '6.221898814', '6.201890152', '', '0000-00-00 00:00:00', ''),
(219, 0, 0, 0, 0, '', '', '', '6.22187331', '6.201965201', '', '0000-00-00 00:00:00', ''),
(220, 0, 0, 0, 0, '', '', '', '6.206466714', '6.177049236', '', '0000-00-00 00:00:00', ''),
(221, 0, 0, 0, 0, '', '', '', '6.20648286', '6.176913104', '', '0000-00-00 00:00:00', ''),
(222, 0, 0, 0, 0, '', '', '', '6.199927782', '6.18680983', '', '0000-00-00 00:00:00', ''),
(223, 0, 0, 0, 0, '', '', '', '6.199833638', '6.186886468', '', '0000-00-00 00:00:00', ''),
(224, 0, 0, 0, 0, '', '', '', '6.199754935', '6.187012587', '', '0000-00-00 00:00:00', ''),
(225, 0, 0, 0, 0, '', '', '', '6.199673133', '6.187134921', '', '0000-00-00 00:00:00', ''),
(226, 0, 0, 0, 0, '', '', '', '6.197709854', '6.185204683', '', '0000-00-00 00:00:00', ''),
(227, 0, 0, 0, 0, '', '', '', '6.230219065', '6.214893789', '', '0000-00-00 00:00:00', ''),
(228, 0, 0, 0, 0, '', '', '', '6.230449757', '6.214887775', '', '0000-00-00 00:00:00', ''),
(229, 0, 0, 0, 0, '', '', '', '6.25496909', '6.324370388', '', '0000-00-00 00:00:00', ''),
(230, 0, 0, 0, 0, '', '', '', '6.254937344', '6.324485254', '', '0000-00-00 00:00:00', ''),
(231, 0, 0, 0, 0, '', '', '', '6.254850584', '6.324509424', '', '0000-00-00 00:00:00', ''),
(232, 0, 0, 0, 0, '', '', '', '6.256462201', '6.328901893', '', '0000-00-00 00:00:00', ''),
(233, 0, 0, 0, 0, '', '', '', '6.256644926', '6.328837705', '', '0000-00-00 00:00:00', ''),
(234, 0, 0, 0, 0, '', '', '', '6.26002524', '6.350906342', '', '0000-00-00 00:00:00', ''),
(235, 0, 0, 0, 0, '', '', '', '6.26021185', '6.351114647', '', '0000-00-00 00:00:00', ''),
(236, 0, 0, 0, 0, '', '', '', '6.257493633', '6.351625219', '', '0000-00-00 00:00:00', ''),
(237, 0, 0, 0, 0, '', '', '', '6.257418562', '6.35180543', '', '0000-00-00 00:00:00', ''),
(238, 0, 0, 0, 0, '', '', '', '6.259050823', '6.350017754', '', '0000-00-00 00:00:00', ''),
(239, 0, 0, 0, 0, '', '', '', '6.283773995', '6.343019801', '', '0000-00-00 00:00:00', ''),
(240, 0, 0, 0, 0, '', '', '', '6.283703556', '6.342864557', '', '0000-00-00 00:00:00', ''),
(241, 0, 0, 0, 0, '', '', '', '6.283394129', '6.345339404', '', '0000-00-00 00:00:00', ''),
(242, 0, 0, 0, 0, '', '', '', '6.283431037', '6.345466415', '', '0000-00-00 00:00:00', ''),
(243, 0, 0, 0, 0, '', '', '', '6.292560015', '6.36078886', '', '0000-00-00 00:00:00', ''),
(244, 0, 0, 0, 0, '', '', '', '6.292728055', '6.360785128', '', '0000-00-00 00:00:00', ''),
(245, 0, 0, 0, 0, '', '', '', '6.292768054', '6.360853288', '', '0000-00-00 00:00:00', ''),
(246, 0, 0, 0, 0, '', '', '', '6.292803953', '6.360940852', '', '0000-00-00 00:00:00', ''),
(247, 0, 0, 0, 0, '', '', '', '6.303047466', '6.382018595', '', '0000-00-00 00:00:00', ''),
(248, 0, 0, 0, 0, '', '', '', '6.303053207', '6.382096338', '', '0000-00-00 00:00:00', ''),
(249, 0, 0, 0, 0, '', '', '', '6.303062886', '6.382200834', '', '0000-00-00 00:00:00', ''),
(250, 0, 0, 0, 0, '', '', '', '6.300559186', '6.376676816', '', '0000-00-00 00:00:00', ''),
(251, 0, 0, 0, 0, '', '', '', '6.300552827', '6.376490135', '', '0000-00-00 00:00:00', ''),
(252, 0, 0, 0, 0, '', '', '', '6.300457165', '6.37635446', '', '0000-00-00 00:00:00', ''),
(253, 0, 0, 0, 0, '', '', '', '6.302502254', '6.369619276', '', '0000-00-00 00:00:00', ''),
(254, 0, 0, 0, 0, '', '', '', '6.302516411', '6.369560868', '', '0000-00-00 00:00:00', ''),
(255, 0, 0, 0, 0, '', '', '', '6.302485582', '6.369508954', '', '0000-00-00 00:00:00', ''),
(256, 0, 0, 0, 0, '', '', '', '6.302544988', '6.369445201', '', '0000-00-00 00:00:00', ''),
(257, 0, 0, 0, 0, '', '', '', '6.37375796', '6.333193717', '', '0000-00-00 00:00:00', ''),
(258, 0, 0, 0, 0, '', '', '', '6.197893803', '6.276304755', '', '0000-00-00 00:00:00', ''),
(259, 0, 0, 0, 0, '', '', '', '6.197743942', '6.276216915', '', '0000-00-00 00:00:00', ''),
(260, 0, 0, 0, 0, '', '', '', '6.197731515', '6.276147511', '', '0000-00-00 00:00:00', ''),
(261, 0, 0, 0, 0, '', '', '', '6.197619564', '6.276036237', '', '0000-00-00 00:00:00', ''),
(262, 0, 0, 0, 0, '', '', '', '6.190004158', '6.270333443', '', '0000-00-00 00:00:00', ''),
(263, 0, 0, 0, 0, '', '', '', '6.189951855', '6.270410853', '', '0000-00-00 00:00:00', ''),
(264, 0, 0, 0, 0, '', '', '', '6.189943615', '6.270548989', '', '0000-00-00 00:00:00', ''),
(265, 0, 0, 0, 0, '', '', '', '6.189903693', '6.270648317', '', '0000-00-00 00:00:00', ''),
(266, 0, 0, 0, 0, '', '', '', '6.18994471', '6.270784159', '', '0000-00-00 00:00:00', ''),
(267, 0, 0, 0, 0, '', '', '', '6.192508526', '6.250961856', '', '0000-00-00 00:00:00', ''),
(268, 0, 0, 0, 0, '', '', '', '6.192200211', '6.250896597', '', '0000-00-00 00:00:00', ''),
(269, 0, 0, 0, 0, '', '', '', '6.135592062', '6.268974912', '', '0000-00-00 00:00:00', ''),
(270, 0, 0, 0, 0, '', '', '', '6.135370877', '6.268768005', '', '0000-00-00 00:00:00', ''),
(271, 0, 0, 0, 0, '', '', '', '6.135316928', '6.268909821', '', '0000-00-00 00:00:00', ''),
(272, 0, 0, 0, 0, '', '', '', '6.159869005', '6.360299833', '', '0000-00-00 00:00:00', ''),
(273, 0, 0, 0, 0, '', '', '', '6.169995128', '6.239845509', '', '0000-00-00 00:00:00', ''),
(274, 0, 0, 0, 0, '', '', '', '6.170046378', '6.23970302', '', '0000-00-00 00:00:00', ''),
(275, 0, 0, 0, 0, '', '', '', '6.161175615', '6.245285121', '', '0000-00-00 00:00:00', ''),
(276, 0, 0, 0, 0, '', '', '', '6.168812826', '6.239524125', '', '0000-00-00 00:00:00', ''),
(277, 0, 0, 0, 0, '', '', '', '6.168929109', '6.239490579', '', '0000-00-00 00:00:00', ''),
(278, 0, 0, 0, 0, '', '', '', '6.168897536', '6.239387036', '', '0000-00-00 00:00:00', ''),
(279, 0, 0, 0, 0, '', '', '', '6.167208398', '6.239989576', '', '0000-00-00 00:00:00', '')

]