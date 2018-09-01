# pdftomongo
sudo apt update
sudo apt install git
sudo apt install python3-pip

# Installing virtualenv
pip3 install virtualenv

## Use Virtualenv to get gitcode
virtualenv pdftomongo

# Getting Git code
cd pdftomongo
mkdir app
git init
git remote add origin 
git remote add origin https://github.com/puneetkucheria/pdftomongo.git
git pull origin master

# Install pdfminer2
pip3 install pdfminer2

# Install Mongodb
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 2930ADAE8CAF5059EE73BB4B58712A2291FA4AD5
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.6 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.6.list
sudo apt update
sudo apt install -y mongodb-org

## commnads used to mainage mongo server
sudo systemctl enable mongod.service
sudo systemctl stop mongod.service
sudo systemctl start mongod.service
sudo systemctl status mongod
