from django.shortcuts import render

# Create your views here.
# import boto3
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView


class DashboardView(TemplateView):
    template_name = "dashboard/index.html"


class GeneralFundView(TemplateView):
    template_name = "dashboard/general_fund.html"


class TechFundView(TemplateView):
    template_name = "dashboard/tech_fund.html"


class HealthFundView(TemplateView):
    template_name = "dashboard/health_fund.html"


class ChooseFundView(TemplateView):
    template_name = "dashboard/choose_fund.html"

@csrf_exempt
class FundInvestView(TemplateView):
    template_name = "dashboard/fund-invest.html"


class LoginView(TemplateView):
    template_name = "dashboard/login.html"


class FundInvestView(TemplateView):
    template_name = "dashboard/fund-invest.html"


class FundCashView(TemplateView):
    template_name = "dashboard/fund-invest-cash.html"


class FundCashSummaryView(TemplateView):
    template_name = "dashboard/fund-invest-cash-summary.html"


class FundCryptoView(TemplateView):
    template_name = "dashboard/fund-invest-crypto.html"


class FundOTPView(TemplateView):
    template_name = "dashboard/fund-invest-otp.html"


class FundSuccessView(TemplateView):
    template_name = "dashboard/fund-invest-success.html"


class DashboardNewView(TemplateView):
    template_name = "dashboard/index-new.html"
