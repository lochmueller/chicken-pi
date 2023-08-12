
echo "Upgrade dependencies"
sudo apt update && sudo apt-get upgrade

echo "Install python3-gpiozero"
sudo apt install python3-gpiozero

echo "Install python3-gpiozero"
sudo apt install python3-picamera

echo "Install python3 python3-pip"
sudo apt-get install python3 python3-pip

echo "Install Flask"
pip install Flask

echo "Install trio"
pip install trio

echo "Switch to home"
cd ~

echo "Clone Git"
git clone git@github.com:lochmueller/chicken-pi.git

echo "Change tp project"
cd chicken-pi

echo "Use this command to start the server: flask --app app run -h 0.0.0.0"
