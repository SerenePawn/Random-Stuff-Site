$(document).ready(function () {
    $('.link-1').click(function () {
        $('#mask').show();
        $('.signIn').show();
    });
    $('#mask').click(function () {
        $('#mask').hide();
        $('.signIn').hide();
    });
    $('.link-2').click(function () {
        window.open('/signup')
    });
    $('.link-3').click(function () {
        window.open('/faq')
    });
    $('.menu').click(function () {
       $('.menuBackground').slideToggle();
    });

    $('.good').click(function () {
        var item_id = this.id;
        $.ajax('item/' + item_id, {
            data: {'ajax': 'used'},
            success: function (result) {
                $('.body').html(result);
                window.history.replaceState({}, '', '/item/' + item_id);
            }
        });
    });
});