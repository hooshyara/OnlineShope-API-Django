from django.urls import path
from .views import   ProductListView, ComparisonView, CommentsView
app_name = 'products'


urlpatterns = [
    path('', ProductListView.as_view()),
    path('<int:id>/delete', ProductListView.as_view(), name='delete_product'),
    path('<int:id>/update', ProductListView.as_view(), name='update_product'),
    path('<int:id>/comparison', ComparisonView.as_view(), name='Comparison'),
    path('<int:id>/comment/', CommentsView.as_view(), name='comment_create'),


    
   





 


    

] 