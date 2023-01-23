$( document ).ready(function() {
    console.log( "Documento Cargado!" );
    obtener_xml_user( pinta_datos_xmls_user )
    
});

function descarga_xml(){
    let url_formulario_descarga_xml = $('#form_descarga_xml').attr('action')
    let url_input_descarga_xml = $('#input_url_xml_descarga').val()
    $.ajax({
        headers: {'X-CSRFToken': CSRF_TOKEN} ,
        url: url_formulario_descarga_xml ,
        type:'post',
        data:{
            "url_xml": url_input_descarga_xml ,
        },
        dataType:'JSON',
        success: function( request ){
            obtener_xml_user( pinta_datos_xmls_user )
        },
        error: function( request ){
            console.log("Error Error Error")
        },
    })

}

function pinta_datos_xmls_user( json_xmls ){
    
    lista_divs_historial.forEach( divs_ingresados => {
        divs_ingresados.remove()
    });
    
    lista_divs_historial = []
    
    json_xmls.forEach( xml_data => {
        let div_xml_historial = $("#Div_XML_Historial").clone()
        $(div_xml_historial).attr("hidden",false)

        $(div_xml_historial).find("img").attr("src", xml_data["imagen_xml"].replace('/app','') )
        $(div_xml_historial).find("img").attr( "width", "100%" )
        
        $(div_xml_historial).find("#fecha_creacion").text( String('Fecha Creacion: ' + xml_data["fecha_creacion"] ) )
        $(div_xml_historial).find("#id_xml").text( xml_data["id"] )

        $( div_xml_historial ).insertBefore("#Div_XML_Historial")
        
        lista_divs_historial.push( div_xml_historial )

    }); 
}

function obtener_xml_user( func_pinta_datos_xmls_user ){
    $.ajax({
        url: url_obtener_xml_user ,
        type:'get',
        data:{},
        dataType:'JSON',
        success: function( request ){
            console.log( "Exito Objetos Obtenidos!!!" )
            console.log( request )
            func_pinta_datos_xmls_user( request["xml_user"] )
        },
        error: function( request ){
            console.log("Error Objetos no Obtenidos")
        },
    })

}

function descargar_xml_seleccionado(event){
    let div_xml_historial = event.target.parentNode.parentNode.parentNode
    id_xml = $(div_xml_historial).find("#id_xml").text() 
    console.log( url_descargar_xml_document.replace('0', id_xml )  )
    window.location.replace( url_descargar_xml_document.replace('0', id_xml ) );
}

function borrar_xml_seleccionado(event){
    let div_xml_historial = event.target.parentNode
    id_xml = $(div_xml_historial).find("#id_xml").text() 
    //console.log( url_borrar_xml_document.replace('0', id_xml )  )
    $.ajax({
        headers: {'X-CSRFToken': CSRF_TOKEN} ,
        url: url_borrar_xml_document ,
        type:'post',
        data:{ "id_xml":id_xml },
        dataType:'JSON',
        success: function( request ){
            console.log( "Exito Objetos Obtenidos!!!" )
            obtener_xml_user( pinta_datos_xmls_user )
        },
        error: function( request ){
            console.log("Error Objetos no Obtenidos")
        },
    })

}