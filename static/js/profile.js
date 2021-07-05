$(document).ready(function () {
     $(document).on('submit', 'form.profile-form', function (e) {
         form = $(this);
         e.preventDefault();
         $.ajax({
             url: user_profile_url,
             method: 'post',
             data: form.serialize(),
             dataType: 'json',
             headers: {
                 "X-CSRFToken": form.find("[name=csrfmiddlewaretoken]").val()
             },
             success: function (data) {
                 if (data.status) {
                     if (form.find("input[name='personal_info_change_form']").length) {
                         $('#nameModal').modal("hide");
                         $('#personl-info').html(data.massage);
                     } else if (form.find("input[name='email_change_form']").length) {
                         $('#emailModel').modal("hide");
                         $('#personl-email').html(data.massage);
                     } else {
                         $('#passwordModal').modal("hide");
                     }
                 } else {
                     form.find(":input").each(function () {
                         $(this).css({
                             'border': '1px solid black'
                         }).next('p').remove();
                     })
                     $.each(data.errors, function (key, value) {
                         form.find("#id_" + key).css({
                             'border': '1px solid red'
                         }).after('<p class="error m-0">' + value + '</p>');
                     });
                 }
             },
             error: function (data) {
                 console.log(data);
             },
         });
     });

     $(document).on('click', '.remove-whishlist-product', function (e) {
         e.preventDefault();
         wishlist_record_id = $(this).attr('value');
         $.ajax({
             url: wishlist_url,
             method: 'POST',
             data: {
                 'wishlist_record_id': wishlist_record_id,
                 'wishlist_type': 'remove'
             },
             dataType: 'JSON',
             headers: {
                 "X-CSRFToken": $("[name=csrfmiddlewaretoken]").val()
             },
             success: function (data) {
                 if (data.status) {
                     $('.wishlist_record_' + wishlist_record_id).html('');
                 }
             },
             error: function (data) {
                 console.log(data);
             },
         });
     });

     $(document).on('click', '#remove-wishlist', function (e) {
         e.preventDefault();
         $.ajax({
             url: wishlist_url,
             method: 'POST',
             data: {
                 'wishlist_id': $('#different-wish-list').val(),
                 'wishlist_type': 'remove_wishlist'
             },
             dataType: 'JSON',
             headers: {
                 "X-CSRFToken": $("[name=csrfmiddlewaretoken]").val()
             },
             success: function (data) {
                 if (data.status) {
                     window.location.reload();
                 }
             },
             error: function (data) {
                 console.log(data);
             },
         });
     });


     function customer_wishlist_change(wishlist_id, wishlist_name) {
         $('.product-item').hide();
         $('.wishlist_' + wishlist_id).show();
         $('#wish-list-title').html('<u>' + wishlist_name + '</u>');
     }

     $(document).ready(function () {
         customer_wishlist_change($('#different-wish-list').val(), 'Wish List')
     });

     $(document).on('change', '#different-wish-list', function (e) {
         wishlist_name = $(this).find("option:selected").attr('id');
         if (wishlist_name == 'Wish List') {
             $('#remove-wishlist').hide();
         } else {
             $('#remove-wishlist').show();
         }
         customer_wishlist_change(this.value, wishlist_name);
     });
 });