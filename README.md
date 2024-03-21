# Pixagram: A Django-powered Instagram Clone

![Logo](logo.jpg)

Pixagram is a social media platform inspired by Instagram, built using the robust Django framework. It empowers users to:

- **Capture and share** captivating photos and videos with their network.
- **Unleash their creativity** with a suite of intuitive editing tools to enhance their content.
- **Explore a diverse and dynamic feed**, brimming with content from other users.
- **Engage and connect** through likes, comments, and follows, fostering a vibrant online community.

**Pixagram boasts:**

- **A user-friendly and aesthetically pleasing interface** for seamless navigation.
- **Effortless photo and video sharing capabilities** to capture and share your moments.
- **A comprehensive set of editing tools** to personalize your visual stories.
- **Engaging social features** to connect and interact with others.

**Embrace Pixagram as your platform to express yourself, connect with the world, and share your captivating visual journey.**

## Tech Stack
 
**Client:** HTML5, CSS3, JavaScript

**Server:** Django, postgresql

## Run Locally

Clone the project

```bash
  git clone git@github.com:SinhaAmrit/pixagram.git
```

Create virtual environment

```bash
  py -m venv venv (windows)
  python -m venv venv (Unix/MacOS)
```

Activate virtual environment

```bash
  venv\Scripts\activate.bat (windows)
  source venv/bin/activate (Unix/MacOS)
```

Go to the project directory

```bash
  cd ./pixagram
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Collect static files by running

```bash
  python manage.py collectstatic
```

Setup environment variables

```bash
  copy .env.copy .env (windows)
  cp .env.copy .env (Unix/MacOS)
```

To run this project, you will need to add the following environment variables to your .env file

`SECRET_KEY`  
`DB_ENGINE`  
`DB_HOST`  
`DB_NAME`  
`DB_USER`  
`DB_PASSWORD`  
`DB_PORT`  

Generate SECRET KEY by running

```bash
  python tools/generate_SECRET_KEY.py
```

Make migrations

```bash
  python manage.py migrate
```

Start the server

```bash
  python manage.py runserver
```

Open URL

```bash
  http://127.0.0.1:8000/
```

## Deployment

pixagram/settings.py

```bash
  ...
    DEBUG = False
  ...
```

run

```bash
  python manage.py collectstatic && python -m gunicorn pixagram.asgi:application -k uvicorn.workers.UvicornWorker
```

## Authors

- [@SinhaAmrit](https://github.com/SinhaAmrit)
- [@ydvXanurag](https://github.com/ydvXanurag)
- [@studentakanksha0810](https://github.com/studentakanksha0810)
- [@Ashutosh-Singh-Thakur](https://github.com/Ashutosh-Singh-Thakur)
