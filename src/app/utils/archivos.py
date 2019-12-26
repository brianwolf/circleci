def nombre_completo(nombre: str, extension: str):
    '''
    Devuelve el nombre con la extension
    '''
    if '.' in extension:
        extension = '.' + extension

    if extension not in nombre:
        return nombre + '.' + extension

    return nombre


def nombre_extension(nombre_completo: str):
    '''
    Devuelve el nombre separado de la extension
    '''
    if '.' in nombre_completo:
        nombre = nombre_completo.split('.')[0]
        extension = nombre_completo.split('.')[1]

        return nombre, extension

    return nombre_completo, ''