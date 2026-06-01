from django.urls import path

from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("skills/", views.skills, name="skills"),
    path("education/", views.education, name="education"),
    path("experience/", views.experience, name="experience"),
    path("projects/", views.projects, name="projects"),
    path("certifications/", views.certifications, name="certifications"),
    path("contact/", views.contact, name="contact"),
]
