from django.urls import path
from . import views


urlpatterns = [
    path('',views.AdminHomeView.as_view(), name='admin_page'),
    path('course/',views.CourseListView.as_view(), name='course_list'),
    path('course/<int:pk>',views.CourseDetailView.as_view(), name='course_detail'),
    path('course/create',views.CourseCreateView.as_view(), name='course_create'),
    path('course/<int:pk>/update',views.CourseUpdateView.as_view(), name='course_update'),
    path('course/<int:pk>/delete',views.CourseDeleteView.as_view(), name='course_delete'),
    
]