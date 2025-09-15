# בסיס
FROM python:3.11-slim

# set working directory
WORKDIR /app

# העתק קבצי requirements והתקן תלותים
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y sqlite3 && rm -rf /var/lib/apt/lists/*

# העתק את כל הקוד
COPY . .

# חשיפה של פורט 5000
EXPOSE 5000

# הפקודה להרצת האפליקציה
CMD ["python", "run.py"]
