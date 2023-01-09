def get_name(record_store):
    return record_store["name"]

def find_record_by_title(title, record_store):
    for record in record_store["records"]:
        if record["title"] == title:
            return record
    return None

def sell_record(record, record_store):
    # instructions: update the record_store money value so that it's inceased by the 
    # price of the record
    money_value = record_store["money"]
    record_price = record["price"]
    new_money_value = money_value + record_price
    record_store["money"] += record["price"]
    # above: have increased the record store's money

    # below: remove the sold record from the record store
    record_store["records"].remove(record)
