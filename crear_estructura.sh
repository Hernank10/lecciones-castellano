#!/data/data/com.termux/files/usr/bin/bash

echo "🚀 Creando proyecto Django..."

# Crear proyecto
django-admin startproject lecciones_castellano
cd lecciones_castellano

# Crear app
python manage.py startapp morfosintaxis

# Crear estructura de carpetas
echo "📁 Creando carpetas..."
mkdir -p morfosintaxis/templates/morfosintaxis
mkdir -p morfosintaxis/static/morfosintaxis/{css,js,img}
mkdir -p morfosintaxis/management/commands

# Crear archivos de templates
echo "📄 Creando archivos..."
touch morfosintaxis/templates/morfosintaxis/{base.html,index.html,lista_lecciones.html,leccion_detalle.html,ejercicio.html,progreso.html}

# Crear archivos static
touch morfosintaxis/static/morfosintaxis/css/estilos.css
touch morfosintaxis/static/morfosintaxis/js/ejercicios.js

# Crear archivos de configuración
touch morfosintaxis/urls.py
touch morfosintaxis/forms.py
touch morfosintaxis/management/__init__.py
touch morfosintaxis/management/commands/__init__.py
touch morfosintaxis/management/commands/cargar_lecciones.py

# Crear requirements.txt
echo "Django==4.2" > requirements.txt

# Crear README
echo "# Curso de Morfosintaxis Castellana" > README.md

echo "✅ Estructura creada exitosamente!"
echo ""
echo "📂 Estructura del proyecto:"
tree -L 3 2>/dev/null || find . -type d | sed 's|[^/]*/| |g'

echo ""
echo "🎯 Próximos pasos:"
echo "1. cd lecciones_castellano"
echo "2. pip install -r requirements.txt"
echo "3. python manage.py migrate"
echo "4. python manage.py createsuperuser"
echo "5. python manage.py runserver"
