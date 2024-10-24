from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/todo/', include('todo_app.urls')),
    path('api/blog/', include('blog.urls')),
    path('api/book/', include('book.urls')),
]
