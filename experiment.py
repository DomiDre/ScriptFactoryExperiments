import os

class Experiment():
    def __init__(self, parent, arguments, savepath):
        self.parent = parent
        self.arguments = arguments
        self.Nargs = len(self.arguments)
        self.savepath = savepath

    def check_assertion(self, cond, error_message):
        self.parent.check_assertion(cond, error_message, self.error_help)

    def read_template_file_to_template(self):
        self.template = []
        with open(self.template_file, 'r') as templatefile:
            for line in templatefile:
                self.template.append(line)

    def read_template(self):
        self.check_assertion(self.Nargs > 0,\
                'Script factory needs to have defined the template file name')

        self.mode = self.arguments[0]
        self.template_file = self.parent.experiment_path+'/'+\
                             self.mode+'.template'
        self.check_assertion(os.path.isfile(self.template_file),
                        'Template file '+self.template_file+' does not exist.')

        self.read_template_file_to_template()


    def error_help(self):
        print('')
        print('Usage script factory: ScriptFactory.py EXPERIMENT TEMPLATEFILE [additional arguments]')

    def save_template_to_file(self):
        savepath = self.savepath

        write_file = True
        if os.path.isfile(savepath):
            string_write_file = input('About to overwrite ' + savepath +\
                                          ' . Ok? [Y]')
            if not string_write_file.strip() in ['', 'y', 'Y', 'yes', 'Yes','YES',\
                                          'ok', 'j', 'J',]:
                write_file = False
        
        if not write_file:
            print('Aborted.')
            sys.exit()
        
        with open(savepath, 'w') as savefile:
            for message in self.parent.log.get():
                savefile.write(message+'\n')
            
            for line in self.template:
                savefile.write(line)