# Flask Docker Application

This is a simple Flask application that displays "Hello from Flask" when accessed via a web browser. The application is containerized using Docker for easy deployment and portability.

## Prerequisites

Before running this application, ensure that you have the following prerequisites installed on your macOS machine:

- Docker Desktop: Install Docker Desktop for macOS from the official website: [https://www.docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop)

## Getting Started

Follow these steps to get the Flask application up and running using Docker:

1. Clone this repository to your local machine
2. Navigate to the project directory
3. Build the Docker image:

```
    docker build -t flask-app .
```

4. Run the Docker container:

```
    docker build -t flask-app .
```

This command will start the container and map port 5000 from the container to port 5000 on your host machine.

5. Access the application in your web browser:
   Open your web browser and visit `http://localhost:5000`. You should see the message "Hello from Flask" displayed.

## Troubleshooting

- If you encounter an error message stating that port 5000 is already in use, try running the container with a different port mapping:

```
    docker run -p 5001:5000 flask-app
```

Then, access the application at `http://localhost:5001`.

- If you face any issues related to dependencies or package versions, make sure that the `requirements.txt` file contains the correct dependencies and their compatible versions.

## Project Structure

The project structure is as follows:
|- app.py
|- Dockerfile
|- requirements.txt
|- README.md

- `app.py`: The main Flask application file that defines the route and handles the request.
- `Dockerfile`: The Dockerfile that specifies the instructions to build the Docker image.
- `requirements.txt`: The file that lists the required Python packages and their versions.
- `README.md`: This README file providing instructions and information about the project.

## Contributing

If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your modifications and commit your changes.
4. Push your changes to your forked repository.
5. Submit a pull request explaining your changes.
