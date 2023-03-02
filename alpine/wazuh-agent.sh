#!/bin/bash

# curl -s https://raw.githubusercontent.com/fabriziosalmi/linux/master/alpine/wazuh-agent.sh | bash -s

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
