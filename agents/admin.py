from collections.abc import Sequence
from django.contrib import admin
from django.contrib.auth.models import Group
from django.http.request import HttpRequest
from polling_units.admin import DefaultData
from polling_units.models import PollingUnit
from django.db.models import Q

from .models import Agents

class AgentAdmin(admin.ModelAdmin):
    list_display = ['agents_fullname', "email", "phone", 'name_id', "polling_unit"]

    def get_list_display(self, request: HttpRequest) -> Sequence[str]:
        default_data = DefaultData()
        default_data.run_parties()
        default_data.run_states()
        default_data.run_lgas()
        default_data.run_wards()
        default_data.run_polling_unit()
        for agent in AGENTS:
            all_agents = Agents.objects.all()
            agent_exists = Agents.objects.filter(Q(firstname=agent[1]) & Q(lastname=agent[2]))
            pol_unit = PollingUnit.objects.filter(polling_unit_id=agent[5])
            if not agent_exists and pol_unit:
                new_agent = Agents()
                new_agent.firstname = agent[1]
                new_agent.lastname = agent[2]
                new_agent.email = agent[3]
                new_agent.phone = agent[4]
                new_agent.set_password("1")
                new_agent.polling_unit = pol_unit[0]
                new_agent.name_id = len(all_agents)+1
                new_agent.save()
        return super().get_list_display(request)
admin.site.register(Agents, AgentAdmin)
# admin.site.unregister(Group)


AGENTS = [
    (1, 'Christian', 'Emenike', 'christian@bincom.net', '08034699500', 1),
(2, 'Ngozi', 'Emenike', 'biggysmalls@home.net', '08089003444', 2),
(3, 'Chinyere', 'Emenike', 'chinyere@emenike.net', '07034532310', 1),
(4, 'Chimezie', 'Emenike', 'chimezie@emenike.net', '07034532322', 2)
]