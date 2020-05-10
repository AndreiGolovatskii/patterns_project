function buy_unit_query(player_id, class_id, x, y) {
    var data  = {
        action_type: 'buy_unit',
        player_id: Number(player_id),
        unit_class_id: Number(class_id),
        position_x:  Number(x),
        position_y:  Number(y)
    };

    $.ajax ({
        type: 'POST',
        url: '/action',
        data: JSON.stringify(data),
        contentType: 'application/json',
        dataType: 'json'
    });
}

function get_game(callback) {
    $.post('/get_game', callback,'json');
}
