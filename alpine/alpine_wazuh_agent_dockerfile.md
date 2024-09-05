Source: [\Wazuh](https://www.reddit.com/r/Wazuh/comments/ywtgec/comment/iwv17wc/?utm_source=share&utm_medium=web2x&context=3)

**Docker**

```
# File: Dockerfile

FROM alpine:latest
RUN apk update && apk add make gcc automake autoconf libtool curl openssl openssl-dev libgcc cmake gnupg perl fakeroot brotli automake autoconf libtool gawk libsigsegv nodejs build-base python3 libc-dev gettext-dev zip procps --update alpine-sdk
RUN apk --no-cache add ca-certificates wget
RUN wget -q -O /etc/apk/keys/sgerrand.rsa.pub https://alpine-pkgs.sgerrand.com/sgerrand.rsa.pub
RUN wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.35-r0/glibc-2.35-r0.apk
RUN apk add --force-overwrite glibc-2.35-r0.apk
RUN apk add linux-headers && ln -s /usr/include/linux/a.out.h /usr/include/a.out.h
RUN wget https://github.com/wazuh/wazuh/archive/refs/heads/AlpineCompileForCommunity-4.3.10.zip
RUN unzip AlpineCompileForCommunity-4.3.10.zip
RUN cd wazuh-AlpineCompileForCommunity-4.3.10/src && make deps TARGET=agent EXTERNAL_SRC_ONLY=1
RUN addgroup -S wazuh && adduser -S wazuh
RUN cd wazuh-AlpineCompileForCommunity-4.3.10/src && make TARGET=agent
RUN cd wazuh-AlpineCompileForCommunity-4.3.10/ ./install.sh
```

**Alpine**

```
apk update && apk add make gcc automake autoconf libtool curl openssl openssl-dev libgcc cmake gnupg perl fakeroot brotli automake autoconf libtool gawk libsigsegv nodejs build-base python3 libc-dev gettext-dev zip procps --update alpine-sdk
apk --no-cache add ca-certificates wget
wget -q -O /etc/apk/keys/sgerrand.rsa.pub https://alpine-pkgs.sgerrand.com/sgerrand.rsa.pub
wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.35-r0/glibc-2.35-r0.apk
apk add --force-overwrite glibc-2.35-r0.apk
apk add linux-headers && ln -s /usr/include/linux/a.out.h /usr/include/a.out.h
wget https://github.com/wazuh/wazuh/archive/refs/heads/AlpineCompileForCommunity-4.3.10.zip
unzip AlpineCompileForCommunity-4.3.10.zip
cd wazuh-AlpineCompileForCommunity-4.3.10/src && make deps TARGET=agent EXTERNAL_SRC_ONLY=1
addgroup -S wazuh && adduser -S wazuh
cd wazuh-AlpineCompileForCommunity-4.3.10/src && make TARGET=agent
cd wazuh-AlpineCompileForCommunity-4.3.10/ ./install.sh
```
