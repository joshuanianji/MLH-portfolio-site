cd /root/MLH-portfolio-site
git fetch && git reset origin/main --hard

source .venv/bin/activate
pip install -r requirements.txt 

echo "Reloading daemon..."
systemctl daemon-reload
echo "Restarting myportfolio"
systemctl restart myportfolio
echo "Status"
systemctl status myportfolio
