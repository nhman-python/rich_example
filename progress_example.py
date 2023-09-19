from rich.progress import Progress
import httpx


def patch_url(url: str, num_request: int):
    with Progress() as progress:
        task = progress.add_task('example progress request!', total=num_request)
        for i in range(num_request):
            print(httpx.get(url))
            progress.update(task, advance=1)
        print('done progress')


if __name__ == '__main__':
    patch_url('https://example.com', 3)
