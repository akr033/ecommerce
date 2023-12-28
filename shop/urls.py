from . import views
from django.urls import path,include

app_name = 'shop'
urlpatterns = [
    # path('',views.index,name='index'),
    path('',views.allProdCat,name='allProdCat'),
    path('category/<slug:c_slug>/',views.allProdCat,name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.ProDetail,name='ProdCatDetail'),

    # path('movie/<int:movie_id>',views.details,name='details'),
    # path('add/',views.add_movie,name='add_movie'),
    # path('update/<int:id>',views.update,name='update'),
    # path('delete/<int:id>',views.delete,name='delete'),
]
