from Logger import Logger
from Experiment import Experiment

import numpy as np
import sys, os, datetime, glob, importlib

class ScriptFactory():
  def __init__(self):
    # Initialize global variables
    self.version = 0.2
    self.authors = [('Dominique Dresen', 'Dominique.Dresen@uni-koeln.de')]
    self.log = Logger()

    self.run_factory()

  def run_factory(self):
    self.log_header() #Initialize header and put into log

    self.get_arguments() # Get arguments from CL as well as the savepath

    # Generate Experiment object.
    self.experiment = Experiment(self, self.additional_arguments)

    # Read desired template and save to file
    self.experiment.read_template()

    # Read or generate a name for the saved script.
    self.create_savefile_name()

    # Replace {{}} args in template with additionally given arguments
    self.experiment.replace_arguments_in_template()

    self.experiment.save_template_to_file(self.save_template_to)

  def log_header(self):
    # Generate a header included in generated script
    self.log.comment('Initialized ScriptFactory v'+str(self.version))
    self.log.comment('Date: ' + str(datetime.datetime.now()))

    self.log.comment('Author(s)/Contact:')
    for author, mail in self.authors:
      self.log.comment(author + '\t ' + mail)
    self.log.log('')

  def get_available_experiments(self):
    print('Available Experiments are:')
    avail_experiments = os.listdir(
      os.path.dirname(os.path.realpath(__file__))+'/experiments/')
    for exp in avail_experiments:
     print('\t'+exp)

  def get_available_templates(self):
    print('Available Templates are:')
    available_files = os.listdir(self.experiment_path)
    available_templates = []
    for f in available_files:
      if f.endswith('.template'):
        available_templates.append(f.split('.template')[0])
    for template in available_templates:
     print('\t'+template)


  def get_arguments(self):
    # Get arguments from CL
    self.passed_args = sys.argv
    self.N_passed_args = len(self.passed_args) - 1
    # At least 2 argument have to be passed
    self.check_assertion(self.N_passed_args >= 1,\
      'Specify Experiment and Template', self.get_available_experiments)

    # Experiment folders are always uppercase
    self.arg_experiment = self.passed_args[1].upper()
    self.experiment_path = os.path.dirname(os.path.realpath(__file__))+\
      '/experiments/'+self.arg_experiment

    self.check_assertion(os.path.isdir(self.experiment_path),\
      'Specified experiment folder does not exist.', self.get_available_experiments)

    self.log.comment('Preparing Script for Experiment: ' +\
             self.arg_experiment)

    self.check_assertion(self.N_passed_args >= 2,\
      "You didn't specify a template", self.get_available_templates)

    self.additional_arguments = self.passed_args[2:]
    self.N_experiment_args = len(self.additional_arguments)

  def create_savefile_name(self):
    # If name for saving is given as last argument use this one
    if self.N_experiment_args >= 2 and\
        self.additional_arguments[-1].endswith('.py'):
      self.save_template_to = self.additional_arguments[-1]

    # Otherwise propose one from experiment & template name
    else:
      self.save_template_to = self.arg_experiment+'_'+\
                  self.passed_args[2]+'.py'

      # Ask if that is ok. User can otherwise propose his own.
      check_savepath = input('Saving file to ['+self.save_template_to+\
                   ']. Specify other filename or just press ENTER: ')
      if not check_savepath.strip() in ['', 'y', 'Y', 'yes', 'Yes','YES',\
                      'ok', 'j', 'J',]:
        if not check_savepath.endswith('.py'): #Savefile must be a python file
          check_savepath = check_savepath+'.py'
        self.save_template_to = check_savepath

  def check_assertion(self, condition, err_message, child_func=None):
    # Help method to check if conditions are fulfilled. Otherwise exit with error message
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
    # Message which is posted in case of an error
    print('Usage: ScriptFactory.py EXPERIMENT TEMPLATEFILE [additional arguments]')

if __name__ == '__main__':
  sf = ScriptFactory()