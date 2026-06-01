def validate_side(side):
    side = side.upper()

    if side not in ["BUY", "SELL"]:
        raise ValueError(
            "Invalid side. Allowed values: BUY, SELL"
        )

def validate_order_type(order_type):
    order_type = order_type.upper()

    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError(
            "Invalid order type. Allowed values: MARKET, LIMIT"
        )