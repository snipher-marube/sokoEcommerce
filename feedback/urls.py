from django.urls import path
from feedback.views import leave_feedback


urlpatterns = [
    path('feedbacks/', leave_feedback, name='feedback'),
]
