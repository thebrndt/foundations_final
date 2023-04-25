# Project FliSP

This is a project for the Foundations Course at CODE. Spring 2023.

<hr>

## Project Description

FliSP is a project where people who live in shared flats and living spaces to share their stories, frustrations, tips and tricks for living with others.

<hr>

## Project Tech Stack

FliSP is built using various technologies that work together.

##### Frontend
> HTML, CSS, JavaScript
##### Backend
>Python, Flask, SQLite, SQLAlchemy
##### Deployment
>Postgres, render.com

<hr>

## Setup Instructions
Instructions assuming you have python installed on your device or system. If commands with prefix 'python' cause issues, you may want to specify a specific version to use in you commands (for example: 'python3 < command here >')

1. Clone the repository:
> https://github.com/thebrndt/foundations_final
2. Create a virtual environment in the directory
> python -m venv venv (or python3 -m venv venv)
3. Activate the virtual environment (venv)
> source venv/bin/acitve (or source venv\Scripts\activate on windows)
4. Install requirements
> pip install -r requirements.txt
5. Setup environment variables (.env)
> FLASK_DEBUG=True
DATABASE_URL=sqlite:///database.db
FLASK_APP=run.py
6. Run (either using gunicornn or python command)
> gunicorn:app (or python run.py)


<hr>

## Changelog (as of previous hand-in)

- Completely rebuilt project from scratch (fixing structural code issues)
- New and updated HTML and CSS with Javascript for interactivity and better responsiveness
- Backend logic for handling functions and operations (CRUD)
- Pagination funtionality as contents of databased increase, currently split by 4 items per page
- CRUD operates with databases and backend
- Deployed on a live site hosted on render.com (https://flisp.onrender.com/)

<hr>

## Previous Versions and Repositories

V 0.1 - Hand-in 1 - https://github.com/thebrndt/foundations_project
V 0.2 - Hand-ins 2-3 - https://github.com/thebrndt/foundations_flask
V 0.3 - Hand-in 5 - https://github.com/thebrndt/foundations_final _(current)_

<hr>

### Notes
- Currently no true login or session-based authentication system implemented
  - creating an account adds a new user (author) to the database
    - no email may be be the same
    - attempting to login would will create a new user and break the website (therefor disabled)
  - logging in only checks if email already exists in a page and redirects if true
- Anyone can post, however since every post must have an author, one must be selected from the list of authors who already exist
- 'Slugs' and the corresponding urls for articles are not consistent or uniform and users have to chose their own when posted (limited to 12 characters and cannot include spaces)
  - can technically include special characters but preferably not