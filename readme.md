# Solución de la Kata Guilded Rose

## Ejercicio de refactorización

El ejercicio fue propuesto como práctica del curso de 
Principios SOLID aplicados de CodelyTVPro.

### Reglas básicas:

Un cliente tiene un inventario de productos perecederos (Items)
estos productos tienen una calidad Q y una cantidad de días de venta S.

Al terminar cada día el sistema actualiza Q y S de tal modo que todos los días S y Q pierden valor.

Originalmente existen los siguientes tipos de producto:

- **Items:** si aumenta el tiempo en días (T+=1) entonces Q -= 1 y S -= 1
- Legendarios: no pueden venderse y tampoco perecen
- Bree: si(T+=1) entonces Q+=1 S-=1
- Back Stage: similar a *Bree* pero 10 días previos al concierto aumenta Q += 2,
5 días antes Q += 3 y si ya pasó el concierto Q = 0


Además el cliente comenzó a comprar Items Conjured a un nuevo proveedor.
Estos funcionan como un *Item* normal pero Q-=2

Los productos con caducidad pierden calidad el doble de rápido una vez que han expirado.

En el archivo: src/test_gilded_rose.py se muestra el código legacy del cliente.

El reto es refactorizar la base de código del cliente sin afectar la implementación y 
hacer uso de los principios SOLID.



Requerimiento detallado en:
https://github.com/NotMyself/GildedRose

El reto fue tomado de:
https://kata-log.rocks/gilded-rose-kata

El código base en python fue tomado de: 
https://github.com/emilybache/GildedRose-Refactoring-Kata/tree/master/python