import quiz.views as quiz_views
from django.urls import path

urlpatterns = [
    path('', quiz_views.qpage, name='qpage'),  # Home page or main quiz page
]
