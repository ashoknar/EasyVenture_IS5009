import boto3

def main():
    ## Get single item from a table
    # client = boto3.client('dynamodb')
    # response = client.get_item(
    #     TableName='funds',
    #     Key={
    #         'ticker': { # ticket is primary key attribute name
    #             'S': 'HEALTHVD', # S represents string, HEALTHVD is the primary key value
    #         }
    #     }
    # )
    # print(response)
    
    ## Get all items from a table
    client = boto3.client('dynamodb')
    dynamodb = boto3.resource('dynamodb')
    # response = client.scan(
    #     TableName='funds'
    # )
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
    print(item)
    # items = response.get("Items")
    # for item in items:
    #     item["description"] = item.get("description").get("S")
    #     item["name"] = item.get("name").get("S")
    #     item["price"] = item.get("price").get("S")
    #     item["ticker"] = item.get("ticker").get("S")
    #     item["holding_period"] = item.get("holding_period").get("S")
    #     item["management_firm"] = item.get("management_firm").get("S")
    #     item["fund_target"] = item.get("fund_target").get("S")
    #     item["available_units"] = item.get("available_units").get("S")
    #     item["rating"] = item.get("rating").get("S")
    table = dynamodb.Table('user_portfolio')
    table.update_item(
        Key={
            'email': 'valerie_chua@email.com'
        },
        UpdateExpression='SET funds = :val1',
        ExpressionAttributeValues={
            ':val1': str(400)
        }
    )
    result = dynamodb.update_item(  
        Key={  
            "email": 'valerie_chua@email.com'  
        },  
        UpdateExpression="SET funds.#player_id.score = :score_val",  
        ExpressionAttributeNames={  
            "#player_id": player_id  
        },  
        ExpressionAttributeValues={  
            ":score_val": score_val  
        }  
    )
    rc = table.update_item(Key={ 'username' : user }, 
    UpdateExpression="set list[" + itemnum + "].field = :nd",
    ExpressionAttributeValues={
        ':nd': data,
    },
    ReturnValues="UPDATED_NEW"
    )
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
    fund_list = item.get("funds").get("L")
    print(item)
    # print(response.get("Items"))
    

if __name__ == "__main__":
    main()