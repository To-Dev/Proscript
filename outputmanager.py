from tabulate import tabulate

class outputmanager:
    
    def result(role_array, output_type = 'grid'):
        try:
            print(tabulate(role_array, ['Prosit', 'Animateur', 'Secretaire', 'Scribe', 'Gestionnaire'], tablefmt = output_type))
        except:
            print("Printing error, wrong output parameter or corrupted result")

    def help():
        print("./Proscript <prositnumber> -l <listfile> -o <outputtype>")
