#Saul Eliseo Aparicio Vivar - 21760641
# Algoritmo para convertir números romanos a decimales y viceversa

# Diccionario de números romanos a decimales
ROMAN_TO_DECIMAL = {
    'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
}

# Diccionario de decimales a números romanos
DECIMAL_TO_ROMAN = [
    (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
    (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
    (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
    (1, 'I')
]

# Función para convertir número romano a decimal
def roman_to_decimal(roman):
    roman = roman.upper()
    total = 0
    prev_value = 0

    # Verifica si la secuencia es válida
    for i in range(len(roman) - 1, -1, -1):
        current_value = ROMAN_TO_DECIMAL.get(roman[i], -1)
        
        if current_value == -1:
            raise ValueError(f"Caracter no válido: {roman[i]}")
        
        # Si es menor que el valor anterior, restamos
        if current_value < prev_value:
            total -= current_value
        else:
            total += current_value
        
        prev_value = current_value

    # Verifica si la secuencia tiene más repeticiones de las permitidas
    if not validate_roman(roman):
        raise ValueError("La secuencia romana no es válida según las reglas de repetición y resta.")
        
    # Verifica que la secuencia no contenga patrones no permitidos
    if not is_valid_roman_sequence(roman):
        raise ValueError("La secuencia romana tiene un patrón no permitido.")
        
    return total

# Función para convertir decimal a número romano
def decimal_to_roman(number):
    if not (1 <= number <= 3999):
        raise ValueError("El número debe estar entre 1 y 3999")

    result = ''
    for value, symbol in DECIMAL_TO_ROMAN:
        while number >= value:
            result += symbol
            number -= value
    return result

# Función para validar secuencias romanas según las reglas de repetición y resta
def validate_roman(roman):
    # Reglas de repetición
    # No se permite más de tres repeticiones consecutivas de 'I', 'X', 'C', 'M'
    # No se permite más de dos repeticiones consecutivas de 'V', 'L', 'D'
    repetitions = {'I': 3, 'X': 3, 'C': 3, 'M': 3, 'V': 1, 'L': 1, 'D': 1}

    for char in repetitions:
        if roman.count(char * (repetitions[char] + 1)) > 0:
            return False

    # Verifica si la secuencia de caracteres cumple con las reglas de sustracción
    invalid_patterns = ['IIII', 'VV', 'LL', 'DD', 'IL', 'IC', 'ID', 'IM', 'XD', 'XM', 'LC', 'LD', 'LM']
    for pattern in invalid_patterns:
        if pattern in roman:
            return False
    
    return True

# Función para verificar si una secuencia romana es válida (sin patrones incorrectos como "IXI")
def is_valid_roman_sequence(roman):
    # Comprobación de patrones no válidos
    invalid_combinations = ['IXI', 'VIV', 'XIX', 'LXL', 'DCD', 'IIV', 'VV', 'LL', 'DD']
    for pattern in invalid_combinations:
        if pattern in roman:
            return False
    return True

# Función principal de conversión
def convert(entrada):
    # Si la entrada es un número romano
    if isinstance(entrada, str):
        try:
            decimal_value = roman_to_decimal(entrada)
            print(f"El número romano {entrada} es igual a {decimal_value} en decimal.")
        except ValueError as e:
            print(f"Error: {e}")
    
    # Si la entrada es un número decimal
    elif isinstance(entrada, int):
        try:
            if entrada <= 0 or entrada > 3999:
                raise ValueError("El número debe ser mayor que 0 y menor o igual a 3999.")
            roman_value = decimal_to_roman(entrada)
            print(f"El número decimal {entrada} es igual a {roman_value} en romano.")
        except ValueError as e:
            print(f"Error: {e}")

#Convertir
convert('MMMCMXCIX')   # Convertir de romano a decimal
convert(3999)    # Convertir de decimal a romano
