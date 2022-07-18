#!/bin/bash

docker-compose -f docker-compose.yml run myportfolio python -m unittest -v tests.test_db
docker-compose -f docker-compose.yml run myportfolio python -m unittest -v tests.test_app