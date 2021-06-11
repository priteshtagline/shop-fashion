(function ($) {
    'use strict';

    function carousel_slider() {
        $('.carousel_slider').each(function () {
            var $carousel = $(this);
            $carousel.owlCarousel({
                dots: $carousel.data("dots"),
                loop: $carousel.data("loop"),
                items: $carousel.data("items"),
                margin: $carousel.data("margin"),
                mouseDrag: $carousel.data("mouse-drag"),
                touchDrag: $carousel.data("touch-drag"),
                autoHeight: $carousel.data("autoheight"),
                center: $carousel.data("center"),
                nav: $carousel.data("nav"),
                rewind: $carousel.data("rewind"),
                navText: ['<i class="fal fa-chevron-left navigator-left"></i>', '<i class="fal fa-chevron-right navigator-right"></i>'],
                autoplay: $carousel.data("autoplay"),
                animateIn: $carousel.data("animate-in"),
                animateOut: $carousel.data("animate-out"),
                autoplayTimeout: $carousel.data("autoplay-timeout"),
                smartSpeed: $carousel.data("smart-speed"),
                responsive: $carousel.data("responsive")
            });
        });
    }

    $(document).on("ready", function () {
        carousel_slider();
    });

})(jQuery);

$(".toggle-password").click(function () {

    $(this).toggleClass("toggle-password");
    var input = $($(this).attr("toggle"));
    if (input.attr("type") == "password") {
        input.attr("type", "text");
        $(this).text("Hide")
    } else {
        input.attr("type", "password");
        $(this).text("Show")
    }
});

$(document).ready(function () {

    $('#first_form').submit(function (e) {
        e.preventDefault();
        var email = $('#email').val();
        var password = $('#password').val();

        $(".error").remove();
        if (email.length < 1) {
            $('#email').after('<p class="error m-0">This field is required</p>');
        }
        if (password.length < 1) {
            $('#password').after('<p class="error m-0">This field is required</p>');
        }
    });

    $('#second_form').submit(function (e) {
        e.preventDefault();
        var fname = $('#fname').val();
        var lname = $('#lname').val();
        var email = $('#email').val();
        var password = $('#password').val();

        $(".error").remove();

        if (fname.length < 1) {
            $('#fname').after('<p class="error m-0">This field is required</p>');
        }
        if (lname.length < 1) {
            $('#lname').after('<p class="error m-0">This field is required</p>');
        }
        if (email.length < 1) {
            $('#email').after('<p class="error m-0">This field is required</p>');
        }
        if (password.length < 1) {
            $('#password').after('<p class="error m-0">This field is required</p>');
        }
    });

    $('#change-mail').submit(function (e) {
        e.preventDefault();
        var newEmail = $('#new-email').val();
        var confirmEmail = $('#confirm-email').val();
        var password = $('#password').val();

        $(".error").remove();

        if (newEmail.length < 1) {
            $('#new-email').after('<p class="error m-0">This field is required</p>');
        }
        if (confirmEmail.length < 1) {
            $('#confirm-email').after('<p class="error m-0">This field is required</p>');
        }
        if (password.length < 1) {
            $('#password').after('<p class="error m-0">This field is required</p>');
        }
    });

    // $('#change-password').submit(function (e) {
    //     e.preventDefault();
    //     var current = $('#current-password').val();
    //     var newPass = $('#new-password').val();

    //     $(".error").remove();

    //     if (current.length < 1) {
    //         $('#current-password').after('<p class="error m-0">This field is required</p>');
    //     }

    //     if (newPass.length < 1) {
    //         $('#new-password').after('<p class="error m-0">This field is required</p>');
    //     }
    // });

    // $('#change-name').submit(function (e) {
    //     e.preventDefault();
    //     var fname = $('#first-name').val();
    //     var lname = $('#last-name').val();

    //     $(".error").remove();

    //     if (fname.length < 1) {
    //         $('#first-name').before('<p class="error m-0">This field is required</p>');
    //     }
    //     if (lname.length < 1) {
    //         $('#last-name').after('<p class="error m-0">This field is required</p>');
    //     }
    // });

});

$(document).ready(function () {
    $("input").blur(function () {
        if (!$(this).val()) {
            $("#nameError").css("display", "block");
            $("#nameError").empty().append("<span class='error'><span aria-hidden='true'></span> Please enter your name</span>");
            $("#name").attr("aria-invalid", "true");
        } else {
            $("#nameError").css("display", "none");
            $("#nameError").text("");
            $("#name").attr("aria-invalid", "false");
        }
    });
});

$(".button-collapse").click(function () {

    $("body").toggleClass("side-nav-open");
    $('#overlay').fadeToggle("slow", "swing");

});

$('#overlay').click(function () {
    $('#overlay').fadeOut('slow');
    $("body").toggleClass("side-nav-open");
});

$(document).ready(function () {
    $(".nav-pills a").click(function () {
        $(this).tab('show');
    });
});

$(document).ready(function () {
    $(".user-btn").click(function () {

        $("body").toggleClass("side-menu-open");
        $('#overlay').fadeToggle("slow", "swing");

    });
});

$(document).ready(function () {
    $('#overlay').click(function () {
        $('#overlay').fadeOut('slow');
        $("body").toggleClass("side-menu-open");
    });
});

$(document).ready(function () {
    $('.nav-pills a').click(function () {
        $('#overlay').fadeOut('slow');
        $("body").toggleClass("side-menu-open");
    });
});
if ($(".grid").length > 0) {
    $('.grid').masonry({
        itemSelector: '.grid-item',
        columnWidth: '.grid-sizer',
        percentPosition: true
    });
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}

var image = $('#product_img');
//var zoomConfig = {};
var zoomActive = false;

zoomActive = !zoomActive;
if (zoomActive) {
    if ($(image).length > 0) {
        $(image).elevateZoom({
            cursor: "crosshair",
            easing: true,
            gallery: 'pr_item_gallery',
            zoomType: "inner",
            galleryActiveClass: "active"
        });
    }
} else {
    $.removeData(image, 'elevateZoom'); //remove zoom instance from image
    $('.zoomContainer:last-child').remove(); // remove zoom container from DOM
}

$.magnificPopup.defaults.callbacks = {
    open: function () {
        $('body').addClass('zoom_image');
    },
    close: function () {
        // Wait until overflow:hidden has been removed from the html tag
        setTimeout(function () {
            $('body').removeClass('zoom_image');
            $('body').removeClass('zoom_gallery_image');
            //$('.zoomContainer:last-child').remove();// remove zoom container from DOM
            $('.zoomContainer').slice(1).remove();
        }, 100);
    }
};

// Set up gallery on click
var galleryZoom = $('#pr_item_gallery');
galleryZoom.magnificPopup({
    delegate: 'a',
    type: 'image',
    gallery: {
        enabled: true
    },
    callbacks: {
        elementParse: function (item) {
            item.src = item.el.attr('data-zoom-image');
        }
    }
});

// Zoom image when click on icon
$('.product_img_zoom').on('click', function () {
    var atual = $('#pr_item_gallery a').attr('data-zoom-image');
    $('body').addClass('zoom_gallery_image');
    $('#pr_item_gallery .item').each(function () {
        if (atual == $(this).find('.product_gallery_item').attr('data-zoom-image')) {
            return galleryZoom.magnificPopup('open', $(this).index());
        }
    });
});

$('.plus').on('click', function () {
    if ($(this).prev().val()) {
        $(this).prev().val(+$(this).prev().val() + 1);
    }
});
$('.minus').on('click', function () {
    if ($(this).next().val() > 1) {
        if ($(this).next().val() > 1) $(this).next().val(+$(this).next().val() - 1);
    }
});

$(document).ready(function () {
    $(".megamenu").on("click", function (e) {
        e.stopPropagation();
    });
});

$('.filter').affix({
    offset: {
        top: $('.filter').offset().top,
        bottom: ($('footer').outerHeight(true) + $('.application').outerHeight(true)) + 40
    }
});

$(document).ready(function () {
    $(".error").remove();
    $('#current-password').blur(function () //whenever you click off an input element

        {
            if (!$('#current-password').val()) { //if it is blank. 
                $('#current-password').after('<p class="error m-0">This field is required</p>');
            }
        })
})