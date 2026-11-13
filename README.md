# GBA 6270 CI/CD Pipeline

A small Python project used to demonstrate a CI/CD pipeline:
GitHub push → webhook through ngrok → Jenkins (in Docker) runs the unit tests → result posted to a Webex space.

## Run the tests locally

```
python -m unittest -v
```
