from django.contrib import admin
from django.urls import path, include
from courses import views

urlpatterns = [
    path("", views.index),
    path("courses/", views.courses, name="course_home"),
    path("courses/<int:course_id>/", views.course_playlist, name="get_course"),
]