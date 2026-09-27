# Restaurante App

## Descripción

Restaurante App es una aplicación desarrollada en Python utilizando Programación Orientada a Objetos (POO) y Tkinter. El proyecto fue elaborado como parte de la Semana 13 de la asignatura, tomando como referencia la estructura del proyecto docente "Biblioteca App" y adaptándola al contexto de un restaurante.

La aplicación permite realizar un acceso mediante usuario y contraseña, visualizar productos registrados y consultar usuarios almacenados en archivos JSON. Además, incorpora una estructura organizada en modelos, servicios y vistas gráficas para facilitar el mantenimiento y la ampliación futura del sistema.

---

## Objetivo

Aplicar los conceptos de Programación Orientada a Objetos, separación de responsabilidades, manejo de archivos JSON y desarrollo de interfaces gráficas con Tkinter mediante una aplicación básica de gestión para un restaurante.

---

## Estructura del Proyecto

```text
restaurante_app/
├── datos/
│   ├── productos.json
│   └── usuarios.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
├── ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
├── main.py
└── README.md
```

---

## Responsabilidad de cada módulo

### datos/

Contiene los archivos JSON utilizados para almacenar la información local de la aplicación.

- productos.json
- usuarios.json

### modelos/

Representa las entidades principales del sistema.

#### Producto

Almacena la información de los productos del restaurante:

- Código
- Nombre
- Categoría
- Precio
- Stock

#### Usuario

Representa los usuarios que pueden acceder al sistema.

- Usuario
- Contraseña
- Nombre

### servicios/

Contiene la lógica de negocio de la aplicación.

#### ArchivoServicio

Responsable de leer la información almacenada en los archivos JSON.

#### RestauranteServicio

Responsable de:

- Cargar productos
- Cargar usuarios
- Validar credenciales
- Listar productos
- Listar usuarios

### ui/

Contiene las interfaces gráficas desarrolladas con Tkinter.

#### LoginView

Permite:

- Ingresar usuario
- Ingresar contraseña
- Validar acceso
- Mostrar mensajes de error

#### MainView

Permite:

- Mostrar productos registrados
- Mostrar usuarios registrados
- Mostrar opción de ventas (pendiente)
- Cerrar sesión

### main.py

Punto de entrada de la aplicación.

Responsabilidades:

- Crear la ventana principal
- Inicializar servicios
- Mostrar LoginView
- Controlar el cambio entre vistas
- Mantener un único ciclo de ejecución

---

## Flujo de la Aplicación

```text
Inicio de la aplicación
        ↓
main.py
        ↓
LoginView
        ↓
Ingreso de usuario y contraseña
        ↓
Validación mediante RestauranteServicio
        ↓
MainView
        ↓
Productos registrados
Usuarios registrados
Ventas (Pendiente)
        ↓
Cerrar sesión
        ↓
LoginView
```

---

## Funcionalidades Implementadas

### Acceso al sistema

- Validación de usuario y contraseña.
- Mensaje de error cuando existen campos vacíos.
- Mensaje de error cuando las credenciales son incorrectas.
- Mensaje de bienvenida cuando el acceso es correcto.

### Gestión de Productos

- Lectura desde productos.json.
- Visualización de productos registrados.

### Gestión de Usuarios

- Lectura desde usuarios.json.
- Visualización de usuarios registrados.

### Cierre de Sesión

- Regreso a la pantalla de inicio de sesión.
- Uso de una única ventana principal de Tkinter.

### Funcionalidades Futuras

- Gestión de ventas.
- Registro de pedidos.
- Administración de clientes.
- Reportes del restaurante.

---

## Tecnologías Utilizadas

- Python 3
- Tkinter
- Programación Orientada a Objetos (POO)
- JSON
- Visual Studio Code
- GitHub

---

## Requisitos

- Python 3 instalado.
- Tkinter habilitado.
- Visual Studio Code (opcional).

---

## Ejecución del Proyecto

Ubicarse en la carpeta principal del proyecto y ejecutar:

```bash
python main.py
```

---

## Evidencias de Funcionamiento

La aplicación permite:

1. Mostrar la pantalla de inicio de sesión.
2. Validar credenciales de acceso.
3. Mostrar el panel principal.
4. Consultar productos registrados.
5. Consultar usuarios registrados.
6. Regresar al inicio de sesión mediante la opción Cerrar Sesión.

---

## Autor

Alex Toaquiza

Universidad Estatal Amazónica

Programación Orientada a Objetos – Semana 13