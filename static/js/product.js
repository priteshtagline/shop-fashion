$(document).ready(function () {
    function wishlist_update(wishlist_name, wishlist_url) {
        $.ajax({
            url: wishlist_url,
            method: 'POST',
            data: {
                'wishlist_type': 'add',
                'product_id': product_id,
                'wishlist_name': wishlist_name,
            },
            dataType: 'JSON',
            headers: {
                "X-CSRFToken": $("[name=csrfmiddlewaretoken]").val()
            },
            success: function (data) {
                if (data.status) {
                    if (wishlist_name != 'wish list'){
                        $("#exampleModal").modal("hide");
                    }
                } else {
                    $('#new-wish-list-name').after('<p class="text-danger" style="padding-left:30px">' +
                        data.message + '</p>')
                    if (data.message == 'login_required') {
                        window.location = login_url;
                    }
                }
            },
            error: function (data) {
                console.log(data);
            },
        });
    }

    $(document).on('click', '.move-diffrent-wishlist-btn', function (e) {
        $('.move-diffrent-wishlist').css('display', 'none');
        $('.wish-list-info-btn').css('display', 'flex');
        $('.back-modal-btn').css('visibility', 'visible');
        $('#nav-home').toggleClass('show active');
    });
    
    $(document).on('click', '.back-modal-btn', function (e) {
        $('.move-diffrent-wishlist').css('display', 'block');
        $('.wish-list-info-btn').css('display', 'none');
        $('.back-modal-btn').css('visibility', 'hidden');
        $('#nav-home').toggleClass('show active');
    });


    $(document).on('click', '.wishlist-btn', function (e) {
        wishlist_update('wish list', wishlist_url);
    });

    $(document).on('click', '.wishlist-btn-move', function (e) {
        wish_list_name = $('input[name="wish-list-name"]:checked').val();
        if (wish_list_name === undefined) {
            $('#new-wish-list-name').after('<p class="text-danger" style="padding-left:30px">select at list one wihslist</p>');
        } else if (wish_list_name == 0) {
            wish_list_name = $("#new-wish-list-name").val();
            wish_list_name == '' ? $("#new-wish-list-name").css('border', '1px solid red') : wishlist_update(wish_list_name, wishlist_url);;
        } else {
            wishlist_update(wish_list_name, wishlist_url);
        }
    });

});