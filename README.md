# 📚 Curso de Morfosintaxis Castellana

Plataforma web interactiva con 100 lecciones de morfosintaxis del español, diseñada para estudiantes de lengua castellana.

## 🎯 Características

- ✅ 100 lecciones organizadas por nivel (básico, intermedio, avanzado)
- ✅ Ejercicios interactivos con retroalimentación inmediata
- ✅ Sistema de seguimiento de progreso del estudiante
- ✅ Panel de administración para gestionar contenido
- ✅ Teoría, ejemplos y práctica en cada lección

## 🛠️ Tecnologías

- **Backend:** Django 4.2
- **Base de datos:** SQLite (desarrollo)
- **Frontend:** HTML, CSS, JavaScript
- **Autenticación:** Django Auth

## 📋 Requisitos

- Python 3.8+
- pip

## 🚀 Instalación

### Clonar el repositorio

```bash
git clone https://github.com/Hernank10/lecciones-castellano.git
cd lecciones-castellano
Instalar dependencias
pip install -r requirements.txt
Configurar la base de datos
python manage.py makemigrations
python manage.py migrate
Crear superusuario
python manage.py createsuperuser
Iniciar el servidor
python manage.py runserver
Accede a: http://127.0.0.1:8000
👨‍💼 Panel de Administración
Accede al panel de administración en: http://127.0.0.1:8000/admin
Desde aquí puedes:
Crear y editar lecciones
Agregar ejercicios
Ver progreso de estudiantes
Activar/desactivar lecciones
📚 Estructura del Proyecto
lecciones_castellano/
├── manage.py
├── lecciones_castellano/      # Configuración del proyecto
│   ├── settings.py
│   └── urls.py
├── morfosintaxis/              # App principal
│   ├── models.py              # Modelos (Leccion, Ejercicio, Progreso)
│   ├── views.py               # Vistas
│   ├── admin.py               # Configuración del admin
│   ├── templates/             # Templates HTML
│   └── static/                # CSS, JS, imágenes
└── db.sqlite3                 # Base de datos
🎓 Niveles de Lecciones
Básico: Fundamentos de morfosintaxis
Intermedio: Estructuras más complejas
Avanzado: Análisis sintáctico profundo
🤝 Contribuir
Las contribuciones son bienvenidas. Por favor:
Fork el proyecto
Crea una rama (git checkout -b feature/nueva-funcionalidad)
Commit tus cambios (git commit -m 'Agregar nueva funcionalidad')
Push a la rama (git push origin feature/nueva-funcionalidad)
