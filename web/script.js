class DrawingController {
    constructor(buy_callback, get_unit_proto) {
        this.buy_callback = buy_callback;
        this.get_unit_proto = get_unit_proto;
        this.canvas = document.getElementById("canvas");
        this.field = $("#field");
        this.selected_store_item = undefined;
        this.cell_size = 30;

        this.canvas.onmousemove = this.update_tmp_object.bind(this);
        this.canvas.onmouseup = this.buy_selected_unit.bind(this);

        this.selected_store_item = undefined;

        this.store = $("#store");
        this.store.slideToggle();

        this.wallet_element = $("#wallet");
    }

    update_tmp_object(evt) {
        $('#tmp_object').remove();
   
        if (this.selected_store_item != undefined) {
            var x = evt.offsetX,
                y = evt.offsetY;
    
            x = (x - x % this.cell_size) / this.cell_size;
            y = (y - y % this.cell_size) / this.cell_size;
            let tmp_object = this.get_unit_proto(this.selected_store_item);
            tmp_object.class_id = "tmp_object";
            tmp_object.position_x = x;
            tmp_object.position_y = y;
            tmp_object.id = "tmp_object";
            draw_object(this.field, tmp_object, this.cell_size);
        }
    }

    buy_selected_unit(evt) {
        $('#tmp_object').remove();
        if (this.selected_store_item != undefined) {
            var x = evt.offsetX,
                y = evt.offsetY;
 
            x = (x - x % this.cell_size) / this.cell_size;
            y = (y - y % this.cell_size) / this.cell_size;
            
            this.buy_callback(this.selected_store_item, x, y);
            this.selected_store_item = undefined;
        }
    }

    update_canvas(width_cells, height_cells) {
        let w = width_cells * this.cell_size;
        let h = height_cells * this.cell_size;
       
        this.canvas.height = h;
        this.canvas.width = w;

        draw_grid(this.canvas, w, h, this.cell_size);
    }

    set_selected_store_item(id) {
        this.selected_store_item = id;
    }

    add_store_item(item) {
        var new_item = document.createElement("button");
        new_item.id = item.class_id;

        var img = document.createElement("img")
        img.src = item.texture
        img.width = 80
        new_item.appendChild(img)

        var title = document.createElement("div");
        title.textContent = item.name;
        new_item.appendChild(title)

        this.set_cost(item.price, new_item);

        this.store.append(new_item);
        $(`#${item.class_id}`).click(this, DrawingController.select_store_item);
    }

    static select_store_item(evt) {
        var id = $(this)[0].id;
        let store = evt.data;
        if (store.selected_store_item == id) {
            store.selected_store_item = undefined;
        } else {
            store.selected_store_item = id;
        }
        console.log(`selected item: ${store.selected_store_item}`);
    }

    set_cost(cost, element) {
        var money = document.createElement("div");
        money.textContent = "money: " + cost.money.toFixed(2);

        var oil = document.createElement("div");
        oil.textContent = "oil: " + cost.oil.toFixed(2);

        var electricity = document.createElement("div");
        electricity.textContent = "electricity: " + cost.electricity.toFixed(2);


        element.append(money);
        element.append(oil);
        element.append(electricity);
    }

    update_wallet(wallet) {
        this.wallet_element.empty();
        this.set_cost(wallet, this.wallet_element);
    }

    add_unit(unit) {
        unit.id = unit.unit_id;
        console.log(unit);
        draw_object(this.field, unit, this.cell_size);
    }

    clear_market() {
        this.store.empty();
    }


    rm_unit(id) {
        $(`#id`).remove();
    }

    update_terrain(texture) {
        $("#terrain").empty();

        var img = document.createElement("img")
        img.src = texture
        img.width = this.canvas.width;
        img.height = this.canvas.height;
        $("#terrain").append(img)
    }
}

class Game {
    constructor() {
        this.draw_controller = new DrawingController(this.buy_unit.bind(this),
                                                     this.get_unit_proto.bind(this));
        this.player_id = 0;
        this.market_units = undefined;
        this.units = {}

        setInterval(this.update.bind(this), 500);
    }

    buy_unit(class_id, x, y) {
        console.log(`buy ${class_id}`);
        buy_unit_query(this.player_id, class_id, x, y);
        this.update();
    }
    update() {
        get_game(this.update_game.bind(this));
    }

    update_game(game_data) {
        console.log(game_data);
        
        this.draw_controller.update_canvas(game_data.terrain.width, game_data.terrain.height);
        this.draw_controller.update_terrain(game_data.terrain.texture);
        
        this.draw_controller.update_wallet(game_data.players[this.player_id].wallet);

        let old_units = this.market_units;
        this.market_units = {}
        for (let i = 0; i < game_data.market.length; i++) {
            let unit = game_data.market[i];
            this.market_units[unit.class_id] = unit;
        }

        if (JSON.stringify(this.market_units) != JSON.stringify(old_units)) {
            this.draw_controller.clear_market();
            game_data.market.forEach(this.draw_controller.add_store_item.bind(this.draw_controller))
        }
        
        let new_units = {}
        for (let i = 0; i < game_data.players[this.player_id].units.length; ++i) {
            let unit = game_data.players[this.player_id].units[i];
            new_units[unit.unit_id] = unit;
            if (!(unit.unit_id in this.units)) {
                this.draw_controller.add_unit(unit);
                delete this.units[unit.unit_id];
            }
            new_units[unit.unit_id] = unit;
        }
        let to_rm = Object.keys(this.units);
        for (let i = 0; i < to_rm.length; ++i) {
            this.draw_controller.rm_unit(to_rm[i].unit_id);
        }

        this.units = new_units;
    }

    get_unit_proto(class_id) {
        return this.market_units[class_id];
    }
}

let game = new Game();
