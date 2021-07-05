 $(function () {
     $('.lazy').Lazy({
         effect: 'show',
     });
 });

 $(document).ready(function () {
     $(document).on('submit', 'form.email-subscribe-form', function (e) {
         form = $(this);
         e.preventDefault();
         $.ajax({
             url: email_subscribe_url,
             method: 'POST',
             data: form.serialize(),
             dataType: 'JSON',
             headers: {
                 "X-CSRFToken": form.find("[name=csrfmiddlewaretoken]").val()
             },
             success: function (data) {
                 if (data.status) {
                     form.find("p").empty().show().html(data.message).delay(1500).fadeOut(300);
                     setTimeout(function () {
                         form.find("input[type=email]").val("");
                     }, 1500);
                 }
             },
             error: function (data) {
                 console.log(data);
             },
         });
     });
 });

 $(document).on('click', '.like-product', function (e) {
     e.preventDefault();
     selector_heart = $(this).find('i')
     like_action = $.inArray('far', selector_heart.attr('class').split(' ')) != -1 ? 'add' : 'remove'
     $.ajax({
         url: like_product_url,
         method: 'POST',
         data: {
             'product_id': $(this).attr('value'),
             'like_action': like_action
         },
         dataType: 'JSON',
         headers: {
             "X-CSRFToken": $("[name=csrfmiddlewaretoken]").val()
         },
         success: function (data) {
             if (data.status) {
                 selector_heart.toggleClass('fa');
                 selector_heart.toggleClass('far');
             } else {
                 if (data.message == 'login_required') {
                    window.location = login_url;
                 }
             }
         },
         error: function (data) {
             console.log(data);
         },
     });
 });