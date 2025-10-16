# 🏥 API de Gestión de Pacientes - Django REST

API RESTful desarrollada en Django para el manejo de pacientes en un sistema médico.

## 📋 Tabla de Contenidos

- [Requisitos Previos](#requisitos-previos)
- [Instalación y Configuración](#instalación-y-configuración)
- [Configuración de la Base de Datos](#configuración-de-la-base-de-datos)
- [Migraciones](#migraciones)
- [Ejecución del Servidor](#ejecución-del-servidor)
- [Endpoints de la API](#endpoints-de-la-api)
- [Estructura del Proyecto](#estructura-del-proyecto)

## 🛠 Requisitos Previos

- **Python 3.8** o superior
- **MySQL Server 5.7** o superior
- **pip** (gestor de paquetes de Python)

## 🚀 Instalación y Configuración

### 1. Clonar el repositorio

```bash
git clone <url-del-repositorio>
cd patients-management-api
```
### 2. Configurar Ambiente Virtual
#### 2.1 Windows (PowerShell o CMD)
```bash
# Crear ambiente virtual
python -m venv venv

# Activar ambiente virtual
venv\Scripts\activate

# Verificar que está activado (deberías ver (venv) en la terminal)
```

#### 2.2 Linux/macOS (Terminal)
```bash
# Crear ambiente virtual
python3 -m venv venv

# Activar ambiente virtual
source venv/bin/activate

# Verificar que está activado (deberías ver (venv) en la terminal)
```

### 3. Instalación de dependencias
```bash
# Con el ambiente virtual activado, instalar las dependencias
pip install -r requirements.txt
```

### 4. Configuración de la Base de Datos
Vaya a sus gestor de bases de datos MySQL y cree la base de datos `patients`

### 5. Migraciones
#### Aplicar Migraciones para Crear las Tablas
```bash
# Crear migraciones (si es necesario)
python manage.py makemigrations

# Aplicar migraciones para crear las tablas en la base de datos "patients"
python manage.py migrate
```

### 6. Ejecución del Servidor
#### Iniciar el Servidor de Desarrollo
```bash
# Asegúrate de estar en el directorio del proyecto Django
# y con el ambiente virtual activado

python manage.py runserver
```

#### URLs de Acceso
* Servidor principal: http://127.0.0.1:8000
* API de pacientes: http://127.0.0.1:8000/api/patients/
* Admin de Django: http://127.0.0.1:8000/admin/

### 7. Endpoints de la API

#### GET /api/patients/

Descripción: Obtiene la lista de todos los pacientes

URL: http://127.0.0.1:8000/api/patients/

Respuesta:

```json
{
    "message": "Success",
    "patients": [
        {
            "id": 1,
            "name": "Ana",
            "lastname": "Ávila Ardila",
            "age": 32,
            "insurance": "REMALA EPS"
        }
    ]
}
```

#### GET /api/patients/{id}/

Descripción: Obtiene un paciente específico por ID

URL: http://127.0.0.1:8000/api/patients/1/

#### POST /api/patients/

Descripción: Crea un nuevo paciente

URL: http://127.0.0.1:8000/api/patients/

Body:
```json
{
    "name": "Carlos",
    "lastname": "Gómez",
    "age": 28,
    "insurance": "SALUD TOTAL"
}
```

#### PUT /api/patients/{id}/

Descripción: Actualiza un paciente existente

URL: http://127.0.0.1:8000/api/patients/1/

#### DELETE /api/patients/{id}/

Descripción: Elimina un paciente

URL: http://127.0.0.1:8000/api/patients/1/

### 8. Estructura del Proyecto

- **`manage.py`**: Script principal para administrar el proyecto Django
- **`requirements.txt`**: Lista de dependencias y paquetes Python necesarios
- **`.env`**: Variables de entorno sensibles (base de datos, secret keys)
- **`patients_api/models.py`**: Define el modelo `Patient` con campos: name, lastname, age, insurance
- **`patients_api/views.py`**: Contiene la lógica del CRUD (GET, POST, PUT, DELETE)
- **`patients_api/urls.py`**: Define los endpoints de la API (`/api/patients/`, `/api/patients/<id>/`)
- **`project/settings.py`**: Configuración de Django, base de datos, apps instaladas
