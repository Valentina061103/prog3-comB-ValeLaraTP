from funcionesMutante import is_mutant

exit_app = "s"
while exit_app != "n":
    option = 0
    while option < 1 or option > 5:
        print(" Ingrese la opcion deseada: ")           #casos de prubea
        print("1 NUEVO MUTANTE")                        #Mutante: {ATTCGA}{ATTACT}{ATTCTG}{ATAAAG}{TTTGCA}{ATGGCC}
        print("2 Demostracion de un No mutante ")       #NO mutante: {AGTCAA}{GAAGTA}{TACGTA}{GGCTAG}{TGCTAG}{AAGGTG}
        option = int(input("Ingrese opción: "))
    if option == 1: #eleccion del usuario
        dna = [] #ingreso mutantes 
        for i in range(6):
            wordADN = ""
            letter_position = 1
            while len(wordADN) < 6:
                letterADN = input(f"Ingrese letra {letter_position} de la secuencia de ADN {i+1} (A, T, C, G): ").upper()
                if letterADN in ["A", "T", "C", "G"]:
                    wordADN += letterADN
                    letter_position+=1
                else:
                    print("Por favor, ingrese una letra entre las validas (A, T, C, G).")
            dna.append(wordADN)
            print(dna)

        is_mutants = "Es mutante." if is_mutant(dna) else "No es mutante."
        print(is_mutants)
    elif option == 2: #mostrar al usurio como se ve cuando no es mutante
        dna_not = [
            "ATGCGA", 
            "CAGTGC", 
            "TTGTGT", 
            "AGAAGG", 
            "CGACTA", 
            "TCACTG"]
        is_mutants = "Es mutante." if is_mutant(dna_not) else "No es mutante."
        print(is_mutants)
    exit_app = input("Desea ingresar otro ADN? Ingrese la letra 's' para si y la letra 'n' para no: ")
