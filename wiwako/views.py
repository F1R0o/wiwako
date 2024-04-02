# from django.shortcuts import render
# from .models import Wiwako
# from django.core.paginator import Paginator
# from .forms import SearchForm
# from django.views.generic import ListView
# from django.db.models import Q
# from carousel.models import CarouselItem
# # # # Create your views here.
# def home(request):
#     wiwakebi = Wiwako.objects.all()[:3]
#     carousel_items = CarouselItem.objects.all()
#     context = {"wiwaka": wiwakebi, "carousel_items": carousel_items}
#     return render(request, "wiwako/home.html", context)


# def individual(request,id):
#       wiwaka = Wiwako.objects.get(pk=id)
#       redirect_to = {"wiwaka":wiwaka}
#       return render(request,"wiwako/individual.html",redirect_to)



# def product_page(request):
#      selected_category = request.GET.get('category') 
#      if selected_category:  
#          wiwakebi = Wiwako.objects.filter(category__name=selected_category).order_by("-id")
#      else: 
#          wiwakebi = Wiwako.objects.all().order_by("-id")
    
#      paginator = Paginator(wiwakebi, 1)
#      page_number = request.GET.get('page', 1)
#      page_obj = paginator.get_page(page_number)
#      context = {"wiwaka": page_obj}
#      return render(request, "wiwako/products.html", context)






# class SearchResultsView(ListView):
#     model = Wiwako
#     template_name = 'wiwako/results.html'
#     context_object_name = 'results'
#     paginate_by = 2

#     def get_queryset(self):
#           query = self.request.GET.get('query')
#           queryset = Wiwako.objects.all().order_by("-id")
        
#           if query:
#               queryset = queryset.filter(
#                   Q(saxeli_qartulad__icontains=query) | Q(saxeli_inglisurad__icontains=query)
#               )
        
#           return queryset

#     def get_context_data(self, **kwargs):
#           context = super().get_context_data(**kwargs)
#           context['query'] = self.request.GET.get('query', '')
#           return context
    




from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from .models import Wiwako
from carousel.models import CarouselItem
from .serializers import WiwakoSerializer, CarouselItemSerializer
from django.db.models import Q
from rest_framework.views import APIView







class Pagination(PageNumberPagination):
     page_size = 3
     page_size_query_param = 'page_size'
     max_page_size = 1000


class HomeAPIView(ListAPIView):
    queryset = Wiwako.objects.all()[:3]
    serializer_class = WiwakoSerializer

class CarouselApi(ListAPIView):
    queryset = CarouselItem.objects.all()
    serializer_class = CarouselItemSerializer




class ProductPageAPIView(ListAPIView):
     serializer_class = WiwakoSerializer
     pagination_class = Pagination

     def get_queryset(self):
         category_name = self.request.GET.get('category')
         queryset = Wiwako.objects.all().order_by("-id")
        
         if category_name:
             queryset = queryset.filter(category__name=category_name)
        
         return queryset


class SearchResultsAPIView(ListAPIView):
     serializer_class = WiwakoSerializer
     pagination_class = Pagination

     def get_queryset(self):
         query = self.request.GET.get('query')
         queryset = Wiwako.objects.all().order_by("-id")
        
         if query:
            queryset = queryset.filter(
                 Q(saxeli_qartulad__icontains=query) | Q(saxeli_inglisurad__icontains=query)
             )
        
         return queryset