import pandas as pd

class RagApp:
    def __init__(self, filepath, sheet):
        self.filepath = filepath  # Removed comma to make it a single value
        self.sheet = sheet
        self.df = None  # Initialize df as None

    def open(self):
        print(f"Opening file: {self.filepath}, sheet: {self.sheet}")
        self.df = pd.read_excel(self.filepath, sheet_name=self.sheet)
        self.dm=self.df.to_markdown()
        return self.dm
    
    

