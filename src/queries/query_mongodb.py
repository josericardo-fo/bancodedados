import sys

sys.path.insert(1, "./config")

from mongodb_config import get_database


def find_conversations_by_client(call_id):
    db = get_database("jul_ia")
    collection = db["conversas"]
    return collection.find({"call_id": call_id})


if __name__ == "__main__":
    call_id = ""  # Substitua pelo ID do cliente desejado
    conversations = find_conversations_by_client(call_id)
    for convo in conversations:
        print(convo)
