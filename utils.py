from datetime import datetime

def get_current_date():
    return datetime.now().strftime("%Y-%m-%d")

def calculate_total_bill(price_per_night, nights):
    return float(price_per_night) * int(nights)