# Overcast development container
FROM ubuntu:20.04

# Update packages and install required dependencies
RUN apt-get update && \
    apt-get install -y curl python3 python3-pip && \
    apt-get install -y git

# Install any additional packages or tools needed for your project
RUN pip install django

# Set the working directory inside the container
WORKDIR /workspace

# Default command to run (modify as needed)
CMD ["/bin/bash"]
