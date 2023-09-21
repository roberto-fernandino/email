# Plataforma de Email

Esta é uma plataforma simples para enviar emails utilizando templates HTML ou templates HTML personalizados. A aplicação é orquestrada com Docker e Docker Compose e inclui um painel para personalizar os emails.

## Requisitos

- Docker
- Docker Compose

## Como Usar

### Configuração Inicial

1. Clone o repositório para sua máquina local.
2. Navegue até o diretório do projeto.
3. Cole o arquivo `.env` na raiz do projeto.
4. Execute para construir os contêineres.
```bash 
docker-compose build
``` 
5. Execute para inicializar os contêineres.
```bash 
docker-compose up
``` 

### Criar uma Conta de Administrador

1. Após a inicialização do `docker-compose`, abra um novo terminal.
2. Execute para acessar o contêiner do Django.
```bash
docker exec -it django_app_email sh
```
3. Dentro do contêiner, execute e siga as instruções para criar um usuário administrador.
```bash
python manage.py createsuperuser
```

4. Pronto agora pode sair do terminal do contaier e desfrutar da plataforma.

### Acessar a Plataforma
1. Quando executar o container com `docker-compose up` uma url NGROK será informada ela que você usará. 
2. Painel de Administração: Acesse `<url_ngrok>/admin` para administrar a plataforma. É aqui que você pode enviar emails e gerenciar destinatários.
  
- Relatórios: Acesse `<url_ngrok>` para ver gráficos e relatórios sobre os emails enviados.

## Funcionalidades

- Envio de emails com templates HTML pré-definidos.
- Envio de emails com templates HTML personalizados.
- Painel para customização de emails.
- Gráficos e relatórios para monitorar os emails enviados.
- Exportacao de relatório em formato CSV.

## Dicas

- Fique atento aos logs do docker.