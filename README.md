# Cuenta-Bancaria
En este proyecto simularemos una cuenta bancaria.

Este código implementa una clase CuentaBancaria que simula las operaciones básicas de una cuenta bancaria y utiliza conceptos fundamentales de encapsulamiento en programación orientada a objetos (POO). El objetivo principal es demostrar cómo se pueden proteger los datos sensibles en una clase, permitiendo interacciones controladas y seguras.

Características de la Clase CuentaBancaria

Encapsulamiento de Datos:

- Atributo protegido: El número de cuenta (_numero_cuenta) está protegido para evitar modificaciones accidentales, pero es accesible en situaciones controladas.
  
- Atributo privado: El saldo (__saldo) se mantiene completamente privado y solo es accesible a través de métodos específicos, garantizando la integridad de los datos.

Métodos Públicos:

- get_saldo(): Permite consultar el saldo actual de la cuenta sin exponer directamente el atributo privado.
  
- depositar(monto): Agrega una cantidad al saldo de la cuenta, permitiendo transacciones de ingreso.
  
- retirar(monto): Permite retirar fondos si el saldo es suficiente; de lo contrario, notifica que el saldo es insuficiente.
  
Objetivos de Diseño
Este proyecto enfatiza la importancia de proteger los datos mediante encapsulamiento en POO, limitando el acceso directo a los atributos de la clase y proporcionando métodos controlados para gestionar el saldo de manera segura.

Este código es ideal para mostrar cómo implementar el encapsulamiento en una clase de Python y ofrece un ejemplo claro de control de acceso en aplicaciones bancarias o financieras.
