# from django.urls import path
# from .views import home,individual,product_page,SearchResultsView
# from django.conf.urls.static import static
# from django.conf import settings
# urlpatterns = [
#       path("",home,name="HOME"),
#       path("products/",product_page,name='PRODUCTS'),
#       path("search/", SearchResultsView.as_view(),name='search_results'),
#       path("<int:id>/",individual,name="IND-WIWAKA"),
# ]   

# if settings.DEBUG:
#       urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from .views import HomeAPIView, ProductPageAPIView, SearchResultsAPIView,CarouselApi,WiwakoDetailAPIView

urlpatterns = [
     path('home/', HomeAPIView.as_view(), name='home_api'),
     path('products/', ProductPageAPIView.as_view(), name='product_page_api'),
     path('search/', SearchResultsAPIView.as_view(), name='search_results_api'),
     path("carousel/",CarouselApi.as_view(),name="CAROUSEL"),
     path("products/<int:id>/",WiwakoDetailAPIView.as_view(),name='DETAIL')
]



if settings.DEBUG:
       urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
