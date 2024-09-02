from . import views
from django.urls import include,path

urlpatterns = [
    path('umma/', views.umma_view, name='umma_page'),
    path('', views.home,name='home'),
    path('a/', views.hom,name='hom'),
    
    # path('search/', views.search, name='search'),

    path('my/', views.my_view, name='my_view'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),

    path('view/',views.view,name='view'),
    path('addproduct/',views.product_create,name='product_create'),
    path('editproduct/<int:product_id>/', views.product_update, name='product_update'),
    
    path('deleteproduct/<int:product_id>/', views.product_delete, name='product_delete'),
    path('register/',views.register,name="register"),
    path('login/',views.loginpage,name="login"),
    path('logout/', views.logout_user, name="logout"),

    path('user_status/', views.user_status, name='user_status'),

    
    path('cart/', views.cart, name='cart'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),


    path('increase_quantity/<int:cart_item_id>/', views.increase_quantity, name='increase_quantity'),
    path('decrease_quantity/<int:cart_item_id>/', views.decrease_quantity, name='decrease_quantity'),

    path('checkout/', views.checkout, name='checkout'),


    path('category/<int:category_id>/', views.category_detail, name='category_detail'),

    path('user_orders/', views.user_orders, name='user_orders'),  # Add this line

    path('users_with_orders/', views.users_with_orders, name='users_with_orders'),  # Add this line

]
