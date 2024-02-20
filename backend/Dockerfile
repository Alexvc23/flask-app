FROM python:3.12.2-bullseye

WORKDIR /app

COPY ./* /app/

# Make sure pip is updated and install requirements
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

ENV FLASK_APP=App.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=development


# CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "App:app"]
CMD flask  --app App run
