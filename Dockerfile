FROM python:3.12.11-bookworm
WORKDIR app/

COPY requirements.txt .
RUN pip install --no-cache-dir -r 'requirements.txt'

COPY . .

EXPOSE 5000

ENTRYPOINT ["flask"]
CMD ["--app", "app", "run", "--debug", "--host", "0.0.0.0", "--port", "5000"]