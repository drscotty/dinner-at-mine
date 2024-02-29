#! /usr/bin/env bash

# Let the DB start
python ./dinneratmine/backend_pre_start.py

# Run migrations
alembic upgrade head    <---- ALEMBIC MIGRATION COMMAND

# Create initial data in DB
python ./dinneratmine/initial_data.py