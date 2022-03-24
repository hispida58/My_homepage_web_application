from django.views.generic import TemplateView
import requests
import json
from MyPublications import publications_list


class HomePageView(TemplateView):
    template_name = "home.html"
    text = "MASH"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)

        pub_list = publications_list()
        print(pub_list)
        context.update({'some_list': pub_list['results']})
        return context
# Create your views here.
