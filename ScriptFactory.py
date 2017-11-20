import numpy as np
import sys, os, datetime, glob, importlib
from Logger import Logger
from Experiment import Experiment

class ScriptFactory():
    def __init__(self):
        # Initialize global variables
        self.version = 0.1
        self.authors = [('Dominique Dresen', 'Dominique.Dresen@uni-koeln.de')]
        self.minimum_num_passed_args = 2
        self.log = Logger()

        self.run_factory()

    def run_factory(self):
        self.log_header()
        self.get_arguments()

        self.experiment_path = os.path.dirname(os.path.realpath(__file__))+\
                                '/experiments/'+self.arg_experiment
        print(self.experiment_path)
        self.check_assertion(os.path.isdir(self.experiment_path),\
                             'Specified experiment folder does not exist.')

        try:
            self.experiment = getattr(importlib.import_module('experiments.' +\
                                  self.arg_experiment + '.experiment'),\
                                  'Experiment')(self, self.additional_arguments,\
                                                self.save_template_to)
            self.log.comment('Using experiment.py from '+self.arg_experiment+' folder to generate script.')
        except ModuleNotFoundError:
            self.experiment = Experiment(self, self.additional_arguments,\
                                         self.save_template_to)
            self.log.comment('Using default experiment.py to generate file from template folder.')
        
        self.experiment.read_template()
        self.experiment.save_template_to_file()

    def log_header(self):
        self.log.comment('Initialized ScriptFactory v'+str(self.version))
        self.log.comment('Date: ' + str(datetime.datetime.now()))

        self.log.comment('Author(s)/Contact:')
        for author, mail in self.authors:
            self.log.comment(author + '\t ' + mail)
        self.log.log('')

    def get_arguments(self):
        self.passed_args = sys.argv
        self.N_passed_args = len(self.passed_args) - 1
        
        # At least 2 argument have to be passed
        self.check_assertion(self.N_passed_args >= self.minimum_num_passed_args,\
                             'Specify Experiment and Template')

        # Experiment folders are always uppercase
        self.arg_experiment = self.passed_args[1].upper()
        self.log.comment('Preparing Script for Experiment: ' + self.arg_experiment)
        self.additional_arguments = self.passed_args[2:]
        self.N_experiment_args = len(self.additional_arguments)


        if self.N_experiment_args >= 2 and self.additional_arguments[-1].endswith('.py'):
            self.save_template_to = self.additional_arguments[-1]
        else:
            self.save_template_to = self.arg_experiment+'_'+\
                                    self.passed_args[2]+'.py'

            check_savepath = input('Saving file to ['+self.save_template_to+\
                                   ']. Specify other filename or press ENTER.')
            if not check_savepath.strip() in ['', 'y', 'Y', 'yes', 'Yes','YES',\
                                          'ok', 'j', 'J',]:
                self.save_template_to = check_savepath

    def check_assertion(self, condition, err_message, child_func=None):
        try:
            assert(condition)
        except:
            if child_func is None:
                self.error_help()
            else:
                child_func()
            print('\nError:')
            print(err_message)
            sys.exit()


    def error_help(self):
        # print(" #####                                  #######")
        # print("#     #  ####  #####  # #####  #####    #         ##    ####  #####  ####  #####  #   #")
        # print("#       #    # #    # # #    #   #      #        #  #  #    #   #   #    # #    #  # #")
        # print(" #####  #      #    # # #    #   #      #####   #    # #        #   #    # #    #   #")
        # print("      # #      #####  # #####    #      #       ###### #        #   #    # #####    #")
        # print("#     # #    # #   #  # #        #      #       #    # #    #   #   #    # #   #    #")
        # print(" #####   ####  #    # # #        #      #       #    #  ####    #    ####  #    #   #")
        # print('')
        print('HELP')
        print('Usage: ScriptFactory.py EXPERIMENT TEMPLATEFILE [additional arguments]')


if __name__ == '__main__':
    sf = ScriptFactory()