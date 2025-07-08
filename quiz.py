print("Welcome to Quiz!!")
answer_user = input("Want to start? (y/n)\n")

if answer_user != "y":
    quit()

print("Starting...")

language_user = input("Qual idioma de sua preferência?/Which language do you prefer?(pt-br/en)\n")

perguntas_pt = [
    {
        "Pergunta": "Qual a capital do Brasil?",
        "Opções": {
            "A": "Rio de Janeiro",
            "B": "Teresina",
            "C": "Brasília",
            "D": "Manaus"
        },
        "Resposta": "C"
    },
    {
        "Pergunta": "Quantos segundos tem um minuto?",
        "Opções": {
            "A": "90",
            "B": "120",
            "C": "10",
            "D": "60"
        },
        "Resposta": "D"
    }
]     

perguntas_en = [
    {
        "Question": "What is the capital of Brazil?",
        "Options": {
            "A": "Rio de Janeiro",
            "B": "Teresina",
            "C": "Brasília",
            "D": "Manaus"
        },
        "Answer": "C"
    },
    {
        "Question": "How many seconds are in a minute",
        "Options": {
            "A": "90",
            "B": "120",
            "C": "10",
            "D": "60"
        },
        "Answer": "D"
    }
] 

if language_user == "pt-br":
    perguntas = perguntas_pt
    key_pergunta = "Pergunta"
    key_opcoes = "Opções"
    key_resposta = "Resposta"
elif language_user == "en":
    perguntas = perguntas_en
    key_pergunta = "Question"
    key_opcoes = "Options"
    key_resposta = "Answer"
else:
    perguntas = perguntas_pt

score = 0

for i, pergunta in enumerate(perguntas):
    print(f"\nPergunta {i + 1}: {pergunta[key_pergunta]}")
    for letra, texto in pergunta[key_opcoes].items():
        print(f"{letra}: {texto}")

    resposta_usuario = input("Sua resposta: ").strip().upper()
    resposta_correta = pergunta[key_resposta].strip().upper()
    if resposta_usuario == resposta_correta:
        print("Resposta correta!")
        score += 1
    else: 
        print(f"Resposta errada! A resposta correta é {resposta_correta}")

print(f"\nFim do quiz! Você acertou {score}")                