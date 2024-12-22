import pandas as pd
class CsvReader:
    def __init__(self, path, column=[]):
        self.df = pd.read_csv(path)
        self.df = self.df[column]
    def get_data(self):
        return self.df
    def get_group(self):
        return list(set([str(n[3]).split()[0] for n in self.df.values]))
    def search_data(self,name):
        return (list([[n[2],n[3]] for n in self.df.values if name in str(n[3])]))