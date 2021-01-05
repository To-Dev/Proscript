import sys, getopt

class arghandler:
    
    short_options = "l:o:h"
    long_options = ["list=", "output=", "help",]
    ask_for_help = False
    list_path = 'Team'
    output_type = 'grid'
    
    def __init__(self, argv):
        self.load_args(argv)
        self.hydrate_options()
        
    def load_args(self, argv):
        try:
            self.opts, self.args = getopt.gnu_getopt(argv, self.short_options, self.long_options)
        except getopt.GetoptError:
            print('Bad usage of the command please read the manual "./Proscript -h"')
            sys.exit(2)

    def hydrate_options(self):
        for o, a in self.opts:
            if o in ("-h", "--help"):
                self.enable_help_flag()
            elif o in ("-l", "--list"):
                self.list_path = a
            elif o in ("-o", "--output"):
                self.output_type = a
            else:
                assert False, "unhandled option"
                
    def handle_prosit_nb(self):
        try:
            return int(self.args[0])
        except:
            print('Prosit number is not actually a number please enter a valid one')
            sys.exit(2)
                    
    def enable_help_flag(self):
        self.ask_for_help = True
