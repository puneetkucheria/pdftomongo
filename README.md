# pdftomongo

sudo apt update

sudo apt install git

sudo apt install python3-pip

pip3 install virtualenv

virtualenv pdftomongo

echo "# pdftomongo" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/puneetkucheria/pdftomongo.git

# Install Mongodb
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 2930ADAE8CAF5059EE73BB4B58712A2291FA4AD5
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.6 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.6.list
sudo apt update
sudo apt install -y mongodb-org

sudo systemctl enable mongod.service

sudo systemctl stop mongod.service
sudo systemctl start mongod.service

