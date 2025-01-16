def get_number(prompt):
    """Demande à l'utilisateur d'entrer un nombre."""
    # Pour l'instant, aucune validation des entrées n'est ajoutée.
    return input(prompt)

def get_operator():
    """Demande à l'utilisateur de choisir un opérateur."""
    # Aucun contrôle de validité des opérateurs pour le moment.
    return input("Entrez un opérateur (+, -, *, /) : ")

def calculate(a, b, operator):
    """Effectue l'opération de base entre deux nombres."""
    # Fonction non implémentée
    pass

def main():
    print("Bienvenue dans la calculatrice !")
    num1 = get_number("Entrez le premier nombre : ")
    operator = get_operator()
    num2 = get_number("Entrez le deuxième nombre : ")

    # Appelle la fonction de calcul (non implémentée)
    result = calculate(num1, num2, operator)

    print("Le résultat est :")  # Placeholder sans afficher de résultat.

if __name__ == "__main__":
    main()

