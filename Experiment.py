import os, re, sys

class Experiment():
    def __init__(self, parent, arguments):
        self.parent = parent
        self.arguments = arguments
        self.Nargs = len(self.arguments)
        #arguments:
        #first one is mode, then x args can be given to replace arguments in template
        #last argument can be a .py file to use a template name

    def check_assertion(self, cond, error_message):
        self.parent.check_assertion(cond, error_message, self.error_help)

    def error_help(self):
        print('')
        print('Usage script factory: ScriptFactory.py EXPERIMENT TEMPLATEFILE [additional arguments]')

    def read_template(self):
        self.check_assertion(self.Nargs > 0,\
                'Script factory needs to have defined the template file name')

        self.mode = self.arguments[0]
        self.template_file = self.parent.experiment_path+'/'+\
                             self.mode+'.template'
        self.check_assertion(os.path.isfile(self.template_file),
                        'Template file '+self.template_file+' does not exist.')

        self.read_template_file_to_template()

    def read_template_file_to_template(self):
        self.template = []
        with open(self.template_file, 'r') as templatefile:
            for line in templatefile:
                self.template.append(line)

    def replace_arguments_in_template(self):
        
        arg_list = self.arguments[1:] # get all arguments except mode
        if len(arg_list) > 0:
            if arg_list[-1].endswith('.py'): # remove template file name if its included
                arg_list = arg_list[:-1]
            arg_list = arg_list[::-1] # inverse order to pop arguments from list

            variable_pattern = re.compile(r'{{[a-zA-Z0-9]*}}') # search for {{}} pattern
            for i, line in enumerate(self.template):
                if len(arg_list) == 0: # search is done if no more arguments are in list
                    break
                search_line_for_pattern = variable_pattern.search(line)
                if search_line_for_pattern is None:
                    continue
                else:
                    self.template[i] = line[:search_line_for_pattern.start()] +\
                                    arg_list.pop() +\
                                   line[search_line_for_pattern.end():]

    def save_template_to_file(self, savepath):
        self.savepath = savepath

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
