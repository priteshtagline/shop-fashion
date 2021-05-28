function filterProducts(val, similarProductsSelect) {
    similarProductsSelectVal = similarProductsSelect.val();
    $.getJSON(
        "/products/getProductsByProduct/", {
            id: val == "" ? 0 : val,
        },
        function (j) {
            options = "";
            for (var i = 0; i < j.length; i++) {
                options +=
                    '<option value="' + j[i].id + '">' + j[i].title + "</option>";
            }
            similarProductsSelect.html(options);
            similarProductsSelect.val(similarProductsSelectVal);
        }
    );
}

const $ = jQuery;
jQuery(document).ready(function () {
    similarProductsSelect = '';
    if($("#id_similar_products").length != 0){
        similarProductsSelect = $("#id_similar_products");
    }else if ($("#id_vtov_products").length != 0) {
        similarProductsSelect = $("#id_vtov_products");
    }else{
        similarProductsSelect = $("#id_recommended_products");
    }
    
    filterProducts($("#id_product").val(), similarProductsSelect);
    $("#id_product").change(function () {
        filterProducts($(this).val(), similarProductsSelect);
    });
});