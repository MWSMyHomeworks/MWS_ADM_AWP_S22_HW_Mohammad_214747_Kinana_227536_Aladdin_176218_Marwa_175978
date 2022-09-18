from django.urls import path
# noinspection PyPackages
from .views import LoanStatusViews

urlpatterns = [
    path('loanStatus/', LoanStatusViews.as_view()),
    path('loanstatus/', LoanStatusViews.as_view()),
    path('loanStatus', LoanStatusViews.as_view()),
    path('loanstatus', LoanStatusViews.as_view())
]
