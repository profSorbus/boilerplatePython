# Run the app using Docker

This file contains the instructions if you want to run this application using Docker.

You need to build the container first :

```sh
docker build -t boilerplate:latest .
```

Then, when the build is complete :

```sh
docker run -p 8000:8000 boilerplate:latest .
```
