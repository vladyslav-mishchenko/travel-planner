FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# requirements
COPY requirements.txt /tmp/requirements/requirements.txt
RUN pip install -r /tmp/requirements/requirements.txt
RUN rm -rf /tmp/requirements

# entrypoint
COPY entrypoint.sh /usr/local/bin/entrypoints/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoints/entrypoint.sh

# project workdir
WORKDIR /app
COPY ./app /app

# user
ARG USERNAME=django
ARG USER_UID=1000
ARG USER_GID=$USER_UID
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    && apt-get update \
    && apt-get install -y sudo \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME
USER $USERNAME

ENTRYPOINT ["/usr/local/bin/entrypoints/entrypoint.sh"]

EXPOSE 8000
