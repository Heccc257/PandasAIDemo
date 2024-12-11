import cmd
import os
import agent

my_agent = agent.myAgent()

class PandasAIDemo(cmd.Cmd):
    intro = 'Welcome to my PandasAI demo! Type help or ? to list commands.\n'
    prompt = '(myapp) '

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

if __name__ == '__main__':
    PandasAIDemo().cmdloop()