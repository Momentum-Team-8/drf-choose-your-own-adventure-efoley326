from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path, include
from library import views

urlpatterns = [
    
    path('api-auth/', include('rest_framework.urls')),
    path('library/', views.TheLibrary.as_view()),
    path('library/<int:pk>/', views.BookProfile.as_view()),
    path('admin/', admin.site.urls),
]

urlpatterns = format_suffix_patterns(urlpatterns)

# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns =[
#         path('__debug__/', include(debug_toolbar.urls)),
#     ] + urlpatterns
