from django.urls import path
from .views import BotListView, BotDetailView

urlpatterns = [
    path('bot-list/', BotListView.as_view(),name='bot-list'),
    path('bot-detail/<str:id>/', BotDetailView.as_view(), name='bot-detail'),
    path('bot/webhook', BotListView.as_view())
]