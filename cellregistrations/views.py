from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib import messages
from django.views.generic.edit import CreateView

from .models import CommunityGroup, SubCommunity, MembersDetail
from .forms import SubCommunityForm, MemberForm


def home(request):
    groups = CommunityGroup.objects.all()
    context = {'groups': groups}
    return render(request, 'cellregistrations/home.html', context)

class CommunityGroupDetailView(View):
    def get(self, request, pk):
        group = get_object_or_404(CommunityGroup, pk=pk)
        sub_community_form = SubCommunityForm()
        return render(request, 'cellregistrations/community_group_detail.html', {'group': group, 'sub_community_form': sub_community_form})

    def post(self, request, pk):
        group = get_object_or_404(CommunityGroup, pk=pk)
        sub_community_form = SubCommunityForm(request.POST)
        if sub_community_form.is_valid():
            sub_community = sub_community_form.save(commit=False)
            sub_community.group = group
            sub_community.save()
            messages.success(request, 'Sub-community added successfully.')
            return redirect('community_group_detail', pk=pk)
        else:
            messages.error(request, 'There was an error adding the sub-community. Please try again.')
            return render(request, 'cellregistrations/community_group_detail.html', {'group': group, 'sub_community_form': sub_community_form})


class MembersDetailCreateView(CreateView):
    def get(self, request, sub_community_id):
        sub_community = get_object_or_404(SubCommunity, pk=sub_community_id)
        form = MemberForm()
        return render(request, 'cellregistrations/personal_details.html', {'form': form, 'sub_community': sub_community})

    def post(self, request, sub_community_id):
        sub_community = get_object_or_404(SubCommunity, pk=sub_community_id)
        form = MemberForm(request.POST)
        if form.is_valid():
            sub_community_id = self.kwargs['sub_community_id']
            member_detail = form.save(commit=False)
            member_detail.sub_community = sub_community
            member_detail.save()
            messages.success(request, 'Personal details saved successfully.')
            return redirect('home')












# from django.shortcuts import render, get_object_or_404
# from django.views.generic.edit import CreateView
# from .models import CommunityGroup, SubCommunity, MembersDetail
# from .forms import MemberForm

# def home(request):
#     groups = CommunityGroup.objects.all()
#     context = {'groups': groups}
#     return render(request, 'cellregistrations/home.html', context)

# def community_group_detail(request, group_id):
#     group = get_object_or_404(CommunityGroup, id=group_id)
#     sub_communities = group.subcommunity_set.all()
#     return render(request, 'cellregistrations/community_group_detail.html', {'group': group, 'sub_communities': sub_communities})

# class MembersDetailCreateView(CreateView):
#     model = MembersDetail
#     form_class = MemberForm
#     template_name = 'cellregistrations/personal_details.html'

#     def get_initial(self):
#         initial = super().get_initial()
#         initial['sub_community'] = self.kwargs['sub_community_id']
#         return initial

#     def form_valid(self, form):
#         sub_community = get_object_or_404(SubCommunity, id=self.kwargs['sub_community_id'])
#         form.instance.sub_community = sub_community
#         return super().form_valid(form)

# class MembersDetailCreateView(CreateView):
#     def get(self, request, sub_community_id):
#         sub_community = get_object_or_404(SubCommunity, pk=sub_community_id)
#         form = MemberForm()
#         return render(request, 'cellregistrations/personal_details.html', {'form': form, 'sub_community': sub_community})

#     def post(self, request, sub_community_id):
#         sub_community = get_object_or_404(SubCommunity, pk=sub_community_id)
#         form = MemberForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Personal details saved successfully.')
#             return redirect('home')
#         else:
#             try:
#                 sub_community_id = request.POST['sub_community_id']
#             except KeyError:
#                 messages.error(request, 'Invalid request: sub_community_id is missing.')
#                 return redirect('home')
#             messages.error(request, 'There was an error saving your personal details. Please try again.')
#             return render(request, 'cellregistrations/personal_details_create.html', {'form': form, 'sub_community': sub_community, 'sub_community_id': sub_community_id})





