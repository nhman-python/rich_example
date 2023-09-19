from rich.prompt import Prompt

name = Prompt.ask('enter your name', default='python')
print(name)