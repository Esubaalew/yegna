# Multi-stage build for optimized production image
FROM python:3.11-alpine AS builder

# Set work directory
WORKDIR /app

# Create virtual environment
RUN python3 -m venv venv
ENV VIRTUAL_ENV=/app/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install build dependencies
RUN apk add --no-cache gcc musl-dev libffi-dev

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Production image
FROM python:3.11-alpine AS runner

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV VIRTUAL_ENV=/app/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
ENV PORT=8000

# Set work directory
WORKDIR /app

# Copy virtual environment from builder stage
COPY --from=builder /app/venv venv

# Copy project files
COPY . /app/

# Create staticfiles directory and collect static files
RUN mkdir -p /app/staticfiles

# Make entrypoint script executable
RUN chmod +x /app/docker-entrypoint.sh

# Create non-root user for security
RUN adduser --disabled-password --gecos '' appuser && \
    chown -R appuser:appuser /app
USER appuser

# Expose port
EXPOSE ${PORT}

# Set entrypoint to handle database setup
ENTRYPOINT ["/app/docker-entrypoint.sh"]

# Run the application
CMD ["gunicorn", "--bind", ":8000", "--workers", "2", "yegna_portfolio.wsgi:application"]
