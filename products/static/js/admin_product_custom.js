function filterCategories(val) {
  const categorySelect = $("#id_category");
  const categorySelectVal = categorySelect.val();
  $.getJSON(
    "/products/getCategoryByDepartment/",
    {
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

const $ = jQuery;
jQuery(document).ready(function () {
  const categorySelect = $("#id_category");
  filterCategories($("#id_department").val());
  $("#id_department").change(function () {
    filterCategories($(this).val());
  });
});
