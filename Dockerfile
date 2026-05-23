FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

ARG PRELOAD_NLP_MODELS=true

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

RUN if [ "$PRELOAD_NLP_MODELS" = "true" ]; then \
      python -m spacy download en_core_web_sm && \
      python -c "import nltk; from transformers import pipeline; [nltk.download(pkg) for pkg in ('punkt','stopwords','wordnet')]; pipeline('sentiment-analysis', model='cardiffnlp/twitter-roberta-base-sentiment'); print('Preloaded NLP assets')"; \
    fi

EXPOSE 8000 8501

CMD ["python", "-m", "uvicorn", "data_service.web.api_server:app", "--host", "0.0.0.0", "--port", "8000"]
