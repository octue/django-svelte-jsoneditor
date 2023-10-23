FROM windpioneers/gdal-python:modest-heron-gdal-2.4.1-python-3.11-dev

# Bust any pre-existing apt cache
#     Solves: https://askubuntu.com/questions/1388000/failed-to-fetch-deb-debian-org-debian-pool-main-l-linux-linux-libc-dev-5-10-70-1
# + Overcome the fact that yarn don't bother putting their keys on the ring (required for installing sshd feature)...
# https://github.com/yarnpkg/yarn/issues/7866#issuecomment-1404052064
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo gpg --dearmour -o "/usr/share/keyrings/yarn-keyring.gpg" & \
    echo "deb [signed-by=/usr/share/keyrings/yarn-keyring.gpg] https://dl.yarnpkg.com/debian stable main" | tee /etc/apt/sources.list.d/yarn.list & \
    gpg --refresh-keys & \
    apt-get update -y

# Install poetry
USER vscode
ENV POETRY_HOME=/home/vscode/.poetry
RUN curl -sSL https://install.python-poetry.org | python -
ENV PATH "$POETRY_HOME/bin:$PATH"
RUN poetry config virtualenvs.create false

# Install localtunnel
RUN npm install -g localtunnel
