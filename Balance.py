def balance_combustion(hydrocarbon: str):
    import re
    from fractions import Fraction
    
    match = re.match(r'C(\d*)H(\d*)', hydrocarbon)
    if not match:
        raise ValueError("Formato incorrecto. Usa 'CxHy' como 'C3H8'")
    
    C_atoms = int(match.group(1)) if match.group(1) else 1
    H_atoms = int(match.group(2)) if match.group(2) else 1
    
    O2_atoms = (C_atoms * 2 + H_atoms // 2)
    O2_molecules = Fraction(O2_atoms, 2)
    
    equation = f"{C_atoms}C{H_atoms}H + {O2_molecules} O2 -> {C_atoms} CO2 + {H_atoms // 2} H2O"
    return equation

# Ejemplo de uso
hydrocarbon = "C3H8"  # Propano
equation = balance_combustion(hydrocarbon)
print(equation)

