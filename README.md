## Validador de Tokens con Expresiones Regulares

# Descripción:

Sistema de validación de patrones en cadenas de texto utilizando expresiones regulares en Python. El sistema es capaz de identificar y clasificar diferentes tipos de tokens como correos electrónicos, identificadores, números, contraseñas, palabras reservadas y operadores.

## ✨ Características:

- ✅ Validación de 8 tipos diferentes de tokens mediante expresiones regulares,
- 📁 Procesamiento de archivos de texto con múltiples tokens,
- 💻 Modo interactivo para validación individual,
- 📊 Reportes estadísticos de validación,
- 🖥️ Interfaz de línea de comandos amigable.

## 🎯 Tipos de Tokens Reconocidos:

1. EMAIL: Direcciones de correo electrónico válidas,
2. IDENTIFIER: Identificadores de variables (comienzan con letra o guión bajo),
3. NUMBER: Números enteros y decimales con signo opcional,
4. PASSWORD: Contraseñas seguras (8+ caracteres, mayúscula, minúscula, número y carácter especial),
5. RESERVED_WORD: Palabras reservadas (if, else, while, for, return),
6. LOGICAL_OPERATOR: Operadores lógicos (&&, ||, !),
7. ARITHMETIC_OPERATOR: Operadores aritméticos (+, -, *, /, %, **),
8. RELATIONAL_OPERATOR: Operadores relacionales (==, !=, <, >, <=, >=)

## 📋 Requisitos
- Python 3.6 o superior
- No se requieren librerías externas (utiliza sólo módulos estándar de Python)

## 🔧 Instalación
bash
# Clona o descarga el repositorio
git clone https://github.com/blosttt/taller1-info1148.git
# Navega al directorio del proyecto
cd taller1-info1148
El proyecto no requiere instalación adicional.

## 🚀 Uso:

Modo archivo:
Procesa un archivo de texto con tokens (uno por línea):

bash:
python token_validator.py archivo_tokens.txt

Modo interactivo
Ejecuta el programa sin argumentos para acceder al menú interactivo:

bash:
python token_validator.py
Opciones disponibles:

1. Validar un archivo de texto
2. Validar un token individual
3. Salir

Ejemplos de uso
# Ejemplo de uso directo desde Python
from token_validator import TokenValidator

validator = TokenValidator()
resultado = validator.validate_single_token("usuario@example.com")
print(resultado)  # Output: True (EMAIL)

tokens = validator.process_file("tokens.txt")

## 📁 Estructura del Proyecto

# taller1-info1148/
# ├── token_validator.py  # Código principal del validador
# ├── tokens.txt          # Archivo de ejemplo con tokens para validar
# ├── README.md           # Este archivo
# └── requirements.txt    # Dependencias (vacío o con librerías si se añaden)

## 🧩 Expresiones Regulares Implementadas:
1. EMAIL: ^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$,
2. IDENTIFIER: ^[a-zA-Z_][a-zA-Z0-9_]*$,
3. NUMBER: ^-?\d+(\.\d+)?$,
4. PASSWORD: ^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$,
5. RESERVED_WORD: ^(if|else|while|for|return)$,
6. LOGICAL_OPERATOR: ^(&&|\|\||!)$,
7. ARITHMETIC_OPERATOR: ^(\+|-|\*|/|%|\*\*)$,
8. RELATIONAL_OPERATOR: ^(==|!=|<|>|<=|>=)$,

## 📝 Formato del Archivo de Entrada:
El archivo de entrada debe ser un archivo de texto plano con un token por línea:
usuario@example.com
12345
Password123!
if
&&
==.


## 🔧 Personalización:

Para agregar nuevos tipos de tokens, modifica el diccionario patterns en la clase TokenValidator:

self.patterns = {
    'NUEVO_TOKEN': r'^expresión_regular$',
    # ... otros tokens
}

## 🧪 Pruebas:
El proyecto incluye un archivo tokens.txt con más de 70 ejemplos de tokens válidos e inválidos para pruebas. Se recomienda verificar el funcionamiento con este archivo antes de usar el validador con datos propios.

## ⚠️ Limitaciones:
Las expresiones regulares para contraseñas y correos electrónicos pueden no cubrir todos los casos posibles según estándares actualizados,

El rendimiento puede disminuir con archivos muy grandes (>10,000 tokens),

No se soportan tokens multi-línea,

## 👥 Autor
Desarrollado por Benjmain Sobarzo, Kevin Cortes, Jonthan Huinca para el Taller 1 de INFO1148 - Teoría de la Computación, Semestre II-2025.

