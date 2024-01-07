# Contributing

## Where to start

The best place to start is by raising an issue on this repository (or identifying an existing issue and commenting there that you'll be working on it). If you need we can help you get started and sanity-check your approach.

## Developers Getting Started

To get started with developing `django-svelte-jsoneditor`, fork the repo then open an environment in the devcontainer (the easiest way is to use GitHub codespaces or VSCode remote containers), then type:

```
python manage.py migrate
python manage.py createsuperuser
# (then enter user details for yourself)
python manage.py runserver
# (then go to the localhost address in your browser)
# (and in another terminal...)
pytest
# (this should run all tests and have them pass)
```

You'll find this takes you to the django admin where you have several example models registered, each of which use slightly different options on the json field, so you can see how the widget behaves.

### About Svelte

**You don't need to know or care.** It's the JavaScript framework used to develop the widget - but the widget JS is all pre-built so there are no extra requirements.

## Commit messages

We use conventional commits, both to facilitate semantic version checking and to allow automatic generation of PR descriptions and release notes. This means:

- Your commit messages will be part of the release notes. Please keep your commit messages short (<72 characters) and descriptive of the change made in that commit.

- Please use the following [conventional commit codes](https://github.com/octue/conventional-commits#default-allowed-commit-codes)

- Breaking changes should be indicated by starting the body of the commit message with `BREAKING-CHANGE: <explain what users should do to migrate past the change`, eg you'd do:

```
git commit the_file_you_changed.py -m "FEA: New feature to do XYZ

BREAKING-CHANGE: To implement XYZ, we had to remove setting ABC. To update, users should remove setting ABC and replace it with setting PQR"
```

## Pre-Commit

We use [`pre-commit`](https://pre-commit.com/) to apply consistent code quality checks and linting to new code, commit messages, and documentation.

You need to install pre-commit to get the hooks working. Run:

```
pip install pre-commit
pre-commit install && pre-commit install -t commit-msg
```

Once that's done, each time you make a commit, [a range of checks](/.pre-commit-config.yaml) are made.

Upon failure, the commit will halt. **Re-running the commit will automatically fix most issues** except:

- The `flake8` checks... hopefully over time `black` (which fixes most things automatically already) will remove the need for it
- Docstrings - the error messages should explain how to fix these easily
- You'll have to fix documentation yourself prior to a successful commit (there's no auto fix for that!!)
- Commit messages - the error messages should explain how to fix these too

You can run pre-commit hooks without making a commit, too, like:

```
pre-commit run black --all-files
```

## Documentation

If you're unfamiliar with sphinx or reStructuredText, You can build html documentation using:

```
pre-commit run --all-files build-docs -v
```
