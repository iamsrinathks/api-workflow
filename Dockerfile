# Use a base image that provides Debian-based Linux.
FROM debian:bullseye-slim

# Set environment variables to suppress APT warnings and set non-interactive mode.
ENV DEBIAN_FRONTEND=noninteractive
ENV APT_KEY_DONT_WARN_ON_DANGEROUS_USAGE=DontWarn

# Update and install required packages.
RUN apt-get update && apt-get install -y \
    postgresql-client \
    vim \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Create a directory for your application and copy a "Hello, World" script.
WORKDIR /app
COPY hello-world.sh /app/hello-world.sh

# Make the script executable.
RUN chmod +x /app/hello-world.sh

# Set the entry point for the container.
CMD ["/app/hello-world.sh"]
