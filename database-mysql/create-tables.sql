CREATE TABLE Hospital (
    CNPJ varchar(18) PRIMARY KEY,
    nome varchar(255),
    cidade varchar(100),
    CEP varchar(8),
    endereco varchar(255)
);

CREATE TABLE Paciente (
    CPF varchar(14) PRIMARY KEY,
    nome varchar(255),
    data_nascimento date,
    telefone varchar(20),
    endereco varchar(255),
    plano varchar(100)
);

CREATE TABLE Medico (
    CRM varchar(10) PRIMARY KEY,
    nome varchar(255),
    CPF varchar(14),
    id_hospital varchar(18),
    especialidade varchar(100),
    telefone varchar(20),
    email varchar(255),
    FOREIGN KEY (id_hospital) REFERENCES Hospital(CNPJ),
    FOREIGN KEY (id_disponibilidade) REFERENCES Disponibilidade(id_medico, id_hospital)
);

CREATE TABLE Disponibilidade (
    id_medico varchar(10),
    id_hospital varchar(18),
    dia_semana ENUM(
        'domingo',
        'segunda',
        'terca',
        'quarta',
        'quinta',
        'sexta',
        'sabado'
    ),
    hr_inicio time,
    hr_fim time,
    disponivel boolean,
    FOREIGN KEY (id_medico) REFERENCES Medico(CRM),
    FOREIGN KEY (id_hospital) REFERENCES Hospital(CNPJ),
    PRIMARY KEY (id_medico, id_hospital)
);

CREATE TABLE Consulta (
    id_medico varchar(10),
    id_hospital varchar(18),
    id_paciente varchar(14),
    data_consulta date,
    hora time,
    consulta_status enum('agendada', 'realizada', 'cancelada'),
    FOREIGN KEY (id_medico) REFERENCES Medico(CRM),
    FOREIGN KEY (id_hospital) REFERENCES Hospital(CNPJ),
    FOREIGN KEY (id_paciente) REFERENCES Paciente(CPF),
    PRIMARY KEY (id_medico, id_hospital, id_paciente)
);