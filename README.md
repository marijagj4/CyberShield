# CyberShield

CyberShield is a Django-based educational web application designed to
raise awareness about bullying and cyberbullying among young people.

The platform helps users recognize harmful online behaviour, learn how
to respond safely, anonymously report cyberbullying situations, and
explore collected statistics.

## Live Application

The deployed application can be opened here:

**Live demo:** Add the Render link here after deployment.

Example:

`https://cybershield.onrender.com`

No Python installation is required to open and use the live application.

## Main Features

### Anonymous Cyberbullying Report

Users can submit an anonymous report by selecting:

- the type of cyberbullying;
- the platform where it happened;
- their age group;
- whether they asked someone for help;
- an optional anonymous description.

The form warns users not to enter names, usernames, phone numbers,
addresses, or other personal information.

### Cyberbullying Safety Quiz

The application contains interactive scenarios based on situations that
young people may experience online.

For every scenario, the user selects one of three possible responses.
After submitting the quiz, the application displays:

- whether the answer was correct;
- the safest response;
- an explanation of why that response is recommended.

### Statistics Dashboard

The dashboard displays anonymous statistics, including:

- the total number of submitted reports;
- reports grouped by cyberbullying type;
- reports grouped by online platform.

### Django Administration

An administrator can:

- add and manage quiz scenarios;
- review anonymous reports;
- filter reports by type, platform, age group, and help-seeking behaviour;
- view automatically updated report statistics.

## Target Group

The primary target group is young people, especially students between
11 and 15 years old.

The application is inspired by themes included in the HBSC study,
including bullying, cyberbullying, social support, emotional wellbeing,
and digital safety.

## Technologies

- Python
- Django
- HTML
- CSS
- JavaScript
- SQLite
- WhiteNoise
- Gunicorn
- Render
- Git and GitHub

## Project Structure

```text
CyberShield/
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── cyber_app/
│   ├── migrations/
│   ├── static/
│   │   └── cyber_app/
│   │       └── css/
│   │           └── style.css
│   ├── templates/
│   │   └── cyber_app/
│   │       ├── base.html
│   │       ├── home.html
│   │       ├── report_incident.html
│   │       ├── quiz.html
│   │       └── dashboard.html
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── signals.py
│   ├── urls.py
│   └── views.py
├── initial_data.json
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md