from django.urls import path

from .views import CentralGovernmentSignUpView, LoginView, TimerAddView, TimerView, ManagerSignUpView, \
    GroupSignUpView, ActionView, ActionListView, GroupListView, GroupDetailView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('gov/signup/', CentralGovernmentSignUpView.as_view(), name='gov-signup'),
    path('manager/signup/', ManagerSignUpView.as_view(), name='manager-signup'),  # todo
    path('group/signup/', GroupSignUpView.as_view(), name='group-signup'),
    path('group/list/', GroupListView.as_view(), name='group-list'),
    path('group/detail/', GroupDetailView.as_view(), name='group-detail'),

    path('timer/add/', TimerAddView.as_view(), name='timer-add'),
    path('timer/', TimerView.as_view(), name='timer'),  # todo

    # path('location/list/', LocationListView.as_view(), name='location-list'),

    path('action/list/', ActionListView.as_view(), name='action-list'),
    path('action/', ActionView.as_view(), name='action'),
]
