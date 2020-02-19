import datetime

def sacarArraySemana(lunes, martes, miercoles, jueves, viernes, sabado, domingo):
    lunesObjeto= {"dia": 0, "basura": lunes}
    martesObjeto= {"dia": 1, "basura": martes}
    miercolesObjeto= {"dia": 2, "basura": miercoles}
    juevesObjeto= {"dia": 3, "basura": jueves}
    viernesObjeto= {"dia": 4, "basura": viernes}
    sabadoObjeto= {"dia": 5, "basura": sabado}
    domingoObjeto= {"dia": 6, "basura": domingo}

    array = [lunesObjeto, martesObjeto, miercolesObjeto, juevesObjeto, viernesObjeto, sabadoObjeto, domingoObjeto]
    return array

def sacarDiaSemanaOrdinal():
    # Me devuelve el dia de la semana, donde 0 es lunes y 6 es domingo
    return datetime.datetime.today().weekday()

def sacarDiaSemanaNombre():
    arrayDiasSemana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
    diaOrdinal = sacarDiaSemanaOrdinal()
 
    return arrayDiasSemana[diaOrdinal]

def sacarPasadoMañanaDiaSemanaNombre():
    arrayDiasSemana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
    diaOrdinal = sacarDiaSemanaOrdinal() +1
 
    return arrayDiasSemana[diaOrdinal] 