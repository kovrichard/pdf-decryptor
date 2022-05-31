.PHONY: start stop build sh logs restart config test lint

# \
!ifndef 0 # \
test_env="UPLOAD_FOLDER=$$TEST_UPLOAD_FOLDER" # \
!else
test_env=UPLOAD_FOLDER=\$$TEST_UPLOAD_FOLDER
# \
!endif

container=pdf_decryptor

# start all the containers
start:
	docker-compose up -d

# stop all the containers
stop:
	docker-compose down

# restart containers
restart: stop start

# build the app container
build:
	docker-compose build

# get a shell within the app container
sh:
	docker-compose exec $(container) /bin/sh

# check console output
logs:
	docker-compose logs -f

# show the combined compose file used
config:
	docker-compose config

test:
	docker-compose exec -T $(container) /bin/sh -c "$(test_env) poetry run nose2 -v"

# lint code
lint:
	docker-compose exec $(container) poetry run autoflake --remove-all-unused-imports --ignore-init-module-imports --in-place --recursive pdf_decryptor tests
	docker-compose exec $(container) poetry run isort pdf_decryptor tests
	docker-compose exec $(container) poetry run black pdf_decryptor tests
