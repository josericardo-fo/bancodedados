import random
from datetime import datetime, timedelta

import pandas as pd
from faker import Faker

fake = Faker("pt_BR")
Faker.seed(4321)
random.seed(4321)

# Lista de DDDs válidos no Brasil
valid_ddd = [
    "11", "12", "13", "14", "15", "16", "17", "18", "19",  # São Paulo
    "21", "22", "24",  # Rio de Janeiro
    "27", "28",  # Espírito Santo
    "31", "32", "33", "34", "35", "37", "38",  # Minas Gerais
    "41", "42", "43", "44", "45", "46",  # Paraná
    "47", "48", "49",  # Santa Catarina
    "51", "53", "54", "55",  # Rio Grande do Sul
    "61",  # Distrito Federal
    "62", "64",  # Goiás
    "63",  # Tocantins
    "65", "66",  # Mato Grosso
    "67",  # Mato Grosso do Sul
    "68",  # Acre
    "69",  # Rondônia
    "71", "73", "74", "75", "77",  # Bahia
    "79",  # Sergipe
    "81", "87",  # Pernambuco
    "82",  # Alagoas
    "83",  # Paraíba
    "84",  # Rio Grande do Norte
    "85", "88",  # Ceará
    "86", "89",  # Piauí
    "91", "93", "94",  # Pará
    "92", "97",  # Amazonas
    "95",  # Roraima
    "96",  # Amapá
    "98", "99"  # Maranhão
]

# Lista de especialidades médicas com pesos
specialties = [
    ("Obstetricia", 20),
    ("Ginecologia", 20),
    ("Pediatria", 15),
    ("Cardiologia", 10),
    ("Ortopedia", 10),
    ("Dermatologia", 10),
    ("Neurologia", 5),
    ("Psiquiatria", 5),
    ("Endocrinologia", 5),
]

# Lista de planos de saúde
planos_saude = ["Bradesco Saude", "Hapvida", "Sul America", "Unimed"]


def gerar_brazil_phone_number():
    ddd = random.choice(valid_ddd)
    return f"+55 {ddd} 9{fake.msisdn()[3:7]}-{fake.msisdn()[7:11]}"


def gerar_hospitais(num_hospitais):
    hospitais = []
    for _ in range(num_hospitais):
        hospitais.append(
            {
                "CNPJ": fake.cnpj(),
                "nome": fake.company(),
                "cidade": fake.city(),
                "CEP": fake.postcode(False),
                "endereco": fake.address(),
            }
        )
    return hospitais


def gerar_pacientes(num_pacientes):
    pacientes = []
    for _ in range(num_pacientes):
        pacientes.append(
            {
                "CPF": fake.cpf(),
                "nome": fake.name(),
                "data_nascimento": fake.date_of_birth(
                    minimum_age=0, maximum_age=100
                ).strftime("%Y-%m-%d"),
                "telefone": gerar_brazil_phone_number(),
                "endereco": fake.address(),
                "plano": random.choice(planos_saude),
            }
        )
    return pacientes


def gerar_medicos(num_medicos, hospitais):
    medicos = []
    specialty_choices, weights = zip(*specialties)
    for _ in range(num_medicos):
        medicos.append(
            {
                "CRM": fake.numerify(text="#######"),
                "nome": fake.name(),
                "CPF": fake.cpf(),
                "id_hospital": random.choice(hospitais)["CNPJ"],
                "especialidade": random.choices(specialty_choices, weights=weights)[0],
                "telefone": gerar_brazil_phone_number(),
                "email": fake.email(),
            }
        )
    return medicos


def gerar_disponibilidades(medicos):
    disponibilidades = []
    for medico in medicos:
        for _ in range(
            random.randint(1, 7)
        ):  # Cada médico tem entre 1 e 7 disponibilidades
            start_time = random.choice(
                [
                    fake.date_time_this_year().replace(
                        hour=h, minute=0, second=0, microsecond=0
                    )
                    for h in range(8, 12)
                ]
                + [
                    fake.date_time_this_year().replace(
                        hour=h, minute=0, second=0, microsecond=0
                    )
                    for h in range(14, 18)
                ]
            )
            end_time = start_time + timedelta(hours=1)
            disponibilidades.append(
                {
                    "id_medico": medico["CRM"],
                    "id_hospital": medico["id_hospital"],
                    "dia_semana": random.choice(
                        [
                            "domingo",
                            "segunda",
                            "terca",
                            "quarta",
                            "quinta",
                            "sexta",
                            "sabado",
                        ]
                    ),
                    "hr_inicio": start_time.time().strftime("%H:%M:%S"),
                    "hr_fim": end_time.time().strftime("%H:%M:%S"),
                }
            )
    return disponibilidades


def gerar_consultas(num_consultas, medicos, pacientes, hospitais):
    consultas = []
    for _ in range(num_consultas):
        start_time = random.choice(
            [
                fake.date_time_between_dates(
                    datetime_start=datetime(2024, 1, 1),
                    datetime_end=datetime(2024, 12, 31),
                ).replace(hour=h, minute=0, second=0, microsecond=0)
                for h in range(8, 12)
            ]
            + [
                fake.date_time_between_dates(
                    datetime_start=datetime(2024, 1, 1),
                    datetime_end=datetime(2024, 12, 31),
                ).replace(hour=h, minute=0, second=0, microsecond=0)
                for h in range(14, 18)
            ]
        )
        consulta_status = random.choices(
            ["agendada", "realizada", "cancelada"],
            weights=[
                0 if start_time < datetime(2024, 7, 31) else 0.8,
                0.8 if start_time < datetime(2024, 7, 31) else 0,
                0.2,
            ],
        )[0]
        consultas.append(
            {
                "id_medico": random.choice(medicos)["CRM"],
                "id_hospital": random.choice(hospitais)["CNPJ"],
                "id_paciente": random.choice(pacientes)["CPF"],
                "data_consulta": start_time.date().strftime("%Y-%m-%d"),
                "hora": start_time.time().strftime("%H:%M:%S"),
                "consulta_status": consulta_status,
            }
        )
    return consultas


num_hospitais = 10
num_pacientes = 50
num_medicos = 20
num_consultas = 100

hospitais = gerar_hospitais(num_hospitais)
pacientes = gerar_pacientes(num_pacientes)
medicos = gerar_medicos(num_medicos, hospitais)
disponibilidades = gerar_disponibilidades(medicos)
consultas = gerar_consultas(num_consultas, medicos, pacientes, hospitais)

df_hospitais = pd.DataFrame(hospitais)
df_pacientes = pd.DataFrame(pacientes)
df_medicos = pd.DataFrame(medicos)
df_disponibilidades = pd.DataFrame(disponibilidades)
df_consultas = pd.DataFrame(consultas)

df_hospitais.to_csv("Hospitais.csv", index=False)
df_pacientes.to_csv("Pacientes.csv", index=False)
df_medicos.to_csv("Medicos.csv", index=False)
df_disponibilidades.to_csv("Disponibilidades.csv", index=False)
df_consultas.to_csv("Consultas.csv", index=False)

print("Arquivos CSV foram criados.")
