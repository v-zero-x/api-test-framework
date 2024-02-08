# Flask API Project

This project demonstrates a Flask-based API with CRUD (Create, Read, Update, Delete) operations, encapsulated within Docker containers for an isolated and consistent development and testing environment. It's designed with simplicity in mind, offering a straightforward way to deploy and test a RESTful API. A significant aspect of this project is its development process, which was a collaboration between human creativity and AI-driven guidance, illustrating the potential of AI-assisted software engineering.

> Note from the human involved: ChatGPT did all the work, wrote the API [in one pass](chat.md), wrote all the files, including this entire README. I just ran the files on my macbook according to instructions and guided it through some debugging iterations. YMMV.
> 
> This is the GPT we used: [iterative-coding GPT](https://chat.openai.com/g/g-ZfQ1k76Cv-iterative-coding)

## Table of Contents

- [Project Overview](#project-overview)
- [Human-AI Partnership](#human-ai-partnership)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Building the Project](#building-the-project)
  - [Running the API](#running-the-api)
  - [Executing Tests](#executing-tests)
  - [Cleanup](#cleanup)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Project Overview

This Flask API project is a template for building and testing web APIs in a containerized environment. It features:

- A sample Flask application with CRUD endpoints to manage items.
- Docker configuration for easy setup and teardown.
- A testing framework using `pytest` to validate API functionality.
- Makefile commands to streamline the build, run, and test process.

## Human-AI Partnership

The development of this project was a unique journey that combined human problem-solving skills with AI-driven suggestions. Throughout this process:

- **Idea Generation**: AI provided initial outlines and ideas for setting up a Flask application within Docker, showcasing potential workflows.
- **Code Development**: Human creativity led the implementation, using AI suggestions to refine the codebase and troubleshoot issues.
- **Debugging and Optimization**: The partnership excelled in iterative debugging, with AI offering insights into error messages and proposing fixes.
- **Documentation**: AI helped draft documentation and guides, ensuring clarity and completeness.

This collaboration highlights the synergy between human developers and AI, pushing the boundaries of what can be achieved when both work together.

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:
- [Docker](https://docs.docker.com/get-docker/)
- [Make](https://www.gnu.org/software/make/) (usually pre-installed on Unix-like systems)

### Installation

To set up the project on your local machine:

```sh
git clone https://github.com/yourrepository/flask-api-project.git
cd flask-api-project
```

## Usage

### Building the Project

Build the Docker image for the Flask API:

```sh
make build
```

### Running the API

Start the API server in a Docker container:

```sh
make run
```

Access the API at `http://localhost:5001`. For example, [http://localhost:5001/items](http://localhost:5001/items)

### Executing Tests

Build the Docker image for testing and run the test suite against the API:

```sh
make test-build
make test-run
```

### Cleanup

Remove Docker artifacts created during the development and testing:

```sh
make clean
```

## Contributing

Contributions are welcome! Please fork the repository and submit pull requests with your enhancements. For major changes, open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

- Thanks to OpenAI for providing the AI-driven guidance that helped shape this project.
- Special thanks to all contributors and testers who provided feedback and suggestions.
