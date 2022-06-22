$('#Mantenedor').validate ({
    "rules": {
        "Id": {
            required: true,
        },
        "nombre": {
            required: true,
        },
        "descripcion": {
            required: true,
        },
        "precio": {
            required: true,
        },
        "descuento sub": {
            required: true,
        },
        "descuento oferta": {
            required: true,
        },
    },
    messages: {
        "Id": {
            required: 'Debe ingresar un Id válido',
        },
        "nombre": {
            required: 'Debe ingresar el nombre del producto',
        },
        "nombres": {
            required: 'Debe ingresar el nombres del producto',
        },
        "descripcion": {
            required: 'Debe ingresar una descripcion del producto',
        },
        "precio": {
            required: 'Debe ingresar el precio del producto',
        },
        "descuento sub": {
            required: 'Debe ingresar el descuento del producto para subcriptores',
        },
        "descuento oferta": {
            required: 'Debe ingresar el descuento del producto en oferta',
        },
    }
});