from django.contrib import admin
from django.urls import include, path
from myquiz import views as index_views
from quizapi import views as quizapi_views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', index_views.index, name='index'),  # Home page
    path('login/', index_views.login, name='login'),  # Login page
    path('questions/', include('quiz.urls')),  # Include quiz app URLs
    path('quizapi/', quizapi_views.QuizApiList.as_view(), name='quizapi'),  # API endpoint
    path('admin/', admin.site.urls),  # Admin site
]

urlpatterns = format_suffix_patterns(urlpatterns)
