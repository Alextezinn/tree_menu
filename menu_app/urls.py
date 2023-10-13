from django.urls import path

from menu_app.views import IndexPageView

urlpatterns = [
    path('', IndexPageView.as_view(), name='home'),
    path('item/<slug:item_slug>/', IndexPageView.as_view(), name='item'),
]
