"""IS5009 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from dashboard import views
from django.views.generic import TemplateView

urlpatterns = [
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('dashboard_new/', views.DashboardNewView.as_view(), name='dashboard-new'),
    path('choose_fund/', views.ChooseFundView.as_view(), name='choose_fund'),
    path('general_fund/', views.GeneralFundView.as_view(), name='general_fund'),
    path('health_fund/', views.HealthFundView.as_view(), name='health_fund'),
    path('tech_fund/', views.TechFundView.as_view(), name='tech_fund'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('fund_invest/', views.FundInvestView.as_view(), name='fund-invest'),
    path('fund_invest/cash/', views.FundCashView.as_view(), name='fund-invest-cash'),
    path('fund_invest/cash/summary/', views.FundCashSummaryView.as_view(), name='fund-invest-cash-summary'),
    path('fund_invest/cash/otp/', views.FundOTPView.as_view(), name='fund-invest-otp'),
    path('fund_invest/cash/success/', views.FundSuccessView.as_view(), name='fund-invest-success'),
    path('fund_invest/crypto/', views.FundCryptoView.as_view(), name='fund-invest-crypto'),
    path('admin/', admin.site.urls),
]
