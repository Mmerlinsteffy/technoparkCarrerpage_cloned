from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('Job/<int:id>/',views.globcom,name='globe')
]
