import re
import sys
from datetime import datetime

class TokenValidator:
    def __init__(self):
        # Expresiones regulares para cada tipo de token
        self.patterns = {
            'EMAIL': r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
            'IDENTIFIER': r'^[a-zA-Z_][a-zA-Z0-9_]*$',
            'NUMBER': r'^-?\d+(\.\d+)?$',
            'PASSWORD': r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$',
            'RESERVED_WORD': r'^(if|else|while|for|return)$',
            'LOGICAL_OPERATOR': r'^(&&|\|\||!)$',
            'ARITHMETIC_OPERATOR': r'^(\+|-|\*|/|%|\*\*)$',
            'RELATIONAL_OPERATOR': r'^(==|!=|<|>|<=|>=)$'
        }
        
        # Compilar las expresiones regulares para mejor rendimiento
        self.compiled_patterns = {}
        for token_type, pattern in self.patterns.items():
            self.compiled_patterns[token_type] = re.compile(pattern)
    
    def classify_token(self, token):
        """
        Clasifica un token según las expresiones regulares definidas
        
        Args:
            token (str): Cadena a clasificar
            
        Returns:
            str: Tipo de token o 'INVALID' si no coincide con ningún patrón
        """
        for token_type, pattern in self.compiled_patterns.items():
            if pattern.match(token):
                return token_type
        return 'INVALID'
    
    def process_file(self, filename):
        """
        Procesa un archivo de texto línea por línea y clasifica cada token
        
        Args:
            filename (str): Ruta del archivo a procesar
        """
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                tokens = []
                line_number = 0
                
                for line in file:
                    line_number += 1
                    token = line.strip()
                    if token:  # Ignorar líneas vacías
                        token_type = self.classify_token(token)
                        tokens.append({
                            'token': token,
                            'type': token_type,
                            'line': line_number
                        })
                
                # Mostrar resultados en formato de tabla
                self.display_results(tokens)
                
                # Generar reporte estadístico
                self.generate_report(tokens)
                
                return tokens
                
        except FileNotFoundError:
            print(f"Error: No se pudo encontrar el archivo '{filename}'")
            return []
        except Exception as e:
            print(f"Error al procesar el archivo: {e}")
            return []
    
    def display_results(self, tokens):
        """
        Muestra los resultados en formato de tabla
        
        Args:
            tokens (list): Lista de tokens clasificados
        """
        print("\n" + "="*60)
        print("RESULTADOS DE VALIDACIÓN DE TOKENS")
        print("="*60)
        print(f"{'LÍNEA':<6} {'TOKEN':<25} {'TIPO':<20} {'VÁLIDO':<6}")
        print("-"*60)
        
        valid_count = 0
        for token_info in tokens:
            is_valid = "SÍ" if token_info['type'] != 'INVALID' else "NO"
            if is_valid == "SÍ":
                valid_count += 1
                
            # Truncar token si es muy largo
            display_token = token_info['token']
            if len(display_token) > 24:
                display_token = display_token[:21] + "..."
                
            print(f"{token_info['line']:<6} {display_token:<25} {token_info['type']:<20} {is_valid:<6}")
        
        print("-"*60)
        print(f"Total tokens: {len(tokens)}")
        print(f"Tokens válidos: {valid_count}")
        print(f"Tokens inválidos: {len(tokens) - valid_count}")
        print("="*60)
    
    def generate_report(self, tokens):
        """
        Genera un reporte estadístico de los tokens procesados
        
        Args:
            tokens (list): Lista de tokens clasificados
        """
        # Contar tokens por tipo
        type_counts = {}
        for token_info in tokens:
            token_type = token_info['type']
            type_counts[token_type] = type_counts.get(token_type, 0) + 1
        
        # Calcular porcentajes
        total_tokens = len(tokens)
        valid_tokens = total_tokens - type_counts.get('INVALID', 0)
        
        print("\n" + "="*40)
        print("REPORTE ESTADÍSTICO")
        print("="*40)
        print(f"{'TIPO DE TOKEN':<20} {'CANTIDAD':<10} {'PORCENTAJE':<10}")
        print("-"*40)
        
        for token_type, count in sorted(type_counts.items()):
            percentage = (count / total_tokens) * 100 if total_tokens > 0 else 0
            print(f"{token_type:<20} {count:<10} {percentage:.2f}%")
        
        print("-"*40)
        validity_percentage = (valid_tokens / total_tokens) * 100 if total_tokens > 0 else 0
        print(f"{'TOTAL VÁLIDOS':<20} {valid_tokens:<10} {validity_percentage:.2f}%")
        print(f"{'TOTAL INVÁLIDOS':<20} {type_counts.get('INVALID', 0):<10} {(100 - validity_percentage):.2f}%")
        print("="*40)
    
    def validate_single_token(self, token):
        """
        Valida un único token y muestra el resultado
        
        Args:
            token (str): Token a validar
        """
        token_type = self.classify_token(token)
        is_valid = "SÍ" if token_type != 'INVALID' else "NO"
        
        print(f"\nToken: '{token}'")
        print(f"Tipo: {token_type}")
        print(f"Válido: {is_valid}")
        
        return token_type != 'INVALID'

def main():
    """
    Función principal del programa
    """
    validator = TokenValidator()
    
    print("VALIDADOR DE TOKENS CON EXPRESIONES REGULARES")
    print("="*50)
    
    if len(sys.argv) > 1:
        # Si se proporciona un archivo como argumento
        filename = sys.argv[1]
        print(f"Procesando archivo: {filename}")
        validator.process_file(filename)
    else:
        # Modo interactivo
        while True:
            print("\nOpciones:")
            print("1. Validar un archivo de texto")
            print("2. Validar un token individual")
            print("3. Salir")
            
            choice = input("\nSeleccione una opción (1-3): ").strip()
            
            if choice == '1':
                filename = input("Ingrese la ruta del archivo: ").strip()
                if filename:
                    validator.process_file(filename)
                else:
                    print("Debe ingresar una ruta válida.")
            
            elif choice == '2':
                token = input("Ingrese el token a validar: ").strip()
                if token:
                    validator.validate_single_token(token)
                else:
                    print("Debe ingresar un token.")
            
            elif choice == '3':
                print("¡Hasta luego!")
                break
            
            else:
                print("Opción no válida. Por favor, seleccione 1, 2 o 3.")

if __name__ == "__main__":
    main()