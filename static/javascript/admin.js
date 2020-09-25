function delete_product(product_id){
    var xhttp = new XMLHttpRequest();
    xhttp.open("POST", "/admin/delete/" + product_id);
    xhttp.send();
    var element = document.querySelector('[tokenid="' + product_id + '"]');
    element.parentElement.remove()
}

function edit_product(product_id){
    // update editing form with product data
    form = document.querySelector("#product_update_form")

    //expose editing form


    // send update post request


    // close editing form and clear data
}