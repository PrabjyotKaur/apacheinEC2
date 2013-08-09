var1='ProxyPass /  http://50.112.65.135:80/'
if grep -Fxq "$var1"  /etc/httpd/conf/httpd.conf
then
    echo "ProxyPass comment is Already Exists"
else
    # code if not found
echo -e "<VirtualHost *:80>\nProxyPass /  http://50.112.63.93:80/\nProxyPassreverse / http://50.112.63.93:80/\n</VirtualHost>" | sudo tee -a  /etc/httpd/conf/httpd.conf
fi
