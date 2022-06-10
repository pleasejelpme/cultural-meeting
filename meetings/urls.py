from django.urls import path
from .views import (
    MeetingsListView,
    # PreferencesBasedListView,
    # MeetingDetailView,
    MeetingCreateView,
    meeting_detail_view,
    home_view,
    ComentarioDeleteView
)

urlpatterns = [
    path('meeting/create/', MeetingCreateView.as_view(), name='meeting-create'),
    path('meeting/<int:pk>', meeting_detail_view, name='meeting-detail'),
    path('meetings/', MeetingsListView.as_view(), name='meeting-list'),
    path('delete/<int:pk>', ComentarioDeleteView.as_view(), name='comentario-delete'),
    path('', home_view, name='home'),
]