# IDEA GENERAL

## BussinesManager Web Edition

- Ver diferencia entre Lobby y BussinesManager. Si es necesario cambiar algo. La idea es que sea una presentación. 

-Página de administración y gestión de negocios.

-La página incluirá una parte de contacto y un about me a modeo de presentación del negocio.

-Administrar ventas, productos, clientes

-SuperUser: es obvio.

-Vendedor: Podrá cargar ventas y ver un historial de las mismas. Además podrá administrar sus clientes.

-La idea es que los módulos puedan usarse en otras apps...

-Los productos podrán ser digitales o físicos:
<!-- TODO Confirmar esto -->
Por ejemplo, podría venderse un servicio como una membresía a un gimnasio. Dicho "artículo" inluirá hasta o por cuánto dura en una descripción. 

Artículos físicos de cualquier tipo. Desde un auto hasta una crema para tu hermosa cara.

<!-- ! OPTO por artículos simples-->

### Artículos simples: 
Categorías muy simples y generales. Se pueden crear desde el lado de front. Probablemente elija esta porque es una prueba de todo, pero más que de backend y database. Puedo añadir una SubCategoría que esté relacionada a una SubCategoría para que quede más lindo.

### Artículos sofisticados: 
Categorías más complejas(se recomienda un diagrama), con subcategorías compuestas. Como debería ser un Ecom, creo yo.

## Cuentas
Antes de hacer algo en esta app ver este video: https://www.youtube.com/watch?v=tUqUdu0Sjyc&t=253s

Creo que el nombre correcto hubiera sido Usuarios pero ya no es relevante.

Se debe ver el concepto de vendedor como de staff o administrador(no superuser).

Admin podrá gestionar los vendedores.
Los vendedores podrán administrar sus clientes. Incluirá el registro de usuarios.

Por ejemplo, Cuenta: Juan o Juan@gmail.com. Puede ser o un cliente o un admin. Cada uno con sus permisos.

## Ventas

### Módulo de ventas y negocio

Administrar ventas y con un registro de las mismas hacer estadísticas. 

Por ejemplo, el vendedor podrá ver qué artículos fueron los más vendidos y cuales los menos. Cuánto recaudó en cierto período de tiempo(ganancia-capital) o cuánto gastó en empleados, local e impuestos. Lo ideal sería un gráfico, con la data.

## Productos
Administrar productos (CRUD)
Todo el display será para un admin.

## Tienda
ATENCIÓN! Este es para hacer compras

App que tiene como fin mostrar los productos en forma de una tienda estándar. El display será para el cliente y admin.

## Activar venv

Desde la carpeta UltimaPrueba:

.\UPrueba-env\Scripts\activate

## Hacer migraciones

py manage.py makemigrations

py manage.py migrate

Mariano022 Dragones456b