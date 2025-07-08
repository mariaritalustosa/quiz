print("Welcome to Quiz!!")
answer_user = input("Want to start? (y/n)\n")

if answer_user != "y":
    quit()

print("Starting...")

language_user = input("Qual idioma de sua preferência?/Which language do you prefer?(pt-br/en)\n")

if language_user == "pt-br":
    perguntas = perguntas_pt
elif language_user == "en":
    perguntas = perguntas_en
else:
    perguntas = perguntas_pt


perguntas_pt = [
    {
        "Pergunta": "Qual a capital do Brasil?",
        "Opções": {
            "A": "Rio de Janeiro",
            "B": "Teresina",
            "C": "Brasília"
            "D": "Manaus"
        },
        "Resposta": "C"
    },
    {
        
    }
]     