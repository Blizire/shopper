function delete_product(product_id){
    var xhttp = new XMLHttpRequest();
    xhttp.open("POST", "/admin/delete/" + product_id);
    xhttp.send();
    var element = document.querySelector('[tokenid="' + product_id + '"]');
    element.parentElement.remove()
}

function edit_product(product_id, current_name, current_price){
    // update editing form with product data
    document.querySelector("#update_name").value = current_name;
    document.querySelector("#update_price").value = current_price;
    document.querySelector("#product_update_form").action = "/admin/update/" + product_id;
    // expose editing form

    // hide editing form and clear data
}