"""
main views modules for DjangoNoobs project
"""
from django.shortcuts import render
from django.views.generic import View

class Index(View):
    """
    class-based view for index page
    """
    template_name = 'index.html'

    def get(self, request):
        """
        GET Request method
        """
        return render(request, self.template_name)

    def post(self, request):
        """
        POST Request method
        """
        return render(request, self.template_name)
