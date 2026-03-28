FROM python:3.11.4-slim

# Prevent Python from writing .pyc files and force stdout/stderr flushing
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Install Python dependencies first for better layer caching
COPY requirements.txt ./
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy application source
COPY . .

# Create and use a non-root user
RUN adduser --disabled-password --gecos "" appuser \
    && chown -R appuser:appuser /app
USER appuser

# Default port used by many container platforms
EXPOSE 8080

# Run with gunicorn and support platform-provided PORT env var
CMD ["sh", "-c", "gunicorn --bind 0.0.0.0:${PORT:-8080} app:app"]
