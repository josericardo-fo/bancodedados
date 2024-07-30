import json
import sys

# O módulo mongodb_config.py está na pasta config, que é irmão da pasta src e tia da pasta etl
sys.path.insert(1, "./config")
sys.path.insert(1, "/data")
from config_mongo import get_database


def insert_data(collection_name, data):
    db = get_database("jul_ia")
    collection = db[collection_name]
    collection.insert_many(data)


if __name__ == "__main__":
    # Carregar dados processados
    with open("data/conversas.json", encoding="utf-8") as f:
        conversas_data = json.load(f)

    insert_data("conversas", conversas_data)
