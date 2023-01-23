```
load_module /usr/lib/nginx/modules/ngx_stream_module.so;

events {}

http {
            server_names_hash_bucket_size 512;
            ssl_protocols TLSv1.2 TLSv1.3;
}

stream {

    server {
            listen 443;
            proxy_pass dns_servers_tcp_443;
            proxy_timeout 5s;
            proxy_connect_timeout 2s;
            ssl_protocols TLSv1.2 TLSv1.3;
        }

       upstream dns_servers_tcp_443 {
        least_conn;
        server 10.100.100.100:443;
    }

  }
```
