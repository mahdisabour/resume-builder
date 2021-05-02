from django.urls import path, include
from .views import resumeView, resumeDetailView


urlpatterns = [
    path("<int:pk>/", resumeView.as_view(), name= "resume"),
    path("<int:userId>/<int:resumeId>/", resumeDetailView.as_view(), name= "resumeDetail"),

]
