from django.contrib import admin
from django.urls import path, include
from library import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.default.urls')),
    path('library/', views.library),
    path('library/library', views.book_info),
]

# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns =[
#         path('__debug__/', include(debug_toolbar.urls)),
#     ] + urlpatterns
