# Django Project Setup with Pipenv and VS Code

This guide walks you through creating and running a Django project using `pipenv` for virtual environments and configuring everything inside Visual Studio Code.

---

## Step 1: Install and Set Up Django Environment

```bash
# Install pipenv if you haven't already
pip install pipenv

# Create a virtual environment and install Django
pipenv install Django

# Activate the virtual environment
pipenv shell

# Start a new Django project in the current directory (note the dot at the end)
django-admin startproject <projectname> .

## Step 2: Install and Set Up Django Environment
```bash
# View available Django admin commands
django-admin

# Start a new Django project in the current directory (note the dot at the end)
django-admin startproject <projectname> .

## Step 3: Create a Django App
```bash
python manage.py startapp <appname>

## Step 4: Run the Development Server
```bash
python manage.py runserver

