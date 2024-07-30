-- Tabela Paciente
CREATE TABLE
    Paciente (
        CPF VARCHAR(14) PRIMARY KEY,
        nome VARCHAR(255),
        data_nascimento DATE,
        telefone VARCHAR(20),
        endereco VARCHAR(255),
        plano VARCHAR(255)
    );

-- Tabela Medico
CREATE TABLE
    Medico (
        CRM VARCHAR(10) PRIMARY KEY,
        CPF VARCHAR(14),
        nome VARCHAR(255),
        especialidade VARCHAR(255),
        telefone VARCHAR(20),
        email VARCHAR(255)
    );

-- Tabela Hospital
CREATE TABLE
    Hospital (
        CNPJ VARCHAR(18) PRIMARY KEY,
        nome VARCHAR(255),
        cidade VARCHAR(255),
        CEP VARCHAR(8),
        endereco VARCHAR(255)
    );

-- Tabela Disponibilidade
CREATE TABLE
    Disponibilidade (
        id_disponibilidade INT PRIMARY KEY AUTO_INCREMENT,
        id_medico VARCHAR(10),
        id_hospital VARCHAR(18),
        dia_semana ENUM (
            'domingo',
            'segunda',
            'terca',
            'quarta',
            'quinta',
            'sexta',
            'sabado'
        ),
        hr_inicio TIME,
        hr_fim TIME,
        FOREIGN KEY (id_medico) REFERENCES Medico (CRM),
        FOREIGN KEY (id_hospital) REFERENCES Hospital (CNPJ)
    );

-- Tabela Consulta
CREATE TABLE
    Consulta (
        id_consulta INT PRIMARY KEY AUTO_INCREMENT,
        id_medico VARCHAR(10),
        id_hospital VARCHAR(18),
        id_paciente VARCHAR(14),
        data_consulta DATE,
        hora TIME,
        consulta_status ENUM ('agendada', 'realizada', 'cancelada'),
        FOREIGN KEY (id_medico) REFERENCES Medico (CRM),
        FOREIGN KEY (id_hospital) REFERENCES Hospital (CNPJ),
        FOREIGN KEY (id_paciente) REFERENCES Paciente (CPF)
    );