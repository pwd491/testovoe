```python
python3 main.py --help
```
```bash
usage: main.py [-h] [-U URL] [-T TRIES]

options:
  -h, --help         show this help message and exit
  -U, --url URL      URL address for benchmark
  -T, --tries TRIES  Number of requests
```

Example:
```bash
sergey@x79:~/Developer/testovoe$ python3 main.py
URL: https://filesamples.com/samples/image/jpeg/sample_5184%C3%973456.jpeg
Requests: 10
------------------------------------------------------------
Request 1/10: 1.292 sec | 5424.36 KiB | 4198.17 KiB/s
Request 2/10: 0.848 sec | 5424.36 KiB | 6399.42 KiB/s
Request 3/10: 3.658 sec | 5424.36 KiB | 1483.07 KiB/s
Request 4/10: 1.079 sec | 5424.36 KiB | 5025.72 KiB/s
Request 5/10: 0.784 sec | 5424.36 KiB | 6914.96 KiB/s
Request 6/10: 19.227 sec | 5424.36 KiB | 282.13 KiB/s
Request 7/10: 0.859 sec | 5424.36 KiB | 6311.98 KiB/s
Request 8/10: 21.064 sec | 5424.36 KiB | 257.52 KiB/s
Request 9/10: 0.976 sec | 5424.36 KiB | 5559.56 KiB/s
Request 10/10: 0.886 sec | 5424.36 KiB | 6125.56 KiB/s
------------------------------------------------------------
BENCHMARK RESULTS
Total requests: 10
Total downloaded: 52.97 MiB
Total time: 50.672 sec
Average request time: 5.067 sec
Average download speed: 1070.48 KiB/s
```