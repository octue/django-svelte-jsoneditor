#!/bin/zsh

# Install dependencies
poetry install

# Auto set up remote when pushing new branches
git config --global --add push.autoSetupRemote 1

# Allow precommit to install properly
git config --global --add safe.directory /workspace

# Install precommit hooks
pre-commit install && pre-commit install -t commit-msg

# Set zsh history location
#     This is done in postAttach so it's not overridden by the oh-my-zsh devcontainer feature
#
#     We leave you to decide, but if you put this into a folder that's been mapped
#     into the container, then history will persist over container rebuilds :)
#
#     !!!IMPORTANT!!!
#     Make sure your .zsh_history file is NOT committed into your repository, as it can contain
#     sensitive information. So in this case, you should add
#         .devcontainer/.zsh_history
#     to your .gitignore file.
export HISTFILE="/workspace/.devcontainer/.zsh_history"

# Add aliases to zshrc file
echo '# Aliases to avoid typing "python manage.py" repeatedly' >> ~/.zshrc
echo 'alias dj="python manage.py"' >> ~/.zshrc
echo 'alias djmm="python manage.py makemigrations"' >> ~/.zshrc
echo 'alias djm="python manage.py migrate"' >> ~/.zshrc
echo 'alias djr="python manage.py runserver"' >> ~/.zshrc
echo 'alias djreset="python manage.py reset_db -c"' >> ~/.zshrc
echo 'alias djs="python manage.py shell_plus"' >> ~/.zshrc
echo 'alias dju="python manage.py show_urls"' >> ~/.zshrc
