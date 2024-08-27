# Easy Python Datetime
Dates are something stupidly difficult to handle sometimes. 

This project is intented to help people understand and handle easily dates and datetimes and string representation of dates in python.

It's just a bunch of functions and their tests to make sure they do what they are expected to do.

Right now, everything is expected to take UTC as the only valid format, and "%Y-%m-%dT%H:%M:%S.%fZ" the only valid string format to work with.

Feedback is welcome.
Hope you find it useful.

## Run it
```
pipenv install --dev
pipenv run python -m pytest
```