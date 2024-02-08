HOST_PORT=5001
CONTAINER_PORT=5000
APP_NAME=flask-api
TESTER_NAME=flask-api-tester
NETWORK_NAME=flask-api-net
VERBOSE ?= true

ifeq ($(VERBOSE),true)
    REDIRECT=
else
    REDIRECT=> /dev/null 2>&1
endif

# Build the Docker image for the Flask application
build:
	@docker build --target application -t $(APP_NAME) . $(REDIRECT)

# Run the Flask application container
run:
	@docker run -d -p $(HOST_PORT):$(CONTAINER_PORT) --name $(APP_NAME)-container $(APP_NAME) $(REDIRECT)

# Build the Docker image for the tester
test-build:
	@docker build --target tester -t $(TESTER_NAME) . $(REDIRECT)

# Execute tests against the running Flask application
test-run:
	# Run the tester container. Assumes the Flask application is accessible at host.docker.internal:5001
	docker run --rm $(TESTER_NAME) $(REDIRECT)

# Clean up Docker artifacts
clean:
	# Stop and remove the Flask application container if it's running
	@-docker stop $(APP_NAME)-container $(REDIRECT)
	@-docker rm $(APP_NAME)-container $(REDIRECT)

	# Remove the Docker images
	@-docker rmi $(APP_NAME) $(TESTER_NAME) $(REDIRECT)

	# Remove unused Docker networks (optional, be cautious if you have other networks you want to keep)
	@-docker network rm $(NETWORK_NAME) $(REDIRECT)

	# Clean up dangling images, containers, and networks
	@-docker system prune -f -a --volumes $(REDIRECT)
