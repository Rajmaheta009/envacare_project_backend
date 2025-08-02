# Docker Setup & Verification Guide

This guide explains how to install Docker, build and run your backend container, and verify everything is working.

## 1. Install Docker Desktop
- Download and install Docker Desktop from [https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/).
- Start Docker Desktop and ensure it is running.
- 
## System Requirements

To use WeasyPrint on Windows, install the GTK3 runtime:

1. Download the GTK3 Runtime for Windows:
   https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases

2. Install it to `C:\GTK3\` and make sure `C:\GTK3\bin` is added to your system PATH.

3. Restart your terminal before running the app.

## 2. Build the Docker Image
Open a terminal in your project directory and run:
```sh
docker build -t envacare-backend .
```
If the build completes without errors, your Dockerfile is correct.

## 3. Run the Docker Container
```sh
docker run -p 8000:8000 envacare-backend
```
This will start your backend server inside a Docker container.

## 4. Check if the Container is Running
- Open Docker Desktop and look for `envacare-backend` in the running containers list.
- Or run this command in your terminal:
  ```sh
  docker ps
  ```
  You should see `envacare-backend` listed.

## 5. Test the API
- Open your browser and go to: [http://localhost:8000/docs](http://localhost:8000/docs)
- If the documentation loads, your Docker setup is working perfectly.

## 6. Stop the Container
- In Docker Desktop, stop the running container.
- Or use the terminal:
  ```sh
  docker stop <container_id>
  ```
  Replace `<container_id>` with the actual ID from `docker ps`.
