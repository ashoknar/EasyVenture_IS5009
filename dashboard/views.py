from django.shortcuts import render

# Create your views here.
import boto3, copy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404, render


# class DashboardView(TemplateView):
#     template_name = "dashboard/index.html"


class GeneralFundView(TemplateView):
    template_name = "dashboard/general_fund.html"


class TechFundView(TemplateView):
    template_name = "dashboard/tech_fund.html"


class HEALTHVD(TemplateView):
    template_name = "dashboard/health_fund.html"
    
class GENERALVD(TemplateView):
    template_name = "dashboard/health_fund.html"
    
class TECHVDS2(TemplateView):
    template_name = "dashboard/health_fund.html"

class TECHVD(TemplateView):
    template_name = "dashboard/health_fund.html"

class GENERALVDS2(TemplateView):
    template_name = "dashboard/health_fund.html"
    
class HEALTHVDS2(TemplateView):
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


class FundSellView(TemplateView):
    template_name = 'dashboard/fund-sell-cash.html'


class FundSellSummaryView(TemplateView):
    template_name = 'dashboard/fund-sell-cash-summary.html'


class FundSellOTPView(TemplateView):
    template_name = 'dashboard/fund-sell-otp.html'


class FundSellSuccessView(TemplateView):
    template_name = 'dashboard/fund-sell-success.html'


class DashboardSellView(TemplateView):
    template_name = 'dashboard/index-sell.html'
    

def dashboard(request):
    client = boto3.client('dynamodb')
    response = client.get_item(
        TableName='user_portfolio',
        Key={
            'email': {
                'S': 'valerie_chua@email.com',
            }
        }
    )
    
    item = response.get("Item")
    item["earnings"] = item.get("earnings").get("S")
    item["email"] = item.get("email").get("S")
    item["invested"] = item.get("invested").get("S")
    fund_list = item.get("funds").get("L")
    fund_list_updated = []
    for fund in fund_list:
        fund_updated = {
            "name": fund.get("M").get("name").get("S"),
            "ticker": fund.get("M").get("ticker").get("S"),
            "units": fund.get("M").get("units").get("S"),
            "market_value": fund.get("M").get("market_value").get("S"),
            "profit_percent": fund.get("M").get("profit_percent").get("S")
        }
        fund_list_updated.append(fund_updated)
    item["funds"] = fund_list_updated
    context = {
        'profile': item
    }
    return render(request, 'dashboard/index.html', context)
    
def choose_fund(request):
    ## Get all items from a table
    client = boto3.client('dynamodb')
    response = client.scan(
        TableName='funds'
    )
    items = response.get("Items")
    for item in items:
        item["description"] = item.get("description").get("S")
        item["name"] = item.get("name").get("S")
        item["price"] = item.get("price").get("S")
        item["ticker"] = item.get("ticker").get("S")
        item["holding_period"] = item.get("holding_period").get("S")
        item["management_firm"] = item.get("management_firm").get("S")
        item["fund_target"] = item.get("fund_target").get("S")
        item["available_units"] = item.get("available_units").get("S")
        item["rating"] = item.get("rating").get("S")
    context = {
        'funds': items
    }
    return render(request, 'dashboard/choose_fund.html', context)

    
def fund(request):
    ## Get all items from a table
    client = boto3.client('dynamodb')
    query = request.GET.items()
    for item in query:
        query = item[0]
    print(query)
    response = client.get_item(
        TableName='funds',
        Key={
            'ticker': { # ticket is primary key attribute name
                'S': query, # S represents string, HEALTHVD is the primary key value
            }
        }
    )
    
    item = response.get("Item")
    item["description"] = item.get("description").get("S")
    item["name"] = item.get("name").get("S")
    item["price"] = item.get("price").get("S")
    item["ticker"] = item.get("ticker").get("S")
    item["holding_period"] = item.get("holding_period").get("S")
    item["management_firm"] = item.get("management_firm").get("S")
    item["fund_target"] = item.get("fund_target").get("S")
    item["available_units"] = item.get("available_units").get("S")
    item["rating"] = item.get("rating").get("S")
    # print (item)
    context = {
        'fund': item
    }

    return render(request, 'dashboard/fund.html', context)    

def fund_invest(request):
    client = boto3.client('dynamodb')
    query = request.GET.items()
    for item in query:
        query = item[0]
    print(query)
    response = client.get_item(
        TableName='user_portfolio',
        Key={
            'email': {
                'S': 'valerie_chua@email.com',
            }
        }
    )
    item = response.get("Item")
    item["earnings"] = item.get("earnings").get("S")
    item["email"] = item.get("email").get("S")
    item["invested"] = item.get("invested").get("S")
    item['wallet'] = item.get("wallet").get("S")
    fund_list = item.get("funds").get("L")
    response2 = client.get_item(
        TableName='funds',
        Key={
            'ticker': { # ticket is primary key attribute name
                'S': query, # S represents string, HEALTHVD is the primary key value
            }
        }
    )
    
    fund_updated = response2.get("Item")
    fund_updated["description"] = fund_updated.get("description").get("S")
    fund_updated["name"] = fund_updated.get("name").get("S")
    fund_updated["price"] = fund_updated.get("price").get("S")
    fund_updated["ticker"] = fund_updated.get("ticker").get("S")
    fund_updated["holding_period"] = fund_updated.get("holding_period").get("S")
    fund_updated["management_firm"] = fund_updated.get("management_firm").get("S")
    fund_updated["fund_target"] = fund_updated.get("fund_target").get("S")
    fund_updated["available_units"] = fund_updated.get("available_units").get("S")
    fund_updated["rating"] = fund_updated.get("rating").get("S")
    context = {
        'profile': item,
        'fund': fund_updated
    }
    return render(request, 'dashboard/fund-invest-cash.html', context)
    

def fund_summary(request):
    client = boto3.client('dynamodb')
    query = request.GET.items()
    print("POST", request.POST)
    for item in query:
        query = item[0]
    print(query)
    response = client.get_item(
        TableName='user_portfolio',
        Key={
            'email': {
                'S': 'valerie_chua@email.com',
            }
        }
    )
    item = response.get("Item")
    item["earnings"] = item.get("earnings").get("S")
    item["email"] = item.get("email").get("S")
    item["invested"] = item.get("invested").get("S")
    item['wallet'] = item.get("wallet").get("S")
    item['crypto'] = item.get("crypto").get("S")
    item['amount'] = request.POST.get('amount')
    item['type'] = request.POST.get('type')
    fund_list = item.get("funds").get("L")
    
    response2 = client.get_item(
        TableName='funds',
        Key={
            'ticker': { # ticket is primary key attribute name
                'S': query, # S represents string, HEALTHVD is the primary key value
            }
        }
    )
    
    fund_updated = response2.get("Item")
    fund_updated["description"] = fund_updated.get("description").get("S")
    fund_updated["name"] = fund_updated.get("name").get("S")
    fund_updated["price"] = fund_updated.get("price").get("S")
    fund_updated["ticker"] = fund_updated.get("ticker").get("S")
    fund_updated["holding_period"] = fund_updated.get("holding_period").get("S")
    fund_updated["management_firm"] = fund_updated.get("management_firm").get("S")
    fund_updated["fund_target"] = fund_updated.get("fund_target").get("S")
    fund_updated["available_units"] = fund_updated.get("available_units").get("S")
    fund_updated["rating"] = fund_updated.get("rating").get("S")
    context = {
        'profile': item,
        'fund': fund_updated
    }
    fund_list2 = copy.deepcopy(fund_list)
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('user_portfolio')
    if item['type'] == 'cash':
        table.update_item(
            Key={
                'email': 'valerie_chua@email.com'
            },
            UpdateExpression='SET invested = :val1',
            ExpressionAttributeValues={
                ':val1': str(float(item['invested']) + float(item['amount']) )
            }
        )
        table.update_item(
            Key={
                'email': 'valerie_chua@email.com'
            },
            UpdateExpression='SET wallet = :val1',
            ExpressionAttributeValues={
                ':val1': str(float(item['wallet']) -(float(item['amount']) ))
            }
        )
        print("if updated")
        
        print(fund_list2)
        flag = True
        element = -1
        count = 0
        for fund in fund_list2:
            if fund.get("M").get("ticker").get("S") == query:
                flag = False
                fund["M"]["units"]["S"] = str(int(fund.get("M").get("units").get("S")) - ( float(item['amount']) /  float(fund["M"]["unit_price"]["S"])))
                fund["M"]["market_value"]["S"] = str(float(fund["M"]["units"]["S"]) * float(fund["M"]["unit_price"]["S"]))
            count = count + 1
        if flag:
            fund = copy.deepcopy(fund_list2[0])
            fund["M"]["ticker"]["S"] = query
            fund["M"]["name"]["S"] = fund_updated["name"]
            fund["M"]["units"]["S"] = str(int(int(fund.get("M").get("units").get("S")) - ( float(item['amount']) /  float(fund["M"]["unit_price"]["S"]))))
            fund["M"]["market_value"]["S"] = str(int(float(fund["M"]["units"]["S"]) * float(fund["M"]["unit_price"]["S"])))
            fund_list2.append(fund)
        response = client.update_item(
            TableName='user_portfolio',
            Key={
                'email': {
                    'S': 'valerie_chua@email.com',
                }
            },
            AttributeUpdates={
                'funds': {
                    'Value': {
                        'L': fund_list2
                    },
                    'Action': 'PUT'
                }
            }
        )
    else:
        curr_val = int(item['amount']) * int(fund_updated['unit_price'])
        table.update_item(
            Key={
                'email': 'valerie_chua@email.com'
            },
            UpdateExpression='SET invested = :val1',
            ExpressionAttributeValues={
                ':val1': str(int(item['invested']) - curr_val )
            }
        )
        table.update_item(
            Key={
                'email': 'valerie_chua@email.com'
            },
            UpdateExpression='SET wallet = :val1',
            ExpressionAttributeValues={
                ':val1': str(float(item['wallet']) - float(item['amount']) )
            }
        )
        print("else updated")
    return render(request, 'dashboard/fund-invest-cash-summary.html', context)
    
def fund_sell(request):
    client = boto3.client('dynamodb')
    query = request.GET.items()
    for item in query:
        print("WERER", item)
        query = item[0]
    print(query)
    response = client.get_item(
        TableName='user_portfolio',
        Key={
            'email': {
                'S': 'valerie_chua@email.com',
            }
        }
    )
    item = response.get("Item")
    item["earnings"] = item.get("earnings").get("S")
    item["email"] = item.get("email").get("S")
    item["invested"] = item.get("invested").get("S")
    item['wallet'] = item.get("wallet").get("S")
    fund_list = item.get("funds").get("L")
    
    for fund in fund_list:
        print("Ticker", fund.get("M").get("ticker").get("S"))
        print("Q", query)
        print(fund.get("M").get("ticker").get("S") == query)
        if fund.get("M").get("ticker").get("S") == query:
            fund_updated = {
                "name": fund.get("M").get("name").get("S"),
                "ticker": fund.get("M").get("ticker").get("S"),
                "units": fund.get("M").get("units").get("S"),
                "market_value": fund.get("M").get("market_value").get("S"),
                "profit_percent": fund.get("M").get("profit_percent").get("S"),
                "unit_price": fund.get("M").get("unit_price").get("S")
            }
    item["fund"] = fund_updated
    context = {
        'profile': item
    }
    return render(request, 'dashboard/fund-sell-cash.html', context)

def fund_sell_summary(request):
    client = boto3.client('dynamodb')
    query = request.GET.items()
    for item in query:
        print(item)
        query = item[0]
    # print(query)
    response = client.get_item(
        TableName='user_portfolio',
        Key={
            'email': {
                'S': 'valerie_chua@email.com',
            }
        }
    )
    item = response.get("Item")
    item["earnings"] = item.get("earnings").get("S")
    item["email"] = item.get("email").get("S")
    item["invested"] = item.get("invested").get("S")
    item['wallet'] = item.get("wallet").get("S")
    item['amount'] = request.POST.get('amount')
    item['type'] = request.POST.get('type')
    # print(item)
    fund_list = item.get("funds").get("L")
    fund_list2 = copy.deepcopy(fund_list)
    
    for fund in fund_list:
        # print("Ticker", fund.get("M").get("ticker").get("S"))
        # print("Q", query)
        # print(fund.get("M").get("ticker").get("S") == query)
        if fund.get("M").get("ticker").get("S") == query:
            fund_updated = {
                "name": fund.get("M").get("name").get("S"),
                "ticker": fund.get("M").get("ticker").get("S"),
                "units": fund.get("M").get("units").get("S"),
                "market_value": fund.get("M").get("market_value").get("S"),
                "profit_percent": fund.get("M").get("profit_percent").get("S"),
                "unit_price": fund.get("M").get("unit_price").get("S"),
            }
    value = int(fund_updated["unit_price"]) * int(item["amount"])
    # print(value)
    fund_updated["value"] = str(value)
    item["fund"] = fund_updated
    context = {
        'profile': item
    }
    
    response2 = client.get_item(
        TableName='funds',
        Key={
            'ticker': { # ticket is primary key attribute name
                'S': query, # S represents string, HEALTHVD is the primary key value
            }
        }
    )
    
    fund_item = response2.get("Item")
    print(fund_item.get("price").get("S"))
    print('hello2')
    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('user_portfolio')
    if item['type'] == 'cash':
        table.update_item(
            Key={
                'email': 'valerie_chua@email.com'
            },
            UpdateExpression='SET invested = :val1',
            ExpressionAttributeValues={
                ':val1': str(float(item['invested']) - (float(item['amount']) * float(fund_item.get("price").get("S"))))
            }
        )
        table.update_item(
            Key={
                'email': 'valerie_chua@email.com'
            },
            UpdateExpression='SET wallet = :val1',
            ExpressionAttributeValues={
                ':val1': str(float(item['wallet']) + (float(item['amount']) * float(fund_item.get("price").get("S"))))
            }
        )
        print("if updated")
        
        print(fund_list2)
        element = -1
        count = 0
        for fund in fund_list2:
            if fund.get("M").get("ticker").get("S") == query:
                fund["M"]["units"]["S"] = str(int(fund.get("M").get("units").get("S")) - int(item['amount']))
                fund["M"]["market_value"]["S"] = str(float(fund["M"]["units"]["S"]) * float(fund["M"]["unit_price"]["S"]))
                if fund["M"]["units"]["S"] == '0':
                    element = count
            count = count + 1
        if element > -1:
            fund_list2.remove(element)
        response = client.update_item(
            TableName='user_portfolio',
            Key={
                'email': {
                    'S': 'valerie_chua@email.com',
                }
            },
            AttributeUpdates={
                'funds': {
                    'Value': {
                        'L': fund_list2
                    },
                    'Action': 'PUT'
                }
            }
        )
    else:
        curr_val = int(item['amount']) * int(fund_updated['unit_price'])
        table.update_item(
            Key={
                'email': 'valerie_chua@email.com'
            },
            UpdateExpression='SET invested = :val1',
            ExpressionAttributeValues={
                ':val1': str(int(item['invested']) - curr_val )
            }
        )
        table.update_item(
            Key={
                'email': 'valerie_chua@email.com'
            },
            UpdateExpression='SET wallet = :val1',
            ExpressionAttributeValues={
                ':val1': str(float(item['wallet']) - float(item['amount']) )
            }
        )
        print("else updated")
    return render(request, 'dashboard/fund-sell-cash-summary.html', context)
    

def fund_invest_crypto(request):
    client = boto3.client('dynamodb')
    query = request.GET.items()
    for item in query:
        query = item[0]
    print(query)
    response = client.get_item(
        TableName='user_portfolio',
        Key={
            'email': {
                'S': 'valerie_chua@email.com',
            }
        }
    )
    item = response.get("Item")
    item["earnings"] = item.get("earnings").get("S")
    item["email"] = item.get("email").get("S")
    item["invested"] = item.get("invested").get("S")
    item["wallet"] = item.get("wallet").get("S")
    item["crpyto"] = item.get("crypto").get("S")
    item["amount"] = request.POST.get('amount')
    fund_list = item.get("funds").get("L")
    response2 = client.get_item(
        TableName='funds',
        Key={
            'ticker': { # ticket is primary key attribute name
                'S': query, # S represents string, HEALTHVD is the primary key value
            }
        }
    )
    
    fund_updated = response2.get("Item")
    fund_updated["description"] = fund_updated.get("description").get("S")
    fund_updated["name"] = fund_updated.get("name").get("S")
    fund_updated["price"] = fund_updated.get("price").get("S")
    fund_updated["ticker"] = fund_updated.get("ticker").get("S")
    fund_updated["holding_period"] = fund_updated.get("holding_period").get("S")
    fund_updated["management_firm"] = fund_updated.get("management_firm").get("S")
    fund_updated["fund_target"] = fund_updated.get("fund_target").get("S")
    fund_updated["available_units"] = fund_updated.get("available_units").get("S")
    fund_updated["rating"] = fund_updated.get("rating").get("S")
    context = {
        'profile': item,
        'fund': fund_updated
    }
    return render(request, 'dashboard/fund-invest-crypto.html', context)
    
# def HEALTHVD(request):
#     ## Get all items from a table
#     client = boto3.client('dynamodb')
#     response = client.get_item(
#         TableName='funds',
#         Key={
#             'ticker': { # ticket is primary key attribute name
#                 'S': 'HEALTHVD', # S represents string, HEALTHVD is the primary key value
#             }
#         }
#     )
    
#     item = response.get("Item")
#     item["description"] = item.get("description").get("S")
#     item["name"] = item.get("name").get("S")
#     item["price"] = item.get("price").get("S")
#     item["ticker"] = item.get("ticker").get("S")
#     item["holding_period"] = item.get("holding_period").get("S")
#     item["management_firm"] = item.get("management_firm").get("S")
#     item["fund_target"] = item.get("fund_target").get("S")
#     item["available_units"] = item.get("available_units").get("S")
#     item["rating"] = item.get("rating").get("S")
#     # print (item)
#     context = {
#         'fund': item
#     }

#     return render(request, 'dashboard/fund.html', context)
    
# def GENERALVD(request):
#     ## Get all items from a table
#     client = boto3.client('dynamodb')
#     response = client.get_item(
#         TableName='funds',
#         Key={
#             'ticker': { # ticket is primary key attribute name
#                 'S': 'GENERALVD', # S represents string, HEALTHVD is the primary key value
#             }
#         }
#     )
    
#     item = response.get("Item")
#     item["description"] = item.get("description").get("S")
#     item["name"] = item.get("name").get("S")
#     item["price"] = item.get("price").get("S")
#     item["ticker"] = item.get("ticker").get("S")
#     item["holding_period"] = item.get("holding_period").get("S")
#     item["management_firm"] = item.get("management_firm").get("S")
#     item["fund_target"] = item.get("fund_target").get("S")
#     item["available_units"] = item.get("available_units").get("S")
#     item["rating"] = item.get("rating").get("S")
#     # print (item)
#     context = {
#         'fund': item
#     }

#     return render(request, 'dashboard/fund.html', context)
    
# def TECHVDS2(request):
#     ## Get all items from a table
#     client = boto3.client('dynamodb')
#     response = client.get_item(
#         TableName='funds',
#         Key={
#             'ticker': { # ticket is primary key attribute name
#                 'S': 'TECHVDS2', # S represents string, HEALTHVD is the primary key value
#             }
#         }
#     )
    
#     item = response.get("Item")
#     item["description"] = item.get("description").get("S")
#     item["name"] = item.get("name").get("S")
#     item["price"] = item.get("price").get("S")
#     item["ticker"] = item.get("ticker").get("S")
#     item["holding_period"] = item.get("holding_period").get("S")
#     item["management_firm"] = item.get("management_firm").get("S")
#     item["fund_target"] = item.get("fund_target").get("S")
#     item["available_units"] = item.get("available_units").get("S")
#     item["rating"] = item.get("rating").get("S")
#     # print (item)
#     context = {
#         'fund': item
#     }

#     return render(request, 'dashboard/fund.html', context)
    
# def TECHVD(request):
#     ## Get all items from a table
#     client = boto3.client('dynamodb')
#     response = client.get_item(
#         TableName='funds',
#         Key={
#             'ticker': { # ticket is primary key attribute name
#                 'S': 'TECHVD', # S represents string, HEALTHVD is the primary key value
#             }
#         }
#     )
    
#     item = response.get("Item")
#     item["description"] = item.get("description").get("S")
#     item["name"] = item.get("name").get("S")
#     item["price"] = item.get("price").get("S")
#     item["ticker"] = item.get("ticker").get("S")
#     item["holding_period"] = item.get("holding_period").get("S")
#     item["management_firm"] = item.get("management_firm").get("S")
#     item["fund_target"] = item.get("fund_target").get("S")
#     item["available_units"] = item.get("available_units").get("S")
#     item["rating"] = item.get("rating").get("S")
#     # print (item)
#     context = {
#         'fund': item
#     }

#     return render(request, 'dashboard/fund.html', context)
    
# def GENERALVDS2(request):
#     ## Get all items from a table
#     client = boto3.client('dynamodb')
#     response = client.get_item(
#         TableName='funds',
#         Key={
#             'ticker': { # ticket is primary key attribute name
#                 'S': 'GENERALVDS2', # S represents string, HEALTHVD is the primary key value
#             }
#         }
#     )
    
#     item = response.get("Item")
#     item["description"] = item.get("description").get("S")
#     item["name"] = item.get("name").get("S")
#     item["price"] = item.get("price").get("S")
#     item["ticker"] = item.get("ticker").get("S")
#     item["holding_period"] = item.get("holding_period").get("S")
#     item["management_firm"] = item.get("management_firm").get("S")
#     item["fund_target"] = item.get("fund_target").get("S")
#     item["available_units"] = item.get("available_units").get("S")
#     item["rating"] = item.get("rating").get("S")
#     # print (item)
#     context = {
#         'fund': item
#     }

#     return render(request, 'dashboard/fund.html', context)
    
# def HEALTHVDS2(request):
#     ## Get all items from a table
#     client = boto3.client('dynamodb')
#     response = client.get_item(
#         TableName='funds',
#         Key={
#             'ticker': { # ticket is primary key attribute name
#                 'S': 'HEALTHVDS2', # S represents string, HEALTHVD is the primary key value
#             }
#         }
#     )
    
#     item = response.get("Item")
#     item["description"] = item.get("description").get("S")
#     item["name"] = item.get("name").get("S")
#     item["price"] = item.get("price").get("S")
#     item["ticker"] = item.get("ticker").get("S")
#     item["holding_period"] = item.get("holding_period").get("S")
#     item["management_firm"] = item.get("management_firm").get("S")
#     item["fund_target"] = item.get("fund_target").get("S")
#     item["available_units"] = item.get("available_units").get("S")
#     item["rating"] = item.get("rating").get("S")
#     # print (item)
#     context = {
#         'fund': item
#     }

#     return render(request, 'dashboard/fund.html', context)