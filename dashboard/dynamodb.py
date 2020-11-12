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
    print (items)
    # print(response.get("Items"))
    

if __name__ == "__main__":
    main()