**1. Используя команду cat в терминале операционной системы Linux, 
создать два файла Домашние животные (заполнив файл собаками, кошками, хомяками) 
и Вьючные животными заполнив файл Лошадьми, верблюдами и ослы), а затем объединить их. 
Просмотреть содержимое созданного файла. Переименовать файл, дав ему новое имя (Друзья человека).**

sudo apt update  
cat pets
cat > Pets.txt
cat Pets.txt 
cat > Pack_Animals.txt
cat Pack_Animals.txt
cat Pets.txt Pack_Animals.txt > Human's_Friends.txt
cat Pets.txt Pack_Animals.txt > Human_Friends.txt
cat Human_Friends.txt

**2. Создать директорию, переместить файл туда.**

mkdir Animals
mv Human_Friends.txt Animals/
ls Animals/

**3. Подключить дополнительный репозиторий MySQL. Установить любой пакет из этого репозитория.**
 
sudo apt install mysql-server
sudo apt update
systemctl status mysql.service
wget https://dev.mysql.com/get/mysql-apt-config_0.8.26-1_all.deb
sudo dpkg -i mysql-apt-config_0.8.26-1_all.deb 
sudo apt update
systemctl status mysql.service

**4. Установить и удалить deb-пакет с помощью dpkg.**

dpkg -l
dpkg -l | grep mysql
sudo dpkg -r mysql-apt-config

**5. Выложить историю команд в терминале ubuntu**

history
history > history_commands.txt