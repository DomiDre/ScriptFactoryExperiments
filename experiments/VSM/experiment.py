from Experiment import Experiment
import os

class Experiment(Experiment):
    def error_help(self):
        print('')
        print('Usage VSM factory: ScriptFactory.py VSM MODE [additional arguments]')
        print('Available modes + additional arguments:')

        print('guifit\t--\tUsing Qt5 + SliderApp + VSMModels + lmfit to fit VSMdata')
        print('\t--\tdatfile\t\t--\t.XYE file to load data from')
        print('\t--\tsavefile\t--\twhere to save fit results')

    def read_template(self):
        super().read_template()

        if self.mode == 'guifit':
            if self.Nargs > 1:
                print(self.template)

            print(self.template)