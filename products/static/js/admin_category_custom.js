function filterCategories(val) {
    categorySelect = $("#id_category");
    categorySelectVal = categorySelect.val();
    $.getJSON(
        "/products/getCategoryByDepartment/", {
            id: val == "" ? 0 : val,
        },
        function (j) {
            var options = '<option value="">---------</option>';
            for (var i = 0; i < j.length; i++) {
                options += '<option value="' + j[i].id + '">' + j[i].name + "</option>";
            }
            categorySelect.html(options);
            categorySelect.val(categorySelectVal);
        }
    );
}


function filterSubCategories(val) {
    subCategorySelect = $("#id_subcategory");
    subCategorySelectVal = subCategorySelect.val();
    $.getJSON(
        "/products/getSubCategoryByCategory/", {
            id: val == "" ? 0 : val,
        },
        function (j) {
            var options = '<option value="">---------</option>';
            for (var i = 0; i < j.length; i++) {
                options +=
                    '<option value="' + j[i].id + '">' + j[i].name + "</option>";
            }
            subCategorySelect.html(options);
            subCategorySelect.val(subCategorySelectVal);
        }
    );
}

const $ = jQuery;
jQuery(document).ready(function () {
    categorySelect = $("#id_category");
    filterCategories($("#id_department").val());
    filterSubCategories($("#id_category").val());

    $("#id_department").change(function () {
        filterCategories($(this).val());
        filterSubCategories("");
    });

    $("#id_category").change(function () {
        filterSubCategories($(this).val());
    })
});