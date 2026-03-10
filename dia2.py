def saludar(nombre):
    return f"Hola {nombre}"

def sumar(a, b):
    return a + b

print(saludar("Sergio"))
print(sumar(3, 5))

def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: no se puede dividir por cero"
    except TypeError:
        return "Error: los valores deben ser numéricos"
    except Exception as e:
        return f"Error: {e}"

print(dividir(10, 2))
print(dividir(10, 0))

def obtener_campo(registro, campo):
    try:
        return registro[campo]
    except KeyError:
        return f"Error: el campo '{campo}' no existe en el registro"
    except Exception as e:
        return f"Error: {e}"

contacto = {
    "nombre": "Sergio",
    "email": "sergio@gmail.com",
    "telefono": "1234567890"
}

print(obtener_campo(contacto, "email"))
print(obtener_campo(contacto, "empresa"))