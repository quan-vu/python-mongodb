# Quickstart MongoDB in Python

A quickstart with MongoDB in Python.

## Database

Start MongoDB server with docker:

```shell
docker run -d -p 27017:27017 --name mongodb mongo
```

## Test project

Create python virtual environment:

```shell
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.in
```

Run app:

```shell
python app.py
```

Result

```
{u'_id': ObjectId('5e4dec4dcc2af8e3fb82f287'), u'name': u'Quan Vu'}
```
