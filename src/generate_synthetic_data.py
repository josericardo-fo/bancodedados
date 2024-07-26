import json
import random
from datetime import timedelta

from faker import Faker
from faker.providers.phone_number import Provider

fake = Faker("pt_BR")
fake.add_provider(Provider)
fake_en = Faker("en_US")
Faker.seed(4321)
random.seed(4321)


def generate_brazil_phone_number():
    return f"+55 {fake.msisdn()[:2]} 9{fake.msisdn()[3:7]}-{fake.msisdn()[7:11]}"


def generate_synthetic_data(num_records):
    data = []

    for _ in range(num_records):
        call_id = fake.unique.random_int(min=1, max=1000)
        phone_number = generate_brazil_phone_number()
        start_time = fake.date_time_this_year()
        end_time = start_time + timedelta(minutes=random.randint(1, 30))
        call_status = random.choice(["complete", "incomplete", "failed"])
        num_system_messages = random.randint(5, 15)
        num_user_messages = num_system_messages + random.choice([-1, 0, 1])
        history_messages = {
            "user": [fake_en.sentence() for _ in range(num_user_messages)],
            "system": [fake_en.sentence() for _ in range(num_system_messages)],
        }
        service = random.choice(["appointment", "info", "complaint"])
        rating = random.randint(1, 10)

        record = {
            "call_id": call_id,
            "phone_number": phone_number,
            "start_time": start_time.isoformat(),
            "end_time": end_time.isoformat(),
            "call_status": call_status,
            "history_messages": history_messages,
            "service": service,
            "rating": rating,
        }

        data.append(record)

    return data


num_records = 1000  # Adjust the number of records as needed
synthetic_data = generate_synthetic_data(num_records)

# Save to a JSON file
with open("conversas.json", "w") as f:
    json.dump(synthetic_data, f, indent=4)

print(f"Generated {num_records} synthetic records and saved to conversas.json")
