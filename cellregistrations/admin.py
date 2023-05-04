from django.contrib import admin
from .models import MembersDetail,CommunityGroup,SubCommunity

# Register your models here.

admin.site.register(CommunityGroup)
admin.site.register(SubCommunity)
admin.site.register(MembersDetail)
