
from django.urls import path

from register_app import views

urlpatterns = [

    path('adddepartment',views.add_department,name='adddepartment'),
    path('admin', views.login_view, name='login'),  # Ensure this view exists

    path('add_designation',views.add_designation,name='add_designation'),
    path('register_view',views.register_view,name='register_view'),
    path('view_users',views.view_users,name='view_users'),
    path('edit_user/<int:id>/', views.Edit_user, name='edit_user'),
    path('delete_user/<int:user_id>/', views.delete_user_view, name='delete_user'),
    # path('create_permission/<int:id>/', views.create_permission, name='create_permission'),


]