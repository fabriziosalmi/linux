# GoAccess

#### Install GoAccess

- `yum install goaccess` (Debian/Ubuntu) or 
- `apt-get install goaccess` (Fedora/RedHat) or 
- `brew install goaccess` (OSX)

#### GoAccess via shell

`goaccess -f /var/log/httpd/mysite_access.log`

#### GoAccess export to HTML

`goaccess -f /var/log/httpd/mysite_today.log -o /var/www/html/report.html --log-format=COMBINED`

#### GoAccess real time HTML

`goaccess -f /var/log/httpd/mysite.log -o /var/www/html/report.html --log-format=COMBINED --real-time-html`
