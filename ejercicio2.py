import random

class Mision:
    def __init__(self, tipo, planeta_destino, general):
        self.tipo = tipo
        self.planeta_destino = planeta_destino
        self.general = general
        self.prioridad = "alta" if general in ["Palpatine", "Darth Vader"] else "baja"
        self.recursos_asignados = []

    def asignar_recursos(self):
        if self.prioridad == "alta":
            return  # La asignación de recursos se realiza manualmente

        if self.tipo == "exploracion":
            self.recursos_asignados = ["Scout Trooper"] * 15 + ["speeder bike"] * 2
        elif self.tipo == "contencion":
            vehiculos = ["AT-AT", "AT-RT", "AT-TE", "AT-DP", "AT-ST"]
            self.recursos_asignados = (
                ["Stormtrooper"] * 30
                + [random.choice(vehiculos) for _ in range(3)]
            )
        elif self.tipo == "ataque":
            vehiculos = [
                "AT-AT", "AT-RT", "AT-TE", "AT-DP", "AT-ST", "AT-M6", "AT-MP", "AT-DT"
            ]
            self.recursos_asignados = (
                ["Stormtrooper"] * 50
                + [random.choice(vehiculos) for _ in range(7)]
            )

    def mostrar_recursos(self):
        print(f"Misión: {self.tipo} a {self.planeta_destino} - General: {self.general}")
        print(f"Prioridad: {self.prioridad}")
        print("Recursos asignados:")
        for recurso in self.recursos_asignados:
            print(f" - {recurso}")

misiones = []

# Ejemplo de uso

misiones.append(Mision("exploracion", "Tatooine", "General Kenobi"))
misiones.append(Mision("contencion", "Naboo", "Darth Vader"))
misiones.append(Mision("ataque", "Hoth", "Palpatine"))

for mision in misiones:
    mision.asignar_recursos()
    mision.mostrar_recursos()
    print("\n")
