from django.urls import path
from .views import AllMoves, SelectedMove

urlpatterns = [
    path('', AllMoves.as_view(), name='all_views'),
    path('<str:name>/', SelectedMove.as_view(), name='selected_move' )
]