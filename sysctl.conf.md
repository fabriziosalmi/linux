**/etc/sysctl.conf**

```
fs.file-max = 2097152
fs.protected_hardlinks = 0
fs.protected_symlinks = 0
net.core.dev_weight = 64
net.core.netdev_max_backlog = 16384
net.core.optmem_max = 25165824
net.core.optmem_max = 65535
net.core.rmem_default = 31457280
net.core.rmem_max = 12582912
net.core.rmem_max = 16777216
net.core.somaxconn = 65535
net.core.wmem_default = 31457280
net.core.wmem_max = 12582912
net.core.wmem_max = 16777216
net.ipv4.conf.all.accept_redirects = 0
net.ipv4.conf.all.accept_source_route = 0
net.ipv4.conf.all.log_martians = 1
net.ipv4.conf.all.rp_filter = 1
net.ipv4.conf.all.send_redirects = 0
net.ipv4.conf.default.rp_filter = 1
net.ipv4.ip_local_port_range = 2000 65535
net.ipv4.neigh.default.gc_interval = 30
net.ipv4.neigh.default.gc_thresh1 = 32
net.ipv4.neigh.default.gc_thresh2 = 1024
net.ipv4.neigh.default.gc_thresh3 = 2048
net.ipv4.neigh.default.proxy_qlen = 96
net.ipv4.neigh.default.unres_qlen = 6
net.ipv4.route.flush = 1
net.ipv4.tcp_ecn = 1
net.ipv4.tcp_fin_timeout = 15
net.ipv4.tcp_keepalive_intvl = 15
net.ipv4.tcp_keepalive_probes = 5
net.ipv4.tcp_keepalive_time = 300
net.ipv4.tcp_max_orphans = 16384
net.ipv4.tcp_max_syn_backlog = 4096
net.ipv4.tcp_max_tw_buckets = 1440000
net.ipv4.tcp_mem = 65536 131072 262144
net.ipv4.tcp_moderate_rcvbuf = 1
net.ipv4.tcp_no_metrics_save = 1
net.ipv4.tcp_orphan_retries = 0
net.ipv4.tcp_reordering = 3
net.ipv4.tcp_retries1 = 3
net.ipv4.tcp_retries2 = 15
net.ipv4.tcp_rfc1337 = 1
net.ipv4.tcp_rmem = 8192 87380 16777216
net.ipv4.tcp_slow_start_after_idle = 0
net.ipv4.tcp_synack_retries = 2
net.ipv4.tcp_syncookies = 1
net.ipv4.tcp_tw_recycle = 0
net.ipv4.tcp_tw_recycle = 1
net.ipv4.tcp_tw_reuse = 1
net.ipv4.tcp_wmem = 8192 65536 16777216
net.ipv4.udp_mem = 65536 131072 262144
net.ipv4.udp_rmem_min = 16384
net.ipv4.udp_wmem_min = 16384
net.ipv6.conf.all.accept_redirects = 0
net.ipv6.conf.all.accept_source_route = 0
net.ipv6.route.flush = 1
net.unix.max_dgram_qlen = 50
vm.dirty_background_ratio = 2
vm.dirty_ratio = 60
vm.swappiness = 10
```

Apply with `sysctl -p`

**/etc/security/limits.conf**

```
*       soft    nofile  100000
*       hard    nofile  100000
```

**Bash commands**

`ulimit -Hn 1048576 && ulimit -Sn 65535`