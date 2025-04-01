from sympy import symbols, Eq, solve

def balance_combustion(hydrocarbon: str):
    # Extrae la cantidad de átomos de C y H del hidrocarburo (asumiendo formato CxHy)
    import re
    match = re.match(r'C(\d*)H(\d*)', hydrocarbon)
    if not match:
        raise ValueError("Formato incorrecto. Usa 'CxHy' como 'C3H8'")
    
    C_atoms = int(match.group(1)) if match.group(1) else 1
    H_atoms = int(match.group(2)) if match.group(2) else 1
    
    # Definimos las incógnitas
    a, b, c, d = symbols('a b c d')
    
    # Ecuaciones basadas en la conservación de la materia
    eq1 = Eq(a, C_atoms)  # Carbono
    eq2 = Eq(2 * b, H_atoms)  # Hidrógeno
    eq3 = Eq(2 * c, a + 2 * d)  # Oxígeno
    
    # Resolver el sistema de ecuaciones
    solution = solve((eq1, eq2, eq3), (a, b, c))
    
    # Obtener coeficientes
    C_coef = solution[a]
    H_coef = solution[b]
    O2_coef = solution[c]
    CO2_coef = C_coef
    H2O_coef = H_coef
    
    return f"{hydrocarbon} + {O2_coef} O2 -> {CO2_coef} CO2 + {H2O_coef} H2O"

# Ejemplo de uso
hydrocarbon = "C3H8"  # Propano
equation = balance_combustion(hydrocarbon)
print(equation)
