"""The simple HTTP/HTTPS Benchmark"""

import time
import argparse
import urllib.request as urequest
import urllib.error as uerror

argp = argparse.ArgumentParser()
argp.add_argument(
    "-U",
    "--url",
    help="URL address for benchmark",
    default="https://filesamples.com/samples/image/jpeg/sample_5184%C3%973456.jpeg",
)
argp.add_argument(
    "-T",
    "--tries",
    type=int,
    help="Number of requests",
    default=10,
)
args = argp.parse_args()

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36",
    "Accept": "*/*",
    "Accept-Encoding": "identity",
    "Connection": "keep-alive",
}


class Benchmark:

    def __init__(self, url: str = args.url, tries: int = args.tries) -> None:
        self.url = url
        self.total_time = 0.0
        self.total_bytes = 0
        self.tries = tries

    def request(self, number: int) -> None:
        start_time = time.perf_counter()
        downloaded_bytes = 0

        req = urequest.Request(
            self.url,
            headers=headers,
            method="GET",
        )

        try:
            with urequest.urlopen(req, timeout=15) as response:
                while True:
                    chunk = response.read(8192)

                    if not chunk:
                        break

                    downloaded_bytes += len(chunk)

            elapsed = time.perf_counter() - start_time

            self.total_time += elapsed
            self.total_bytes += downloaded_bytes

            speed = downloaded_bytes / elapsed / 1024

            print(
                f"Request {number}/{self.tries}: "
                f"{elapsed:.3f} sec | "
                f"{downloaded_bytes / 1024:.2f} KiB | "
                f"{speed:.2f} KiB/s"
            )

        except (uerror.URLError, TimeoutError, uerror.HTTPError) as error:
            print(f"Request {number} failed: {error}")
            raise

    def run(self) -> None:
        print(f"URL: {self.url}")
        print(f"Requests: {self.tries}")
        print("-" * 60)

        for number in range(1, self.tries + 1):
            self.request(number)

        self.report()

    def report(self) -> None:
        average_time = self.total_time / self.tries
        average_speed = self.total_bytes / self.total_time / 1024

        print("-" * 60)
        print("BENCHMARK RESULTS")
        print(f"Total requests: {self.tries}")
        print(f"Total downloaded: {self.total_bytes / 1024 / 1024:.2f} MiB")
        print(f"Total time: {self.total_time:.3f} sec")
        print(f"Average request time: {average_time:.3f} sec")
        print(f"Average download speed: {average_speed:.2f} KiB/s")


if __name__ == "__main__":
    benchmark = Benchmark()
    benchmark.run()
