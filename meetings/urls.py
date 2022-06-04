from django.urls import path
from .views import (
    MeetingsListView,
    PreferencesBasedListView,
    MeetingDetailView,
    MeetingCreateView,
)

urlpatterns = [
    path('meeting/create/', MeetingCreateView.as_view(), name='meeting-create'),
    path('meeting/<int:pk>', MeetingDetailView.as_view(), name='meeting-detail'),
    path('meetings/', MeetingsListView.as_view(), name='meeting-list'),
    path('', PreferencesBasedListView.as_view(), name='home'),
]