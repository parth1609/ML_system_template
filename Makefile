PYTHON=python3

install:
	$(PYTHON) -m pip install -r requirements.txt

# Runs Black (code formatter)
# Runs isort (import sorter)
format:
	black app tests
	isort app tests

# Runs Flake8 for code style checking
lint:
	flake8 app tests

# Runs tests with verbose output
test:
	pytest -v

# Starts the FastAPI development server
run:
	uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Builds and runs Docker containers
docker-build:
	docker compose build

docker-up:
	docker compose up


# How tohow to use?
make install
make format	
make lint
make test
make run
make docker-build
make docker-up
