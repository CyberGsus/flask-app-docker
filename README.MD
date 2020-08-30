# flask-app-docker

This is a very simple example of an app that uses a mongo database.

## How to test it?

The routes are:

- `GET /` : Simple 'Hello World'
- `GET /people` : JSON with list of people added to a database
- `POST /people` : Add a person with a `name` and an `age` :

```json
{
  "name": "Jon Smith",
  "age": 34
}
```
