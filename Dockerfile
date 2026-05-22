FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY setup.py ./
COPY data_service ./data_service
COPY static ./static
COPY run_web_interface.py run_dashboard.py main.py ./

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -e .[web,visualization]

EXPOSE 8000 8501

CMD ["python", "-m", "uvicorn", "data_service.web.api_server:APIServer().app", "--host", "0.0.0.0", "--port", "8000"]
