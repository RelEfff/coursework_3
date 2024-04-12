from src.utils import print_result, load_json, filtered_load_json, sorted_load_json, output_last_transactions
from config import ROOT_DIR
import os

OPERATIONS_PATH = os.path.join(ROOT_DIR, "data", "operations.json")

def main():
    operations = load_json(OPERATIONS_PATH)
    filtered_list = filtered_load_json(operations)
    sorted_list = sorted_load_json(filtered_list)
    output_list = output_last_transactions(sorted_list)


    for operation in output_list:

        print_result(operation)



if __name__ == "__main__":
    main()