from Experiment import Experiment
import os

class Experiment(Experiment):
    def error_help(self):
        print('')
        print('Usage SAXS factory: ScriptFactory.py SAXS MODE [additional arguments]')
        print('Available modes + additional arguments:')

        print('sphereplot\t--\tUsing matplotlib to plot data + fit')
        print('\t--\tsaxsdata\t\t--\t.XYEM file to load data & model from')
        print('\t--\tslddata\t--\t.XY file to load SLD from')
        print('\t--\tpngfile\t--\t.png where to store the plot')



