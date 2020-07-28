# Fourparts Web #
The deployment of the Fourparts package (https://github.com/ruixuantan/FourParts) on a site. \
Link to site: https://fourparts.herokuapp.com

To build project:
```
$ python3 setup.py bdist_wheel
$ docker-compose up --build
```

To configure postgres, open up a new terminal while the container is running and enter:
```
$ docker-compose run server fourpartsweb db init
```

Local build is on http://localhost:8000 \
Midi samples can be found here: https://github.com/ruixuantan/FourParts/tree/master/samples

## CLI ##
To run tests and flake8:
```
$ docker-compose exec server pytest
$ docker-compose exec server flake8
```

To delete storage files:
```
$ docker-compose run server fourpartsweb storage del-storage
```

## Deployment ##
### Heroku ###
Ensure set up of initial app and postgres add-on in Heroku. 
Add 1.the secret key, 2.heroku postgres db uri, 3.redis key to instance.settings.py file. 

In app.py, change `app.config.from_object('config.settings')` to `app.config.from_object('instance.settings')`

In Dockerfile and docker-compose.yml, change the command to `gunicorn "fourpartsweb.app:create_app()"`

## Notes ##
Currently, to avoid duplicates of filenames, when the midi file is uploaded, 
a python hash is generated from the concatenated string of the current datetime object
and original midi filename. This will then be used as the new filename of both midi and csv files.

## Next Steps ##
1. Write tests for CLI scripts and celery.
2. Configure webpack to precompile jquery functions or refactor to another javascript library (React).