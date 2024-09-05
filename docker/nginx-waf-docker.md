To create an Nginx image with the ModSecurity module, you'd typically have to build Nginx from source and include the ModSecurity module during the build process. Here's an example `Dockerfile` that achieves this:

```Dockerfile
# Use a base image with a compilation environment
FROM debian:buster-slim as builder

# Set the versions for both Nginx and ModSecurity
ENV NGINX_VERSION=1.21.1 \
    MODSECURITY_VERSION=3.0.4

# Install build dependencies
RUN apt-get update && apt-get install -y \
    g++ \
    make \
    libpcre3-dev \
    zlib1g-dev \
    libssl-dev \
    libxml2-dev \
    libyajl-dev \
    pkgconf \
    libtool \
    git \
    wget

# Clone ModSecurity
RUN git clone --depth 1 -b v${MODSECURITY_VERSION} --single-branch https://github.com/SpiderLabs/ModSecurity \
    && cd ModSecurity \
    && git submodule init \
    && git submodule update \
    && ./build.sh \
    && ./configure \
    && make \
    && make install

# Install Nginx with ModSecurity
RUN wget http://nginx.org/download/nginx-${NGINX_VERSION}.tar.gz \
    && tar zxvf nginx-${NGINX_VERSION}.tar.gz \
    && cd nginx-${NGINX_VERSION} \
    && ./configure --with-compat --add-dynamic-module=../ModSecurity/nginx/modsecurity \
    && make modules

# Begin the final image
FROM nginx:${NGINX_VERSION}-alpine

# Copy over compiled ModSecurity module
COPY --from=builder /nginx-${NGINX_VERSION}/objs/ngx_http_modsecurity_module.so /etc/nginx/modules/

# Load the ModSecurity module in Nginx. Note: this makes Nginx load ModSecurity on startup
RUN echo "load_module modules/ngx_http_modsecurity_module.so;" > /etc/nginx/modules.conf \
    && cat /etc/nginx/nginx.conf > /etc/nginx/nginx.temp \
    && mv /etc/nginx/nginx.temp /etc/nginx/nginx.conf

# Setup ModSecurity
COPY --from=builder /usr/local/modsecurity /usr/local/modsecurity
COPY modsecurity.conf /usr/local/modsecurity/
COPY crs-setup.conf /usr/local/modsecurity/
COPY rules/ /usr/local/modsecurity/rules/

# Make sure permissions are set correctly
RUN chown -R nginx:nginx /usr/local/modsecurity/

# Use the default Nginx configuration (override this as necessary)
COPY nginx.conf /etc/nginx/nginx.conf

# Expose HTTP and HTTPS ports
EXPOSE 80 443

# Run Nginx in the foreground
CMD ["nginx", "-g", "daemon off;"]
```

Here's a brief rundown of what this Dockerfile does:

1. Uses a `builder` pattern with a compilation environment (`debian:buster-slim`).
2. Defines the versions of Nginx and ModSecurity to be installed.
3. Installs build dependencies.
4. Clones and builds ModSecurity from source.
5. Downloads and compiles Nginx with the ModSecurity module.
6. Creates the final image based on `nginx:${NGINX_VERSION}-alpine`.
7. Copies over the compiled ModSecurity module and sets up ModSecurity with default configurations. You might need to provide `modsecurity.conf`, `crs-setup.conf`, and your rules in the context where you're building this Dockerfile.
8. Loads the ModSecurity module in Nginx.
9. Sets up Nginx with a default configuration.

To build and use this image, you would:

1. Save the Dockerfile.
2. Provide the necessary ModSecurity configuration (`modsecurity.conf`, `crs-setup.conf`, and the rules in a `rules/` directory).
3. Build the image: `docker build -t nginx-modsec .`
4. Run a container from the image: `docker run -p 80:80 -p 443:443 nginx-modsec`

This is a basic example, and you might need to modify and enhance it to suit your exact requirements.
