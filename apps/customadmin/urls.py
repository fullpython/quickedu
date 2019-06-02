from django.urls import path
from . import views


urlpatterns = [
    path('',views.AdminHomeView.as_view(),name='admin_page'),
    path('course/',views.CourseListView.as_view(),name='course_list'),
]