# **Hotel CAL - Sistema de Reservas**

Este proyecto es un sistema de reservas para el *Hotel Californian*. El sitio web permite a los usuarios ver habitaciones disponibles, registrarse, iniciar sesión y realizar reservas. Los administradores pueden gestionar las reservas desde una interfaz de administración.

## **Índice**

1. [Introducción](#introducción)
2. [Requisitos Previos](#requisitos-previos)
3. [Descripción del Código](#descripción-del-código)
    - [index.html](#index.html)
    - [login.html](#login.html)
    - [admin.html](#admin.html)
    - [register.html](#register.html)
    - [admin/clientes.html](#admin/clientes.html)
    - [admin/habitaciones.html](#admin/habitaciones.html)
    - [admin/reservas.html](#admin/reservas.html)
    - [cliente/perfil.html](#cliente/perfil.html)
    - [cliente/reservas.html](#cliente/reservas.html)
    - [styles.css](#assets/css/styles.css)
    - [main.js](#assets/js/main.js)
4. [Problemas y Soluciones Comunes](#problemas-y-soluciones-comunes)
5. [Conclusión](#conclusión)

---

## **Introducción**

Este proyecto proporciona un sistema completo para la gestión de reservas de un hotel. Consta de varias páginas clave para la interacción con los usuarios y administradores.

## **Requisitos Previos**

Para ejecutar este proyecto correctamente, asegúrate de tener lo siguiente:

- **Servidor Backend** que maneje las solicitudes a los endpoints como `/api/register`, `/api/login`, `/api/habitaciones/disponibles`, `/api/reservas`, `/api/clientes`, entre otros.
- **Servidor web** Nginx para servir archivos estáticos o un servidor local como XAMPP o WAMP.
- **Editor de código** (opcional): Visual Studio Code, Sublime Text, etc.

---

## **Descripción del Código

- **Página de inicio (`index.html`)**: Muestra las habitaciones disponibles en el hotel y permite a los usuarios realizar reservas, registrarse, tambien que estos puedan iniciar sesión.
- **Página de iniciar sesión (`login.html`)**: Permite a los usuarios inicien sesión en el sistema.
- **Página de registro (`register.html`)**: Permite a los nuevos usuarios registrarse para crear una cuenta.
- **Página de administrador (`admin.html`)**: Permite a los administradores iniciar sesión para gestionar las reservas, habitaciones disponibles y los clientes actuales.
- **Página de administrador sobre los clientes actuales (`admin/clientes.html`)**: Muestra a los administradores una lista de los clientes actuales que están hospedados en el hotel. La información se muestra en una tabla con detalles sobre la habitación, fecha de llegada y salida, al igual que un botón para ver detalles adicionales.
- **Página de administrador de habitaciones disponibles (`admin/habitaciones.html`)**: Muestra una lista de las habitaciones disponibles en el hotel, con detalles como el tipo de habitación, precio por noche y estado (disponible u ocupada).
- **Página de administrador de reservas (`admin/reservas.html`)**: Permite a los administradores gestionar todas las reservas realizadas, visualizar los detalles de cada reserva y cambiar su estado. Muestra una tabla con las reservas, que incluye el ID de la reserva, cliente, habitación, fechas de inicio y fin, tambien el estado de la reserva.
- **Página de perfil de los clientes (`cliente/perfil.html`)**: Permite que el usuario pueda ver su perfil, conteniendo toda su informacion y llevarlo hacia sus reservaciones.
- **Página de reservas de los clientes (`cliente/reservas.html`)**: Permite que usuarain pueda inspecionar sus reservaciones en el hotel, pero si este no inicio sensión lo devuelve hacia la página login.
- **Página del header (`include/header.html`)**: Página que contiene header que se utiliza en todas las paginas del proyecto.
- **Página del footer (`include/footer.html`)**: Página que contiene el footer que es utilizado por todas las paginas del proyecto.
- **Página de Css y JavaScript (`assets/css/styles.css` `assets/js/main.js`)**: En el style sheet es donde hicieron cambios para elementos para las paginas. En la pagina de java script habilito un detalle para la página de reservas que es inspeccionada por el cliente.  
---

## **Problemas

1. **Clonar el Repositorio**:
   Si aún no has clonado el proyecto, puedes hacerlo con el siguiente comando:
   ```bash
   git clone https://github.com/usuario/hotel-cal.git
