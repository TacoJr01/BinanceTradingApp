import logging

def place_order(client, symbol, side, order_type, quantity, price=None):
    params = {
    "symbol": symbol.upper(),
    "side": side,
    "type": order_type,
    "quantity": quantity,
    "newOrderRespType": "RESULT"
}

    if order_type == "LIMIT":
        params["price"] = price
        params["timeInForce"] = "GTC"

    logging.info(f"Request: {params}")
    response = client.place_order(**params)
    logging.info(f"Response: {response}")
    return response
