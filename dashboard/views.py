from django.shortcuts import render

# Create your views here.
# import boto3
from django.views.generic import TemplateView


class DashboardView(TemplateView):
    template_name = "dashboard/index.html"


class GeneralFundView(TemplateView):
    template_name = "general_fund/index.html"


class TechFundView(TemplateView):
    template_name = "tech_fund/index.html"


class ChooseFundView(TemplateView):
    template_name = "choose_fund/index.html"


class FundInvestView(TemplateView):
    template_name = "dashboard/fund-invest.html"


class LoginView(TemplateView):
    template_name = "dashboard/login.html"


class FundInvestView(TemplateView):
    template_name = "dashboard/fund-invest.html"
