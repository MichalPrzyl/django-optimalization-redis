from django.contrib import admin
from django.urls import include, path
from main.views import PersonAPI
import debug_toolbar

urlpatterns = [
    path("admin/", admin.site.urls),
    path("person", PersonAPI.as_view()),
]

urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
