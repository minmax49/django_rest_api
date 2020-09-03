from django.conf.urls import url 
from worklist import views 


urlpatterns = [ 
    url(r'^worklist-detail', views.wl_detail),
]