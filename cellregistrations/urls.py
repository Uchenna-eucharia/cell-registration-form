# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.home, name='home'),
#     path('subcommunity/<int:sub_community_id>/create/', views.MembersDetailCreateView.as_view(), name='personal_details_create'),
# ]



from django.urls import path
from . import views
from .views import  CommunityGroupDetailView, MembersDetailCreateView

urlpatterns = [
    path('', views.home, name='home'),
    path('community-group/<int:pk>/', CommunityGroupDetailView.as_view(), name='community_group_detail'),
    path('subcommunity/<int:sub_community_id>/create/', MembersDetailCreateView.as_view(), name='personal_details_create'),
]
