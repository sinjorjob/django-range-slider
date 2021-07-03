from django.shortcuts import render
from .models import Member
from django.views.generic import ListView
from .filters import MemberFilter  #追加

class MemberList(ListView):
    template_name = 'sample/list.html'
    model = Member

    def get_context_data(self, **kwargs):
       context = super(MemberList, self).get_context_data(**kwargs)
       member_filter = MemberFilter(self.request.GET) #追加
       context['member_filter'] = member_filter  #変更
       return context