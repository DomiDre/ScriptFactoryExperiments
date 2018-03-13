from Experiment import Experiment
import os

class Experiment(Experiment):
    def error_help(self):
        print('')
        print('Usage PPMS factory: ScriptFactory.py PPMS MODE [additional arguments]')
        print('Available modes + additional arguments:')

        print('hys\t--\tPlot hysteresis data')
        print('\t--\tdatfile\t\t--\t.XYE file to load data from')
        print('\t--\pngfilename\t--\twhere to save plot')

        print('temp\t--\tPlot temperature dependant data')
        print('\t--\tdatfile\t\t--\t.XYE file to load data from')
        print('\t--\pngfilename\t--\twhere to save plot')

    def read_template(self):
        super().read_template()
