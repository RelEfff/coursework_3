import json
import datetime



def load_json(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        response = json.load(file)
        return response


def filtered_load_json(json_):
    filtered_list = []
    for state in json_:
        if state.get("state") == "EXECUTED":
            filtered_list.append(state)
    return filtered_list


def sorted_load_json(filtered_json):
    return sorted(filtered_json, key=lambda x: x["date"], reverse=True)


def output_last_transactions(sorted_json):
    return sorted_json[:5]

def not_show_(result):
    if result == None:
        return None
    elif result[0:4] in "Счет":
        return "Счет **" + result[-4:]
    else:
        return result[:-16] + result[-16:-12] + " " + result[-12:-10] + "** **** " + result[-4:]

def print_result(dict_with_operation):
        date_transaction = datetime.datetime.fromisoformat(dict_with_operation["date"])
        date_transaction = date_transaction.strftime('%d.%m.%Y')
        operation_amount = dict_with_operation["operationAmount"]["amount"]
        currency = dict_with_operation["operationAmount"]["currency"]["name"]
        description = dict_with_operation["description"]
        from_transaction = not_show_(dict_with_operation.get("from"))
        to_transaction = not_show_(dict_with_operation["to"])
        print(f"""
        {date_transaction} {description}
        {from_transaction} -> {to_transaction}
        {operation_amount} {currency}
        """)
