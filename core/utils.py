def cnpj_verification(self, value):
    cnpj = value.replace('.', '').replace('-', '').replace('/', '')
    cnpj_block = ['00000000000000', '11111111111111', '22222222222222', '33333333333333', '44444444444444',
                  '55555555555555', '66666666666666', '77777777777777', '88888888888888', '99999999999999']

    if cnpj in cnpj_block:
        return False

    if not cnpj or len(cnpj) < 14:
        return False

    antigo_cnpj = [int(d) for d in cnpj]
    novo_cnpj = antigo_cnpj[:12]
    weight = [5, 6, 7, 8, 9, 2, 3, 4, 5, 6, 7, 8, 9]
    dv1 = sum([novo_cnpj[i] * weight[1:][i] for i in range(12)]) % 11
    dv1 = dv1 if dv1 < 10 else 0
    novo_cnpj.append(dv1)
    dv2 = sum([novo_cnpj[i] * weight[i] for i in range(13)]) % 11
    dv2 = dv2 if dv2 < 10 else 0
    novo_cnpj.append(dv2)

    if novo_cnpj == antigo_cnpj:
        return True
    return False


PAISES_CHOICES = [
    ('Brasil', 'Brasil'),
    ('Argentina', 'Argentina'),
    ('Chile', 'Chile'),
    ('Colômbia', 'Colômbia'),
    ('Peru', 'Peru'),
    ('Venezuela', 'Venezuela'),
    ('México', 'México'),
    ('Estados Unidos', 'Estados Unidos'),
    ('Canadá', 'Canadá'),
    ('França', 'França'),
    ('Alemanha', 'Alemanha'),
    ('Itália', 'Itália'),
    ('Espanha', 'Espanha'),
    ('Portugal', 'Portugal'),
    ('Reino Unido', 'Reino Unido'),
    ('Japão', 'Japão'),
    ('China', 'China'),
    ('Índia', 'Índia'),
    ('Austrália', 'Austrália'),
    ('África do Sul', 'África do Sul'),
    ('Nigéria', 'Nigéria'),
    ('Egito', 'Egito'),
    ('Rússia', 'Rússia'),
    ('Arábia Saudita', 'Arábia Saudita'),
]

CIDADES_CHOICES = [
    ('São Paulo', 'São Paulo'),
    ('Rio de Janeiro', 'Rio de Janeiro'),
    ('Buenos Aires', 'Buenos Aires'),
    ('Córdoba', 'Córdoba'),
    ('Santiago', 'Santiago'),
    ('Valparaíso', 'Valparaíso'),
    ('Bogotá', 'Bogotá'),
    ('Medellín', 'Medellín'),
    ('Lima', 'Lima'),
    ('Arequipa', 'Arequipa'),
    ('Caracas', 'Caracas'),
    ('Valência', 'Valência'),
    ('Cidade do México', 'Cidade do México'),
    ('Guadalajara', 'Guadalajara'),
    ('Nova Iorque', 'Nova Iorque'),
    ('Los Angeles', 'Los Angeles'),
    ('Toronto', 'Toronto'),
    ('Vancouver', 'Vancouver'),
    ('Paris', 'Paris'),
    ('Marselha', 'Marselha'),
    ('Berlim', 'Berlim'),
    ('Munique', 'Munique'),
    ('Roma', 'Roma'),
    ('Milão', 'Milão'),
    ('Madri', 'Madri'),
    ('Barcelona', 'Barcelona'),
    ('Lisboa', 'Lisboa'),
    ('Porto', 'Porto'),
    ('Londres', 'Londres'),
    ('Manchester', 'Manchester'),
    ('Tóquio', 'Tóquio'),
    ('Osaka', 'Osaka'),
    ('Pequim', 'Pequim'),
    ('Shanghai', 'Shanghai'),
    ('Nova Deli', 'Nova Deli'),
    ('Bombaim', 'Bombaim'),
    ('Sydney', 'Sydney'),
    ('Melbourne', 'Melbourne'),
    ('Cidade do Cabo', 'Cidade do Cabo'),
    ('Joanesburgo', 'Joanesburgo'),
    ('Lagos', 'Lagos'),
    ('Abuja', 'Abuja'),
    ('Cairo', 'Cairo'),
    ('Alexandria', 'Alexandria'),
    ('Moscou', 'Moscou'),
    ('São Petersburgo', 'São Petersburgo'),
    ('Riade', 'Riade'),
    ('Jeddah', 'Jeddah'),
]