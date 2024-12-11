import cmd
import os
import agent
import pandas as pd
from io import StringIO


my_agent = agent.myAgent()

class PandasAIDemo(cmd.Cmd):
    intro = 'Welcome to my PandasAI demo! Type help or ? to list commands.\n'
    prompt = '(PandasAIDemo) '

    def do_greet(self, line):
        """Greet command: greet [name]"""
        print("Hello,", line or "World")

    def do_exit(self, line):
        """Exit the program"""
        print("Goodbye!")
        return True  # Return True to exit the loop

    def do_append(self, line):
        """Append command: append [dir|file]"""
        if os.path.isdir(line):
            for file in os.listdir(line):
                if file.endswith(".csv"):
                    file_path = os.path.join(line, file)
                    my_agent.append_csv(file_path)
        else:
            my_agent.append_csv(line)

    def do_delete(self, line):
        """Delete command: delete [dir|file]"""
        if os.path.isdir(line):
            for file in os.listdir(line):
                if file.endswith(".csv"):
                    file_path = os.path.join(line, file)
                    my_agent.del_csv(file_path)
        else:
            my_agent.del_csv(line)

    def do_chat(self, line):
        """Chat command: chat"""
        print("Please enter a question:")
        question = input()
        response = my_agent.chat(question)
        print(f"[Response]: {response}")
        
    def do_chat_with_history(self, line):
        """Chat command: chat"""
        print("Please enter a question and we will answer it with chat history:")
        question = input()
        response = my_agent.chat_with_history(question)
        print(f"[Response]: {response}")

    def do_new_agent(self, line):
        """
        New agent command: new_my_agent [limit]
        Create a new agent with an optional history length limit.
        """
        try:
            if line == "":
                global my_agent
                my_agent = agent.myAgent()
            else:
                my_agent.new_my_agent(int(line))
            print("New agent created successfully")
        except ValueError:
            print("Please provide a valid number")
    
    def do_get_history(self, line):
        """
        Get history command: get_history
        Print the history of the agent.
        """
        print(my_agent.get_history())

    def do_export(self, line):
        """
        Export command: export
        export a new table
        """
        print("Please enter a cmd to export a new table:")
        question = input()
        response = my_agent.chat(question)
        print(f"[Response]: {response}")
        response = str(response)

        try:
            lines = response.strip().split('\n')
            header = lines[0]  # 第一行是列名
            data_lines = [line.split(maxsplit=1)[1] if i > 0 else line for i, line in enumerate(lines)]
            # 使用逗号连接每个字段
            cleaned_data_str = '\n'.join([','.join(line.split()) for line in data_lines])
            # 使用 StringIO 将清理后的字符串转换为文件对象
            data_file = StringIO(cleaned_data_str)

            # 使用 pandas 的 read_csv 函数读取数据
            df = pd.read_csv(data_file)
            df.to_csv("export.csv", index=False)

            print("Exported to export.csv successfully")
        except:
            print("Please provide a valid question")


if __name__ == '__main__':
    PandasAIDemo().cmdloop()

# Joining the people table with the country