# Taller1-Info1148
Descripción
Este proyecto implementa un sistema de validación de patrones en cadenas de texto utilizando expresiones regulares en Python. El sistema es capaz de identificar y clasificar diferentes tipos de tokens como correos electrónicos, identificadores, números, contraseñas, palabras reservadas y operadores.

Características
Validación de 8 tipos diferentes de tokens mediante expresiones regulares

Procesamiento de archivos de texto con múltiples tokens

Modo interactivo para validación individual

Reportes estadísticos de validación

Interfaz de línea de comandos amigable

Tipos de Tokens Reconocidos
EMAIL: Direcciones de correo electrónico válidas

IDENTIFIER: Identificadores de variables (comienzan con letra o guión bajo)

NUMBER: Números enteros y decimales con signo opcional

PASSWORD: Contraseñas seguras (8+ caracteres, mayúscula, minúscula, número y carácter especial)

RESERVED_WORD: Palabras reservadas (if, else, while, for, return)

LOGICAL_OPERATOR: Operadores lógicos (&&, ||, !)

ARITHMETIC_OPERATOR: Operadores aritméticos (+, -, *, /, %, **)

RELATIONAL_OPERATOR: Operadores relacionales (==, !=, <, >, <=, >=)

Requisitos
Python 3.6 o superior

No se requieren librerías externas (utiliza sólo módulos estándar de Python)

Instalación
Clona o descarga el repositorio

Navega al directorio del proyecto

El proyecto no requiere instalación adicional

Uso
Modo archivo
Procesa un archivo de texto con tokens (uno por línea):

bash
python token_validator.py archivo_tokens.txt
Modo interactivo
Ejecuta el programa sin argumentos para acceder al menú interactivo:

bash
python token_validator.py
Opciones disponibles:

Validar un archivo de texto

Validar un token individual

Salir

Ejemplos de uso
python
# Ejemplo de uso directo desde Python
from token_validator import TokenValidator

validator = TokenValidator()
resultado = validator.validate_single_token("usuario@example.com")
print(resultado)  # Output: True (EMAIL)

tokens = validator.process_file("tokens.txt")
Estructura del Proyecto
text
token_validator.py  # Código principal del validador
tokens.txt          # Archivo de ejemplo con tokens para validar
README.md           # Este archivo
Expresiones Regulares Implementadas
EMAIL: ^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$

IDENTIFIER: ^[a-zA-Z_][a-zA-Z0-9_]*$

NUMBER: ^-?\d+(\.\d+)?$

PASSWORD: ^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$

RESERVED_WORD: ^(if|else|while|for|return)$

LOGICAL_OPERATOR: ^(&&|\|\||!)$

ARITHMETIC_OPERATOR: ^(\+|-|\*|/|%|\*\*)$

RELATIONAL_OPERATOR: ^(==|!=|<|>|<=|>=)$

Formato del Archivo de Entrada
El archivo de entrada debe ser un archivo de texto plano con un token por línea:

text
usuario@example.com
12345
Password123!
if
&&
==
Salida del Programa
El programa muestra una tabla con los resultados de la validación:

text
============================================================
RESULTADOS DE VALIDACIÓN DE TOKENS
============================================================
LÍNEA  TOKEN                    TIPO                 VÁLIDO
------------------------------------------------------------
1      usuario@example.com      EMAIL                SÍ
2      12345                    NUMBER               SÍ
3      Password123!             PASSWORD             SÍ
4      if                       RESERVED_WORD        SÍ
5      &&                       LOGICAL_OPERATOR     SÍ
6      ==                       RELATIONAL_OPERATOR  SÍ
------------------------------------------------------------
Total tokens: 6
Tokens válidos: 6
Tokens inválidos: 0
============================================================
Además, genera un reporte estadístico con la distribución de tokens por tipo.

Personalización
Para agregar nuevos tipos de tokens, modifica el diccionario patterns en la clase TokenValidator:

python
self.patterns = {
    'NUEVO_TOKEN': r'^expresión_regular$',
    # ... otros tokens
}
Pruebas
El proyecto incluye un archivo tokens.txt con más de 70 ejemplos de tokens válidos e inválidos para pruebas. Se recomienda verificar el funcionamiento con este archivo antes de usar el validador con datos propios.

Limitaciones
Las expresiones regulares para contraseñas y correos electrónicos pueden no cubrir todos los casos posibles según estándares actualizados

El rendimiento puede disminuir con archivos muy grandes (>10,000 tokens)

No se soportan tokens multi-línea

Autor
Desarrollado por Benjamin Sobarzo, Kevin Cortes, Jonatha Huinca para el Taller 1 de INFO1148 - Teoría de la Computación, Semestre II-2025.

Contacto
Para dudas o sugerencias, contactar a:

bsobarzo2019@alu.uct.cl

kcortes2021@alu.uct.cl

jhuinca2020@alu.uct.cl
