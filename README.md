# Python Learning Bank - DevOps Project

This project is a **Banking Application** developed as part of my DevOps Engineer apprenticeship. The goal is to integrate multiple technologies and best practices to create a secure, scalable, and deployable application that demonstrates the core skills required for the apprenticeship.

---

## Project Overview

The **Python Learning Bank** is a web application that simulates basic banking operations, such as:

- Account creation and deletion
- User authentication (including email verification)
- Data handling with a MariaDB database
- Secure communication using SSL
- Dockerized containers for development and deployment

The project combines the knowledge I’ve gained throughout my apprenticeship in DevOps, cloud infrastructure, security, and continuous integration/deployment (CI/CD).

---

## Learning Outcomes & Skills Gained

### 1. **General Purpose Programming (Python)**

- **Duty**: Develop and maintain codebases, ensuring that they are efficient, secure, and maintainable.
- **KSBs**: Write clean, testable, and maintainable code in Python. Integrate Python with databases (MariaDB) and web frameworks (Django).
- **Learning Outcome**: Applied Python to develop the core functionality of the application, using Django as a framework to manage the backend. Integrated user authentication features and database operations.

### 2. **CI/CD Automation**

- **Duty**: Set up and maintain automated CI/CD pipelines to ensure that software is built, tested, and deployed efficiently and reliably.
- **KSBs**: Understand how to automate testing, building, and deployment using tools like GitHub Actions, Docker, and Jenkins.
- **Learning Outcome**: Integrated CI/CD pipelines for automatic deployment of code changes and feature updates using GitHub Actions. Dockerized the entire application to ensure that the project can be easily replicated across environments.

### 3. **Cloud Infrastructure & Automation (AWS)**

- **Duty**: Automate the deployment of infrastructure using cloud services.
- **KSBs**: Automate the provisioning of resources using Infrastructure as Code (IaC) tools, such as AWS CloudFormation or Terraform.
- **Learning Outcome**: Deployed the application on AWS, utilizing services like EC2 and RDS. Explored infrastructure as code with Terraform to provision cloud resources.

### 4. **Security & Compliance**

- **Duty**: Implement security measures to protect data and infrastructure.
- **KSBs**: Implement secure communication (SSL/TLS), use proper authentication and authorization mechanisms, and ensure that databases are securely configured.
- **Learning Outcome**: Ensured secure communication using SSL certificates. Applied encryption at rest for sensitive data in the MariaDB database. Used secure authentication practices (e.g., JWT tokens) to protect user information.

### 5. **Containerization & Orchestration**

- **Duty**: Build and manage containerized environments for applications.
- **KSBs**: Use Docker to containerize applications and Kubernetes for orchestration of containers.
- **Learning Outcome**: Dockerized the backend and frontend components of the application. Explored Kubernetes as a container orchestration tool for scaling and managing the application in the future.

### 6. **Monitoring & Logging**

- **Duty**: Implement monitoring and logging to track the performance and health of applications and infrastructure.
- **KSBs**: Use monitoring tools like Prometheus, Grafana, and AWS CloudWatch for visibility into system performance.
- **Learning Outcome**: Set up basic logging and monitoring functionality, allowing for real-time performance tracking and troubleshooting. Planned future integration with tools like Prometheus and Grafana.

### 7. **Collaboration and Agile Practices**

- **Duty**: Collaborate with stakeholders and team members to ensure that software is delivered iteratively and continuously.
- **KSBs**: Understand Agile methodologies and use project management tools to manage progress.
- **Learning Outcome**: Worked iteratively on project features, collaborating effectively with project stakeholders. Applied Agile practices using Jira for task management.

---

## Project Structure

python-learning-bank/
│
├── AIQ/ # Django project directory
│ ├── asgi.py # ASGI configuration for asynchronous handling
│ ├── settings.py # Project settings and configuration
│ ├── urls.py # URL routing for the project
│ ├── wsgi.py # WSGI configuration for synchronous handling
│ └── **init**.py # Mark the directory as a Python package
│
├── manage.py # Django project management command-line utility
├── requirements.txt # List of Python dependencies
├── .gitignore # Files and directories to ignore by Git
└── venv/ # Virtual environment for Python dependencies

---

## Key Technologies Used

- **Django**: Backend framework for handling business logic, user authentication, and database operations.
- **MariaDB**: Relational database for storing user and transaction data.
- **Docker**: Containerization tool to isolate the application’s dependencies and environments.
- **GitHub Actions**: CI/CD automation for building, testing, and deploying code.
- **AWS**: Cloud provider for hosting the application and database.
- **SSL**: Secure communication protocol for encrypting data between the client and server.
- **Cloudflare**: DNS and security service to ensure fast and secure access to the application.

---

## Next Steps

1. **Complete API Integration**: Extend the application with RESTful APIs to allow for better interaction between the frontend and backend.
2. **Kubernetes Orchestration**: Deploy the containerized application on Kubernetes for better scalability and management.
3. **Automate Infrastructure**: Use Infrastructure as Code (IaC) tools like Terraform to automate AWS resource provisioning.
4. **Advanced Security Practices**: Implement additional security features, such as OAuth2 for authentication, and explore the use of web application firewalls (WAFs).

---

## Conclusion

This project provides an opportunity to apply and build upon the key skills necessary to become a proficient DevOps Engineer. By focusing on automation, cloud infrastructure, security, containerization, and monitoring, I am gaining hands-on experience with tools and technologies that are essential for managing modern software applications.
