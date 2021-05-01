from django.views.generic import CreateView
from django.http import JsonResponse

from .models import FootballClub
from .forms import FootballClubForm


class FootballClubCreateView(CreateView):
    model = FootballClub
    form_class = FootballClubForm
    success_url = '.'
    template_name = 'fc/form.html'

    def get_context_data(self, **kwargs):
        context = super(
            FootballClubCreateView,
            self
        ).get_context_data(**kwargs)
        context['objects'] = self.model.objects.all()
        return context

    def render_to_response(self, context, **response_kwargs):
        if self.request.is_ajax():
            data = list(context['objects'].values())
            return JsonResponse({'objects': data})
        else:
            response_kwargs.setdefault('content_type', self.content_type)
            return self.response_class(
                request=self.request,
                template=self.get_template_names(),
                context=context,
                using=self.template_engine,
                **response_kwargs
            )
