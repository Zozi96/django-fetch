from django.shortcuts import get_list_or_404
from django.views.generic import CreateView

from .models import FootballClub
from .forms import FootballClubForm


class FootballClubCreateView(CreateView):
    model = FootballClub
    form_class = FootballClubForm
    success_url = '.'
    template_name = 'fc/form.html'

    def get_context_data(self, **kwargs):
        context = super(FootballClubCreateView,
                        self).get_context_data(**kwargs)
        context['objects'] = self.model.objects.all()
        return context
