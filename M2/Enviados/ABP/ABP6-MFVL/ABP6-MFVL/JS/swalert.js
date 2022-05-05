var fecha = new Date();
var meses = new Array("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre");
var diasSemana = new Array("Domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado");
Swal.fire({
    title: 'Este instante',
    text: 'La fecha de hoy es: ' + diasSemana[fecha.getDay()] + ', ' +
        fecha.getDate() + ' de ' + meses[fecha.getMonth()] + ' de ' + fecha.getFullYear() + ', y son las ' +
        fecha.getHours() + ' horas con ' + fecha.getMinutes() + ' minutos y ' + fecha.getSeconds() +
        ' segundos. ',
    confirmButtonText: '¡A vivirlo!',
    footer: 'Es el tiempo exacto para que disfrutes tu vida.',
    width: '80%',
    padding: '3rm',
    backdrop: true,
    allowsOutsideClick: false,
    allowEscapeKey: false,
    allowEnterKey: false,
    stopKeydownPropagation: false,
    customClass: {
        container: 'sContainer',
        header: 'sHeader',
        title: 'sTitle',
        content: 'sContent',
        footer: 'sFooter',
    }    
});


