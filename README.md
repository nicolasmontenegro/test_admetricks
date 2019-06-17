# test_admetricks

## Descripción

Este proyecto es una aplicación web para es visualizar la variación diaria del dólar a Peso Chileno (CLP).
Contiene servicios basados en Django, Nuxt y Postgres, cada uno contenido en un Docker propio que se orquesta a través de Docker-Compose.

## Dependencias

* Docker-compose: https://docs.docker.com/compose/install/

## Instalación

Una vez descomprimido/clonado el repo, inicializar a través de docker compose.

`$ > docker-compose up`

Esto inicializará los siguientes contenedores
* test_admetricks_django
* test_admetricks_node
* postgres

Una vez construido, debe inicializar la base de datos aplicando las migraciones y levantando los datos.

`$ > docker-compose run django python manage.py migrate`

`$ > docker-compose run django python manage.py seed --mode=refresh`

## Instrucciones de uso

Para ingresar a la plataforma debe ingresar a http://localhost:3000.

## Consideraciones 

Puede ser necesario el uso de algún complemento que permita consultas fuera del dominio (CORS)
* Firefox: https://addons.mozilla.org/es/firefox/addon/cors-everywhere/
* Chrome: https://chrome.google.com/webstore/detail/allow-control-allow-origi/nlfbmbojpeacfghkpbjhddihlkkiljbi
