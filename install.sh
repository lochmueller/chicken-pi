
echo "------------ Update & Upgrade dependencies"
sudo apt update && sudo apt-get -y upgrade

echo "------------ Install Package requirements"
sudo apt-get -y install python3 python3-pip python3-gpiozero python3-picamera

echo "------------ Switch to home"
cd ~

echo "------------ Clone Git"
git clone https://github.com/lochmueller/chicken-pi.git

echo "------------ Change tp project"
cd chicken-pi

echo "------------ Install Pip requirements"
pip install -r requirements.txt

echo "------------ Install cronjob for reboot"
touch mycron
echo "@reboot sh ~/chicken-pi/launcher.sh > ~/chicken-pi/logs/crontab.txt 2>&1" >> mycron
crontab mycron
rm -rf mycron

echo "------------ Create logs dir"
mkdir -p logs

echo "------------ Use ~/chicken-pi/launch.sh to start flask manually!"
