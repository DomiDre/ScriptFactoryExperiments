from Experiment import Experiment
import os

class Experiment(Experiment):
    def error_help(self):
        print('')
        print('Usage TEHSIS factory: ScriptFactory.py THESIS MODE [additional arguments]')
        print('Available modes + additional arguments:')

        print('sem\t--\tTo make a snapshot of SEM image')
        print('\t--\ttiffile\t\t--\ttif file to load')
        print('\t--\tChapter\t--\tprefix of filename')
        print('\t--\tsampleName\t--\tsuffix of filename')
        
    def read_template(self):
        super().read_template()
