FROM python:slim

LABEL maintainer="or.zellinger@example.com"
LABEL description="Python Project In Server"

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "Server:app", "--host", "0.0.0.0", "--port", "8000"]
