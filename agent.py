from pandasai import Agent
import os
import pandas as pd

os.environ["PANDASAI_API_KEY"] = "$2a$10$KxglpkIOgEH2MfC.WiSlQuz4x7UiL7z0bDpZSczwQFSnxfj/I2wei"


class History():
    def __init__(self, limit=-1):
        self.limit = limit
        self.questions = []
        self.responses = []

    def appen_history(self, question, response):
        self.questions.append(question)
        self.responses.append(response)
        if self.limit != -1 and len(self.questions) > self.limit:
            self.questions.pop(0)
            self.responses.pop(0)

    def __str__(self) -> str:
        ret = "histories:{ "
        for idx, pr in enumerate(zip(self.questions, self.responses)):
            ret += f"{{question:{pr[0]}, response:{pr[1]}}}, "
        ret += " }"
        return ret
    

class myAgent():
    def __init__(self, history_limit=-1):
        self.dataframes = {}
        self.agent = None
        self.history = History(limit=history_limit)
        
    def append_csv(self, file_path_csv):
        if os.path.exists(file_path_csv) == False:
            print(f"Cannot find {file_path_csv}!!")
            return
        if file_path_csv not in self.dataframes.keys():
            self.dataframes[file_path_csv] = pd.read_csv(file_path_csv)
            self.agent = Agent(list(self.dataframes.values()))
            print(f"append {file_path_csv} successfully!")
        else:
            print(f"{file_path_csv} has already been loaded!")
            
    def del_csv(self, file_path_csv):
        if file_path_csv in self.dataframes.keys():
            self.dataframes.pop(file_path_csv)
            if len(self.dataframes.keys()) > 0:
                self.agent = Agent(list(self.dataframes.values()))
            else: 
                self.agent = None
            print(f"delete {file_path_csv} successfully!")
        else:
            print(f"{file_path_csv} has not been loaded!")

    def run(self, query):
        return self.agent.run(query)

    def chat(self, query):
        if self.agent == None:
            print("Please append csv files first!")
            return
        response = self.agent.chat(query)
        self.history.appen_history(query, response)
        return response
    
    def get_history(self):
        return self.history.__str__()

    def chat_with_history(self, query):
        if self.agent == None:
            print("Please append csv files first!")
            return
        query = f"{self.history.__str__()} query: {query}"
        response = self.agent.chat(query)
        self.history.appen_history(query, response)
        return response
    
if __name__ == "__main__":
    agent = myAgent()
    file_path_csv = 'csvs/revenue_by_country.csv'
    revenue_by_country = pd.read_csv(file_path_csv)
    agent.append_csv(file_path_csv)

    response = agent.chat("What is the revenue of China?")
    print(response)

    response = agent.chat("Plot the histogram of countries showing for each one the gd. Use different colors for each bar")

    file_path_csv = 'area_by_country.csv'
    area_by_country = pd.read_csv(file_path_csv)
    agent.append_csv(file_path_csv)

    file_path_csv = 'people.csv'
    people = pd.read_csv(file_path_csv)
    agent.append_csv(file_path_csv)

    print(response)