# E-Commerce [![Maintenance](https://img.shields.io/badge/Maintained%3F-no-red.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity) [![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white) ![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white) 
![Bootstrap](https://img.shields.io/badge/bootstrap-%238511FA.svg?style=for-the-badge&logo=bootstrap&logoColor=white) ![Figma](https://img.shields.io/badge/figma-%23F24E1E.svg?style=for-the-badge&logo=figma&logoColor=white)


## Objetivo
Projeto final da matéria de WebDesign no curso de Análise e Desenvolvimento de Sistemas no IFRN e teve o objetivo de utilizar o conhecimento adquirido na matéria sobre HTML e CSS.

<br>

## Pré requisitos
- [Python 3](https://www.python.org/downloads/)
- [MySql](https://dev.mysql.com/downloads/mysql/)

<br>

## Configurações necessárias
- Na pasta do projeto utilize o seguinte comando:
```
pip install flask; pip install flask_wtf; pip install pymysql; pip install flask_login

```
### Criação do banco de dados:
- Login no MySql:
```
mysql -u root -p
```
- Criação do banco de dados:
```
CREATE DATABASE ecommerce;
```
- Criação da tabela:
```
CREATE TABLE users(
    id integer not null auto_increment,
    usuario VARCHAR(100) not null,
    email VARCHAR(150) not null,
    senha VARCHAR(50) not null,
    PRIMARY KEY(id)
);
```

<br>

## Inicialização
Execute o arquivo "<b>run.py</b>"
