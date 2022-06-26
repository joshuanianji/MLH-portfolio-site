echo "Reloading daemon..."
systemctl daemon-reload
echo "Restarting myportfolio"
systemctl restart myportfolio
echo "Status"
systemctl status myportfolio
