



from django.urls import path

from production_app import views

urlpatterns = [
    path('addwater_category', views.addwater_category, name='addwater_category'),
    path('create_water', views.create_water, name='create_water'),
    path('view_finished_water_good', views.view_finished_water_good, name='view_finished_water_good'),
    path('update_finished_goods/<int:id>', views.update_finished_goods, name='update_finished_goods'),
    path('delete_goods/<int:id>', views.delete_goods, name='delete_goods'),
    path('Add_damagedgoods', views.Add_damagedgoods, name='Add_damagedgoods'),
    path('damaged_goods', views.damaged_goods, name='damaged_goods'),
    path('add_damaged_good_category',views.add_damaged_good_category, name='add_damaged_good_category'),
    path('damage_delete/<int:id>',views.damage_delete, name='damage_delete'),
    path('update_damage/<int:id>',views.update_damage, name='update_damage'),
    path('search',views.search,name='search')

]