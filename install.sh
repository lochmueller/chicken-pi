
echo "Upgrade dependencies"
sudo apt update && sudo apt-get upgrade

echo "Install python3-gpiozero"
sudo apt install python3-gpiozero

echo "Install python3-gpiozero"
sudo apt install python3-picamera

echo "Install python3 python3-pip"
sudo apt-get install python3 python3-pip

echo "Install fastapi uvicorn[standard]"
pip3 install fastapi uvicorn[standard]
