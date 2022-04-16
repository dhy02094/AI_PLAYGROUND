from django.urls import path, include
from . import views
from .views import *

from django.conf import settings 
from django.conf.urls.static import static

app_name = 'ani'
urlpatterns = [
    # 어떤 글자가 오든지 views의 first_view 함수로 이동해라.
    #path('',views.first_view, name='first_view'),
    path('write/', views.write, name = 'write'),
    path('', views.fileUpload, name='fileupload'),
]

# 위 코드는 이미지 파일을 업로드 하기 위한 설정


