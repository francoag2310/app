var tblSede;

function cargarTabla() {
    tblSede = $('.mydatatable').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        fixedColumns: {
            heightMatch: 'none'
        },
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {'accion': 'obtener_sedes'},
            dataSrc: ""
        },
        columns: [
            {data: "id"},
            {data: "ubicacion"},
            {data: null},
        ],
        columnDefs: [{
            "orderable": false,
            targets: [-1],
            class: 'text-center',
            render: function (data, type, row, meta) {
                var botones = '<a rel="editar" class="btn btn-warning btn-xs" >Modificar<span class="ml-1"></span><i class="far fa-edit"></i></a> ';
                botones += '<a rel="eliminar" class="btn btn-danger btn-xs"> <i class="far fa-trash-alt"></i></a>';
                return botones;
            }
        }],
    })
};

$(function () {
    cargarTabla();

    $('.mydatatable tbody').on('click', 'a[rel="editar"]', function () {
        var tr = tblSede.cell($(this).closest('td, li')).index();
        var data = tblSede.row(tr.row).data();
        $('input[name="accion"]').val('editar')
        $('input[name="id"]').val(data.id)
        $('input[name="ubicacion"]').val(data.ubicacion)
        $('#exampleModal').modal('show')
    });

    $('.mydatatable tbody').on('click', 'a[rel="eliminar"]', function () {
        var tr = tblSede.cell($(this).closest('td, li')).index();
        var data = tblSede.row(tr.row).data();
        data = Object.assign(data, {'accion': 'eliminar'})

        var form = new FormData();
        for (var key in data) {
            form.append(key, data[key]);
        }

        var ruta_destino = window.location.pathname
        enviarConAjax(form, ruta_destino)
    })

    $('#exampleModal').on('hidden.bs.modal', function () {
        $(this).find('form').trigger('reset');
        $('.div-error').hide();
    })

});