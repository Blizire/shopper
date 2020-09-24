function delete_product(product_id){
    var xhttp = new XMLHttpRequest();
    xhttp.open("POST", "/admin/delete/" + product_id);
    xhttp.send();
    var element = document.querySelector('[tokenid="' + product_id + '"]');
    element.parentElement.remove()
}