# Desafio Storm Security


Projeto para resolução do desafio back-end developer proposto pela Storm Security.

## Especificações Principais:
* Python 2.7
* Django 1.10 (O desafio propõe a utilização da versão 1.9 , no entanto foram encontrados erros de compatibilidade com o Django REST Framework)


## Instalação:

* Recomenda-se utilizar o virtualenvwrapper para trabalhar melhor no projeto:


    $ pip install virtualenvwrapper

    $ /usr/local/bin/virtualenvwrapper.sh 

    $ echo "export WORKON_HOME=~/.virtualenvs" >> ~/.bash_profile

    $ echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bash_profile 

    $ source ~/.bash_profile  



* Após fazer a instalação, podemos seguir com o setup do ambiente e a instalação dos pacotes necessários:


    $ mkvirtualenv storm

    $ workon storm

    $ make install
   

## Iniciando a Aplicação:
 
    $ make run


## Acessando Django API REST:

###### Urls base:
* /api/filmes/
* /api/ator/
* /api/genero/


## Sugestão de Arquitetura:

* Configurando o sistema 
- NGINX
- GUNICORN
- SUPERVISOR
- Fabric

* Otimizando o acesso
- EC2
	- Load Balance
	- Auto Scaling
- RDS
- S3
- CloudWatch