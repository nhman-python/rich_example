from rich.table import Table
from rich.console import Console


def example_table(users: list):
    console = Console()
    table = Table(title='this is my database!')
    table.add_column('name', style='cyan')
    table.add_column('age', style='blue')
    table.add_column('email', style='red')

    for user in users:
        table.add_row(user[0], user[1], user[2])
    console.print(table)


user1 = ['python', '10', 'python@gmail.com']
user2 = ['israel', '70', 'israel@gmail.com']
user3 = ['apt_update', '30', 'test@gmail.com']
example_table([user1, user2, user3])
