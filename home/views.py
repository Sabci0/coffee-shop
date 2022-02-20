from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        ctx =super().get_context_data(**kwargs)
        ctx['users'] = get_user_model().objects.all()
        return ctx

class ContactView(TemplateView):
    template_name = 'home/contact.html'

