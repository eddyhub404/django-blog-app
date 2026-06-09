from django.shortcuts import render
from django.views import View as DjangoView


class HomeView(DjangoView):
    def get(self, request):
        return render(request, 'core/home.html')
