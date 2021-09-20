from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [

    # ---django admin--- #
    url(r'admin/', admin.site.urls),

    # ---api to access product app--- #
    url('api/v1/', include("product.urls")),

    
]