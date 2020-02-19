import datetime

def sacarArraySemana(lunes, martes, miercoles, jueves, viernes, sabado, domingo):
    lunesObjeto= {"dia": "lunes", "basura": lunes}
    martesObjeto= {"dia": "martes", "basura": martes}
    miercolesObjeto= {"dia": "miercoles", "basura": miercoles}
    juevesObjeto= {"dia": "jueves", "basura": jueves}
    viernesObjeto= {"dia": "viernes", "basura": viernes}
    sabadoObjeto= {"dia": "sabado", "basura": sabado}
    domingoObjeto= {"dia": "domingo", "basura": domingo}

    array = [lunesObjeto, martesObjeto, miercolesObjeto, juevesObjeto, viernesObjeto, sabadoObjeto, domingoObjeto]
    return array

def sacarDiaSemanaOrdinal():
    # Me devuelve el dia de la semana, donde 0 es lunes y 6 es domingo
    return datetime.datetime.today().weekday()

def sacarDiaSemanaNombre():
    arrayDiasSemana = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo']
    diaOrdinal = sacarDiaSemanaOrdinal()
 
    return arrayDiasSemana[diaOrdinal]
