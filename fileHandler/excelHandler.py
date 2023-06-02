import pandas as pd


class Filehandler:
    file_path = ""
    
    def __init__(self, file_path):
        self.file_path = file_path
    
    
    def xlsxHandler(self):
        project_data = pd.read_excel(self.file_path)
        
        return project_data
    
    
    def project50Handler(self):
        project_data = pd.read_excel(self.file_path)
        
        project50 = project_data[:50]
        project50_excel = project50.to_excel("halfData.xlsx", index = False)
        return project50_excel 
        
         