from rich.console import Console
import time

console = Console()
with console.status("example spinner..."):
    for num in range(10):
        print(f'this is example text hello number {num}')
        time.sleep(1)
print('done')
