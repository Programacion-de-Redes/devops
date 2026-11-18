def es_correo_valido(correo):
    """Devuelve True si el correo tiene @ y un punto después del @. Este es otra prueba""" 
    if "@" not in correo:
        return False

    usuario, dominio = correo.split("@", 1)
    if usuario == "" or "." not in dominio:
        return False
    return True
