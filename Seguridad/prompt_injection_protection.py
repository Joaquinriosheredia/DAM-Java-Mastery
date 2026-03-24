[CÓDIGO]
import re

class PromptInjectionProtection:
    def __init__(self, allowed_chars):
        self.allowed_chars = allowed_chars  # Define caracteres permitidos
        
    def validate_input(self, input_string):
        """
        Valida la entrada del usuario contra una expresión regular basada en los caracteres permitidos.
        
        Args:
            input_string (str): El prompt o entrada proporcionado por el usuario.

        Returns:
            bool: True si no hay inyección de prompts detectada, False en caso contrario.
        """
        # Compila una expresión regular que coincide con cualquier carácter que NO esté permitido
        pattern = re.compile(f"[^{self.allowed_chars}]")
        
        # Verifica si existe algún caracter prohibido en la entrada del usuario
        if pattern.search(input_string):
            return False  # Inyección detectada
        
        return True  # Pasó la validación

    def clean_input(self, input_string):
        """
        Limpia cualquier carácter que no sea permitido en una cadena de entrada.
        
        Args:
            input_string (str): El prompt o entrada proporcionado por el usuario.

        Returns:
            str: La entrada limpia sin caracteres prohibidos.
        """
        # Crea un patrón para la limpieza basada en los caracteres permitidos
        pattern = re.compile(f"[^{self.allowed_chars}]")
        
        # Reemplaza cualquier carácter no permitido con un vacío
        cleaned_string = pattern.sub("", input_string)
        
        return cleaned_string

# Ejemplo de uso:
if __name__ == "__main__":
    allowed_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ,.!?"
    
    # Crear una instancia del mecanismo de defensa
    protection = PromptInjectionProtection(allowed_chars=allowed_characters)
    
    user_input = input("Ingrese un prompt: ")
    
    if not protection.validate_input(user_input):
        print("Alerta! Se ha detectado inyección de prompts.")
    else:
        cleaned_prompt = protection.clean_input(user_input)
        print(f"Prompt limpio: {cleaned_prompt}")