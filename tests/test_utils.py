from src.utils import load_json, filtered_load_json, sorted_load_json, output_last_transactions, not_show_, print_result
import os
from config import ROOT_DIR

OPERATIONS_PATH = os.path.join(ROOT_DIR, "data", "operations.json")


def test_load_json():
    assert load_json(OPERATIONS_PATH)[0] == {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    }


def test_filtered_load_json(list_with_dict):
    assert filtered_load_json(list_with_dict)[0].get("state") == "EXECUTED"


def test_sorted_load_json(list_with_dict):
    assert sorted_load_json(filtered_load_json(list_with_dict))[0]["date"] == "2019-07-15T11:47:40.496961"


def test_output_last_transactions(list_with_dict):
    assert len(output_last_transactions(list_with_dict)) == 5


def test_not_show_():
    assert not_show_("Maestro 1596837868705199") == "Maestro 1596 83** **** 5199"


def test_print_result(list_with_dict):
    assert print_result(list_with_dict[0]) == None
