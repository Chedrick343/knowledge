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