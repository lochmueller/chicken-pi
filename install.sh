
echo "Update & Upgrade dependencies"
sudo apt update && sudo apt-get -y upgrade

echo "Install python3 python3-pip python3-gpiozero python3-picamera"
sudo apt-get -y install python3 python3-pip python3-gpiozero python3-picamera

echo "Install Flask"
pip install Flask

echo "Install trio"
pip install trio

echo "Switch to home"
cd ~

echo "Clone Git"
git clone https://github.com/lochmueller/chicken-pi.git

echo "Change tp project"
cd chicken-pi

echo "Install cronjob for reboot"
crontab -l > mycron
echo "@reboot sh ~/chicken-pi/launcher.sh > ~/chicken-pi/logs/cronlog.txt 2>&1" >> mycron
crontab mycron
rm -rf crontab

echo "Use ~/chicken-pi/launch.sh to start flask manually!"
