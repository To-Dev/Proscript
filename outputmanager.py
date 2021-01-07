from tabulate import tabulate

class outputmanager:
    
    def result(role_array, output_type = 'grid'):
        try:
            print(tabulate(role_array, ['Prosit', 'Animator', 'Secretary', 'Scribe', 'Timekeeper'], tablefmt = output_type))
        except:
            print("Printing error, wrong output parameter or corrupted result")

    def help():
        print("usage:\t./Proscript <prositnumber> -l <listfile> -o <outputtype>\n\t./Proscript -h\n")
        print("Prosit role dispenser script\n")
        print("positional arguments:\n  prositnumber\t\tThe number of prosits in your UE\n")
        print("optional arguments:")
        print("  -h, --help\t\tShow this help message and exit")
        print("  -l, --list=\t\tDefine the name of your group entry file, set to 'Team' by default")
        print("  -o, --output=\t\tChoose output format type, see tabulate pip package doc it use sames options")
