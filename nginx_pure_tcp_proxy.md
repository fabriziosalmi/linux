```
 
# all requests to TCP ports 80 and 443 will be forwarded to the relative origin ip:ports
# change $ORIGIN_IP to a valid origin ip address
# save to /etc/nginx/nginx.conf after a backup of the existing confguration and restart the service

http {
    	server_names_hash_bucket_size 512;
}

stream {
    
    server {
        listen          443;
        proxy_pass      dns_servers_tcp_443;
        proxy_timeout   5s;
        proxy_connect_timeout 2s;
    }

    upstream dns_servers_tcp_443 {
        least_conn;
        server        $ORIGIN_IP:443;
    }

    server {
        listen          80;
        proxy_pass      dns_servers_tcp_80;
        proxy_timeout   5s;
        proxy_connect_timeout 2s;
    }

    upstream dns_servers_tcp_80 {
        least_conn;
        server        $ORIGIN_IP:80;
    }

}

```
