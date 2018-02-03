
$('.good').click(function () {
        var item_id = this.id;
        $.ajax('item/' + item_id, {
            success: function (result) {
                $('.body').html(result)
            }
        });
    });