FROM python:3.10.9

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

ARG USER_ID=1000
ARG GROUP_ID=1000

RUN addgroup --gid $GROUP_ID user && \
    useradd --uid $USER_ID --gid $GROUP_ID -ms /bin/bash user && \
    apt-get update && apt-get install -y sudo && \
    echo "user ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/user && \
    chmod 440 /etc/sudoers.d/user

USER user


EXPOSE 80

CMD python manage.py runserver 0.0.0.0:8080
