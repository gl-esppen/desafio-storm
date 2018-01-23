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

##### Urls base:
* /api/filmes/
* /api/ator/
* /api/genero/


## Ambiente de Homologação

Foi levantando uma microintancia dentro do ambiente da AWS, utilizando o pacote de estudante. Por conta disso não foi possível configurar o ambiente para o RDS, S3, Load Balance e Auto Scaling.

Endereço IP : http://54.245.36.52/

Foi utilizado o NGINX e o gunicorn para colocar o serviço no ar.

##### Comandos basicos de monitoramento gunicorn
* sudo service gunicorn status
* sudo service gunicorn start
* sudo service gunicorn stop


##### Comandos basicos de monitoramento nginx
* sudo service nginx status
* sudo service nginx start
* sudo service nginx stop



## Sugestão de Arquitetura:

* Configurando o sistema 
- SUPERVISOR
Ferramenta para garantir que o gunicorn permaneça ativo e registra os logs de erro.

- Fabric
Ferramenta para automação de deploys.


* Otimizando o acesso
- EC2
    Instancia para aplicação, com integração de outros serviços para otimizar acesso e fluxo de dados.
	
	- Auto Scaling
        Detecta o volume de carga de acesso baseado em um alarme configurado, inicia uma nova instancia e coloca no Load Balance


    - Load Balance
        Configuração de máquinas secundárias para distribuição de carga com a instancia principal, de forma a evitar sobrecarga devido ao alto volume de acesso diário e simultaneo.

- RDS
    Banco de dados Postgres da aplicação

- S3
    Armazenamento de arquivos estáticos e de mídias.    


- CloudWatch
    Monitoramento das máquinas de processos com alertas personalizados (Ex: Database CPU)







