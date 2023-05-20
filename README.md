# Loan API using Django and DRF

[![codecov](https://codecov.io/gh/victoraugusto6/api-loan-django/branch/main/graph/badge.svg?token=9UIXZOAZ47)](https://codecov.io/gh/victoraugusto6/api-loan-django)

#### API made in Django and DRF to Loans and Payments.

### First Steps - Local Instalation

- create virtualenv using **[Poetry](https://python-poetry.org/docs/)**, run:

```commandline
poetry shell
```

- install dependencies with dev tools, run:

```commandline
poetry install --no-root --with dev --sync
```

- copy env-sample to .env, run:

```commandline
cp contrib/env-samplle .env
```

- create **[Docker](https://www.docker.com/)** container, run:

```commandline
docker compose up -d
```

- start Django server, run:

```commandline
python manage.py runserver
```

---

### 🛠 Tools used

| Package                  | Description                                                                                    |
|--------------------------|------------------------------------------------------------------------------------------------|
| **django**               | A high-level Python web framework for building robust and scalable web applications.           |
| **python-dotenv**        | A Python library that allows you to manage application-specific settings in a .env file.       | 
| **dj-database-url**      | A Django utility that allows you to configure the database connection using a URL.             |
| **gunicorn**             | A lightweight and efficient HTTP server for running Python web applications.                   |
| **psycopg2-binary**      | A PostgreSQL adapter for Python that enables interaction with PostgreSQL databases.            |
| **djangorestframework**  | A powerful and flexible toolkit for building RESTful APIs in Django.                           |
| **pytest-django**        | A plugin for the pytest testing framework that provides Django-specific features and fixtures. |
| **flake8**               | A code linter that checks Python code for style and potential errors.                          |
| **black**                | A highly opinionated code formatter for Python that enforces a consistent coding style.        |
| **isort**                | A Python library that automatically sorts and organizes import statements.                     |
| **pre-commit**           | A framework for managing and enforcing pre-commit hooks for code quality and formatting.       |
| **django-debug-toolbar** | A configurable panel for Django applications that displays useful debugging information.       |
| **model-bakery**         | A library for creating model instances in Django tests with minimal code.                      |
| **django-extensions**    | A collection of custom extensions and management commands for Django projects.                 |
| **pytest-cov**           | A plugin for pytest that generates code coverage reports during testing.                       |
