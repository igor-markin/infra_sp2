from django.urls import path

from api.views import GetConfirmationCodeView, GetTokenView

urlpatterns = [
    path('auth/email/', GetConfirmationCodeView.as_view()),
    path('auth/token/', GetTokenView.as_view()),
]
