# Use the official PostgreSQL image from the Docker Hub
FROM postgres:12.18-bullseye

# Update the package lists and install Vim
RUN apt-get update && apt-get install -y vim 

# Clean up the cache to reduce layer size
RUN apt-get clean && rm -rf /var/lib/apt/lists/*
