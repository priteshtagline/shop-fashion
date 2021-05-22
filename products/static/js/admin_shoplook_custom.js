function filterProducts(val) {
    const productsSelect = $("#id_products");
    const productsSelectVal = productsSelect.val();
    $.getJSON(
        "/products/getProductsByDepartment/", {
            id: val == "" ? 0 : val,
        },
        function (j) {
            options = "";
            for (var i = 0; i < j.length; i++) {
                options +=
                    '<option value="' + j[i].id + '">' + j[i].title + "</option>";
            }
            productsSelect.html(options);
            productsSelect.val(productsSelectVal);
        }
    );
}

const $ = jQuery;
jQuery(document).ready(function () {
    const departmentSelect = $("#id_department");
    filterProducts($("#id_department").val());
    $("#id_department").change(function () {
        filterProducts($(this).val());
    });
});