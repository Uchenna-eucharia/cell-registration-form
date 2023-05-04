from django import forms
from .models import MembersDetail, SubCommunity

class MemberForm(forms.ModelForm):
    class Meta:
        model = MembersDetail
        fields = ['email','first_name', 'last_name', 'email', 'whatsapp_number', 'gender', 'age','marital_status','city','country','is_member','center','church','hear','is_first','consent']


class SubCommunityForm(forms.ModelForm):
    class Meta:
        model = SubCommunity
        fields = ['name']
