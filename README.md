# App para el Control de Pico y Placa

## Descripción

Este es un pequeño proyecto que permite verificar si un vehículo puede circular, según el sistema de Pico y Placa. El
sistema de Pico y Placa restringe la circulación de vehículos en función del último dígito de la placa y el día de la
semana.

## Tecnologías

- Flask
- PostgreSQL
- HTML
- CSS
- Bootstrap

## Instalación

1. Clonar el repositorio
2. Tener instalado Python 3.8
2. Crear un entorno virtual (python3.8 -m venv venv_picoplaca)
3. Activar el entorno virtual (source venv_picoplaca/bin/activate)
4. Instalar las dependencias (pip install -r requirements.txt)
5. Crear una base de datos en PostgreSQL
6. Crear un archivo .env en la raíz del proyecto con las siguientes variables de entorno:

```
DATABASE_URL=postgresql://usuario:contraseña@localhost/nombre_base_de_datos
SECRET_KEY=llave_secreta
```

7. Ejecutar la aplicación (python app.py)
8. Acceder a la aplicación en el navegador

## Funcionalidades

### Inicio

![Home](static/images/home.png)

### Configuración de Pico y Placa

![Config Time](static/images/config_time.png)


### Lista de Configuraciones

![List Time](static/images/list_time.png)

### Validación de Placa

![Validate Plate](static/images/validate_plate.png)


### Información Personal

![About Page](static/images/about_page.png)
