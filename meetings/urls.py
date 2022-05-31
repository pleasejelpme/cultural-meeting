from django.urls import path
from .views import (
    MeetingsListView,
    PreferencesBasedListView,
    MeetingDetailView
)

urlpatterns = [
    path('meeting/<int:pk>', MeetingDetailView.as_view(), name='meeting-detail'),
    path('meetings/', MeetingsListView.as_view(), name='meeting-list'),
    path('', PreferencesBasedListView.as_view(), name='home'),
]