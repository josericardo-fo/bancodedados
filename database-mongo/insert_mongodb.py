import json
import sys

sys.path.insert(1, "./config")
sys.path.insert(1, "/data")
from config_mongodb import get_database


def insert_data(collection_name, data):
    db = get_database("jul_ia")
    collection = db[collection_name]
    collection.insert_many(data)


if __name__ == "__main__":
    # Carregar dados processados
    with open("../data/mongo/historico_conversas.json", encoding="utf-8") as f:
        conversas_data = json.load(f)

    insert_data("conversas", conversas_data)
