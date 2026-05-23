FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY setup.py ./
COPY README.md ./
COPY data_service ./data_service
COPY static ./static
COPY examples ./examples
COPY tests ./tests
COPY run_web_interface.py run_dashboard.py main.py ./

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -e .[ai,visualization,realtime,web,test] && \
    pip install --no-cache-dir psycopg2-binary

EXPOSE 8000 8501

CMD ["python", "-m", "uvicorn", "data_service.web.api_server:app", "--host", "0.0.0.0", "--port", "8000"]
