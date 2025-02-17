Nome = input("Informe seu Nome: ")
Hora = input("Que horas são: ")

if Hora <= "12:00":
    print(f"Bom Dia! {Nome}")
elif Hora <= "18:00":
    print(f"Boa tarde! {Nome}")
else:
    print(f"Boa Noite! {Nome}") 
