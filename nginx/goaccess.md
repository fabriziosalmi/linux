# GoAccess

GoAccess is an open source real-time web log analyzer and interactive viewer that runs in a terminal in _*nix_ systems or through your browser. It provides fast and valuable HTTP statistics for system administrators that require a visual server report on the fly.

- [GoAccess website](https://goaccess.io)
- [Live Demo](http://rt.goaccess.io/?20180926071813)
- [Download](https://goaccess.io/download)

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
