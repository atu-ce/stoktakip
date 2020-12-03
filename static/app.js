var x = 0;
$('#apireq1').click(function () {
    $.ajax({
        url: "http://127.0.0.1:5000/api/stocks/",
        dataType: "json",
        success: function (data) {
            console.log('gelen data1: ', data)

            if (x == 0) {
                var info = document.createElement("P");
                info.innerHTML = '<h4 class="purpletext">Stok Adı</h4>'
                var item = document.getElementById("infoStok");
                item.appendChild(info);
            };

            data.forEach(obje => {
                x = x + 1
                if (obje.id == x) {
                    var stok = document.createElement("P");
                    stok.innerHTML = "<ul><li id='stok" + obje.id + "'></li></ul>"
                    var element = document.getElementById("stokId");
                    element.appendChild(stok);
                };
            });

            data.forEach(i => {
                $('#stok' + i.id).text(i.stock_name);
            });
        }
    });

});

var y = 0;
$('#apireq2').click(function () {
    $.ajax({
        url: "http://127.0.0.1:5000/api/stocks/",
        dataType: "json",
        success: function (data) {
            console.log('gelen data2: ', data)

            if (y == 0) {
                var info = document.createElement("P");
                info.innerHTML = '<h4 class="purpletext">Tedarikçi Adı</h4>'
                var item = document.getElementById("infoSupplier");
                item.appendChild(info);
            };

            data.forEach(obje => {
                y = y + 1
                if (obje.id == y) {
                    var supplier = document.createElement("P");
                    supplier.innerHTML = "<ul><li id='supplier" + obje.id + "'></li></ul>"
                    var element = document.getElementById("supplierId");
                    element.appendChild(supplier);
                };
            });

            data.forEach(i => {
                $('#supplier' + i.id).text(i.supplier_name);
            });
        }
    });
});

var z = 0;
$('#updateStok').click(function () {
    $.ajax({
        url: "http://127.0.0.1:5000/api/stocks/",
        dataType: "json",
        success: function (data) {

            if (z == 0) {
                var info = document.createElement("P");
                info.innerHTML = '<h4>    Güncellemek istediğiniz stok bilgisini seçiniz.</h4>'
                var item = document.getElementById("infoUpdateStokId");
                item.appendChild(info);
            };

            data.forEach(obje => {
                z = z + 1
                console.log("z: ",z)
                if (obje.id == z) {
                    console.log('gelen data3: ', data);

                    var text = document.createElement("P");
                    text.innerHTML = `<div class="collapse" id="updateStokAndSupplier${obje.id}"><div class="card card-body" id="formUpdateStokAndSupplier${obje.id}">Çalışıyor: ${obje.id}</div></div>`
                    console.log(obje.id);
                    console.log(obje);
                    var item = document.getElementById("updateText");
                    item.appendChild(text);

                    var update = document.createElement("P");
                    update.innerHTML = '<button type="button" id="update' + obje.id + '" class="btn btn-outline-danger btn-block" data-toggle="collapse" data-target="#updateStokAndSupplier' + obje.id + '" aria-expanded="false" aria-controls="updateStokAndSupplier' + obje.id + '"></button>'
                    var element = document.getElementById("updateStokId");
                    element.appendChild(update);
                };
            });

            data.forEach(i => {
                $('#update' + i.id).text(`Stok adı: ${i.stock_name}, Tedarikçi: ${i.supplier_name}`);
            });
        }
    });
});
