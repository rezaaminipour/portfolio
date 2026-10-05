from django.views.generic import TemplateView
from .models import SiteSetting, SocialLink, EmploymentHistory, Skill

class PortfolioView(TemplateView):
    template_name = 'portfolio/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['settings'] = SiteSetting.objects.first()
        context['social_links'] = SocialLink.objects.filter(is_active=True)
        context['employment_history'] = EmploymentHistory.objects.all()
        context['skills'] = Skill.objects.all()
        return context
