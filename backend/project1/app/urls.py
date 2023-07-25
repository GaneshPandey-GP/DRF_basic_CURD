from django.urls import path
from . import views
urlpatterns = [
    path('stu_info/', views.GetStudentInfo),
    path('insert_new_stu/', views.InsertNewStudent),
    path('insert_new_stu_in_bulk/', views.InsertNewStudent_inBulk),
    path('update_info/', views.UpdateStudent),
    path('delete_info/', views.DeleteInfo)
]
