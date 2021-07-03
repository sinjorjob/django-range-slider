from django.contrib import admin
from django.urls import path
from sample.views import MemberList #追加

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list', MemberList.as_view(), name="list"),  #追加
]
