jQuery(function ($) {
  document.getElementById('id_department').addEventListener('change',function(){
    $.getJSON(
      "/products/getCategoryByDepartment/",
      { id: $(this).val() == "" ? 0 : $(this).val() },
      function (j) {
        var options = '<option value="">---------</option>';
        for (var i = 0; i < j.length; i++) {
          options +=
            '<option value="' + j[i].id + '">' + j[i].name + "</option>";
        }
        $("select#id_category").html(options);
      }
    );
  });
});
