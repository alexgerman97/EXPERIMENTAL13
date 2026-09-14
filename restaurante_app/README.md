# Restaurante App - Semana 13

## Información del estudiante

- Nombre: Alex Toaquiza
- Semana: Practico Experimental 13

---

## Descripción

Restaurante App es una aplicación desarrollada en Python utilizando Programación Orientada a Objetos y Tkinter. Esta versión corresponde a la base gráfica del proyecto y permite simular el acceso al sistema mediante una pantalla de login y visualizar la información de productos y usuarios almacenada en archivos JSON.

---

## Estructura del proyecto

```text
restaurante_app
├── datos
│   ├── productos.json
│   └── usuarios.json
├── modelos
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
├── servicios
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
├── ui
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
├── main.py
└── README.md
```

---

## Responsabilidad de los componentes

### modelos/

Contiene las entidades principales del sistema:

- Producto
- Usuario

### servicios/

Contiene la lógica de negocio y acceso a datos:

- ArchivoServicio: lectura de archivos JSON.
- RestauranteServicio: validación de acceso y consulta de información.

### ui/

Contiene las vistas gráficas desarrolladas con Tkinter:

- LoginView
- MainView

### datos/

Contiene la información almacenada en formato JSON.

### main.py

Inicializa la aplicación, crea la ventana principal y controla el cambio entre vistas.

---

## Flujo de la aplicación

```text
Inicio
   ↓
LoginView
   ↓
Validación de acceso
   ↓
MainView
   ↓
Visualización de productos y usuarios
   ↓
Cerrar sesión
   ↓
LoginView
```

---

## Vistas implementadas

### LoginView

Permite ingresar:

- Usuario
- Contraseña

Muestra mensajes de error cuando:

- Existen campos vacíos.
- Las credenciales son incorrectas.

### MainView

Permite visualizar:

- Productos registrados.
- Usuarios registrados.

Incluye una opción identificada como:

- Ventas (Pendiente)

Además permite cerrar sesión y regresar al login.

---

## Archivos JSON utilizados

### productos.json

Contiene:

- Código
- Nombre
- Categoría
- Precio
- Stock

### usuarios.json

Contiene:

- Identificación
- Nombre
- Correo

---

## Forma de ejecución

Ubicarse en la carpeta del proyecto y ejecutar:

```bash
python restaurante_app/main.py
```

---

## Pruebas realizadas

Se verificó:

1. Inicio correcto de la aplicación.
2. Visualización del login.
3. Validación de campos vacíos.
4. Validación de credenciales incorrectas.
5. Acceso mediante usuario válido.
6. Visualización de productos.
7. Visualización de usuarios.
8. Regreso al login mediante cierre de sesión.

Todas las pruebas fueron satisfactorias.

---

## Conclusión

Se implementó la base gráfica de Restaurante App utilizando Tkinter y manteniendo la separación de responsabilidades mediante modelos, servicios y vistas. Esta estructura permitirá incorporar nuevas funcionalidades en las siguientes semanas sin modificar la arquitectura principal del sistema.