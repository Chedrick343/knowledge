from logic import And, Not, Implication, Or, Symbol, model_check

# Symbols
# "Rain"
# "Hagrid"
# "Dumbledore"

# knowledge
knowledge = And()


# Si no llovió, Harry visitó a Hagrid hoy
# Harry visitó a Hagrid o a Dumbledore hoy, pero no a ambos
# Harry visitó a Dumbledore hoy

# print(f"Rain: {model_check(knowledge, rain)}")
# print(f"Hagrid: {model_check(knowledge, hagrid)}")
# print(f"Dumbledore: {model_check(knowledge, dumbledore)}")
"""

SERVER_ROOM = Symbol("Server Room")
MEETING_ROOM = Symbol("Meeting Room")
EMPLOYEE_CARD = Symbol("Employee Card")
PIN_CODE = Symbol("Pin Code")
REGISTERD_VISTIOR = Symbol("Registered Visitor")
EMERGENCY_MODE = Symbol("Emergency Mode")
DOORS = Symbol("Doors")
INTRUDENT_ALERT = Symbol("Intrudent Alert")

knowledge.add(Implication(And(EMPLOYEE_CARD, PIN_CODE), SERVER_ROOM))

knowledge.add(Implication(Or(EMPLOYEE_CARD, REGISTERD_VISTIOR), MEETING_ROOM))

knowledge.add(Implication(REGISTERD_VISTIOR, Not(SERVER_ROOM)))

knowledge.add(Implication(EMERGENCY_MODE, And(DOORS, SERVER_ROOM, MEETING_ROOM)))

knowledge.add(Implication(INTRUDENT_ALERT, Not(EMERGENCY_MODE)))


knowledge.add(EMPLOYEE_CARD)
knowledge.add(Not(PIN_CODE))
knowledge.add(Not(EMERGENCY_MODE))
knowledge.add(INTRUDENT_ALERT)

print(f"Server Room: {model_check(knowledge, SERVER_ROOM)}")
print(f"Meeting Room: {model_check(knowledge, MEETING_ROOM)}")

"""

COLMUSTARD = Symbol("ColMustard")
PROFPLUM = Symbol("ProfPlum")
MSSCARLET = Symbol("MsScarlet")

BALLROOM = Symbol("Ballroom")
KITCHEN = Symbol("Kitchen")
LIBRARY = Symbol("Library")

KNIFE = Symbol("Knife")
REVOLVER = Symbol("Revolver")
WRENCH = Symbol("Wrench")

knowledge.add(Or(COLMUSTARD, PROFPLUM, MSSCARLET))
knowledge.add(Or(BALLROOM, KITCHEN, LIBRARY))
knowledge.add(Or(KNIFE, REVOLVER, WRENCH))

knowledge.add(Not(COLMUSTARD))
knowledge.add(Not(KITCHEN))
knowledge.add(Not(REVOLVER))
knowledge.add(Not(PROFPLUM))
knowledge.add(Not(BALLROOM))
knowledge.add(Or(Not(MSSCARLET), Not(LIBRARY), Not(WRENCH)))

print(f"Col Mustard: {model_check(knowledge, COLMUSTARD)}")
print(f"Prof Plum: {model_check(knowledge, PROFPLUM)}")
print(f"Ms Scarlet: {model_check(knowledge, MSSCARLET)}")
print(f"Ballroom: {model_check(knowledge, BALLROOM)}")
print(f"Kitchen: {model_check(knowledge, KITCHEN)}")
print(f"Library: {model_check(knowledge, LIBRARY)}")
print(f"Knife: {model_check(knowledge, KNIFE)}")
print(f"Revolver: {model_check(knowledge, REVOLVER)}")
print(f"Wrench: {model_check(knowledge, WRENCH)}")

resultado = "The criminal was: "
if model_check(knowledge, COLMUSTARD):
    resultado += "Col Mustard"
elif model_check(knowledge, PROFPLUM):
    resultado += "Prof Plum"
elif model_check(knowledge, MSSCARLET):
    resultado += "Ms Scarlet"
resultado += " in the: "
if model_check(knowledge, BALLROOM):
    resultado += "Ballroom"
elif model_check(knowledge, KITCHEN):
    resultado += "Kitchen"
elif model_check(knowledge, LIBRARY):
    resultado += "Library"
resultado += " with the: "
if model_check(knowledge, KNIFE):
    resultado += "Knife"
elif model_check(knowledge, REVOLVER):
    resultado += "Revolver"
elif model_check(knowledge, WRENCH):
    resultado += "Wrench"
print(resultado)