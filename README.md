# Concurrent Computing Performance

This project compares the performance of different concurrency models in handling HTTP GET and POST requests. The three models examined are:

- Multi-threading
- Multi-processing
- Asynchronous programming using coroutines

## Directory Structure
```commandline
.
├── WebApp
│   └── simple_web_app.py
└── compare.py
```


## Web Application

The web application is built using Flask and provides a simple API with the following endpoints:

- `GET /`: Returns a welcome message.
- `GET /api/data`: Returns a response after simulating a delay.
- `POST /api/data`: Accepts JSON data and returns it after a delay.

### Running the Web Application

1. Navigate to the `WebApp` directory:
   ```bash
   cd WebApp
   ```
2. Install Flask if you haven't already:
    ```bash
    pip install Flask
    ```
3. Run the web application:
    ``` bash
    python simple_web_app.py
    ```
   The application will be available at http://127.0.0.1:5000.

## Performance Comparison
The `compare.py` script benchmarks the three concurrency models against the web application.

Ensure the web application is running.

In a separate terminal, navigate to the project root directory:

```bash
cd path/to/ConcurrentComputingPerformance
```
Execute the performance comparison script:

``` bash
python compare.py
```

## Results
The script will output the time taken for each concurrency model to complete the requests, allowing you to compare their performance directly.
```
Time taken with threading: 5.050655364990234 seconds

Time taken with multiprocessing: 6.980526447296143 seconds

Time taken with asyncio: 3.007309675216675 seconds
```