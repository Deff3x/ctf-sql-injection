# CTF Project

This is a Capture The Flag (CTF) project built with Python and Flask. The application is a simple note-taking app with a twist.

## Table of Contents

- [CTF Project](README.md#ctf-project)
- [Project Structure](README.md#project-structure)
- [How to Run the Project](README.md#how-to-run-the-project)
- [Tips for the CTF Challenge](README.md#tips-for-the-ctf-challenge)

## Project Structure

- `app/`: Contains the main application code.
	- `app.py`: The main Flask application.
	- `flag.txt`: Contains the flag for the CTF challenge.
	- `requirements.txt`: Python dependencies for the project.
	- `templates/`: HTML templates for the Flask application.
- `docker-build.sh`: Shell script to build and run the Docker container.
- `Dockerfile`: Dockerfile for creating a Docker image of the application.
- `entrypoint.sh`: The entrypoint script for the Docker container.
- `README.md`: This file.

## How to Run the Project

Follow these steps to run the project:

1. Clone the project repository:
	```
	git clone https://github.com/your-username/your-repo.git
	```

2. Create the `flag.txt` file:
	- Navigate to the `app/` directory.
	- Create a new file named `flag.txt`.
	- Add the flag for the CTF challenge in the `flag.txt` file.
	- Alternatively, you can manually insert the flag into the INSERT query in `app.py`.

3. Build and run the Docker container:
	- Open a terminal and navigate to the project root directory.
	- Run the following command to build the Docker image:
	  ```
	  docker build -t ctf-project .
	  ```
	- Once the build is complete, run the Docker container:
	  ```
	  docker run -p 9374:9374 ctf-project
	  ```
	
	Alternatively, you can also run the Python project directly after installing the necessary dependencies. To do this, follow these steps:
	- Open a terminal and navigate to the project root directory.
	- Install the required dependencies by running the following command:
	  ```
	  pip install -r app/requirements.txt
	  ```
	- After the dependencies are installed, run the Python project using the following command:
	  ```
	  python -m flask run --host=0.0.0.0 --port=9374
	  ```

4. Access the application:
	- Open a web browser and go to `http://localhost:9374` to access the note-taking app.

That's it! You have successfully run the CTF project.

## Tips for the CTF Challenge

To approach the CTF challenge, you can consider exploring SQL injection vulnerabilities. SQL injection is a common web application vulnerability that allows an attacker to manipulate the application's database queries.

Here are some resources to help you understand and exploit SQL injection vulnerabilities:

- [OWASP SQL Injection](https://owasp.org/www-community/attacks/SQL_Injection)
- [SQL Injection Cheat Sheet](https://portswigger.net/web-security/sql-injection/cheat-sheet)
- [SQL Injection Payloads](https://github.com/payloadbox/sql-injection-payload-list)

Remember to always perform CTF challenges in a controlled environment and with proper authorization. Happy hacking!
