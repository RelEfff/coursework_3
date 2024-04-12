import json
import os
import datetime
from config import ROOT_DIR

OPERATIONS_PATH = os.path.join(ROOT_DIR, "data", "operations.json")


def load_json():
    with open(OPERATIONS_PATH) as file:
        response = json.load(file)
        return response


def filtered_load_json():
    filtered_list = []
    for state in load_json():
        if state.get("state") == "EXECUTED":
            filtered_list.append(state)
    return filtered_list


def sorted_load_json():
    return sorted(filtered_load_json(), key=lambda x: x["date"], reverse=True)


def output_last_transactions():
    return sorted_load_json()[:5]

def not_show_(result):
    if result == None:
        return None
    elif result[0:4] in "Счет":
        return "Счет **" + result[-4:]
    else:
        return result[:-16] + result[-16:-12] + " " + result[-12:-10] + "** **** " + result[-4:]

def print_result():
    for result in output_last_transactions():
        date_transaction = datetime.datetime.fromisoformat(result["date"])
        date_transaction = date_transaction.strftime('%d.%m.%Y')
        operation_amount = result["operationAmount"]["amount"]
        currency = result["operationAmount"]["currency"]["name"]
        description = result["description"]
        from_transaction = not_show_(result.get("from"))
        to_transaction = not_show_(result["to"])
        print(f"""
        {date_transaction} {description}
        {from_transaction} -> {to_transaction}
        {operation_amount} {currency}
        """)
