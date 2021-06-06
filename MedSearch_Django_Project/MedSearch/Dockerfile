FROM python:3.9
ENV PYTHONUNBUFFERED=1

WORKDIR /MedSearch

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY MedSearch .
CMD ["python", "MedSearch/manage.py", "runserver"]