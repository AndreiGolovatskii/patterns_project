function draw_grid(canvas, w, h, step) {
  var ctx = canvas.getContext('2d');
  ctx.beginPath(); 
  for (var x=0;x<=w;x+=step) {
    ctx.moveTo(x, 0);
    ctx.lineTo(x, h);
  }

  ctx.strokeStyle = 'rgb(15,15,15)';
  ctx.lineWidth = 1;
  ctx.stroke(); 
  ctx.beginPath(); 
  for (var y=0;y<=h;y+=step) {
    ctx.moveTo(0, y);
    ctx.lineTo(w, y);
  }
  ctx.strokeStyle = 'rgb(15,15,15)';
  ctx.stroke(); 
}

function draw_object(field, object, cell_size, tmp=true) {
    var img = document.createElement('img');
    img.src = object.texture;
    img.id = object.id;
    var width = object.size * cell_size;
    var height = object.size * cell_size;
    var x_start = object.position_x * cell_size;
    var y_start = object.position_y * cell_size;
  
    if (tmp) {
        img.style = `width: ${width}px; height: ${height}px; margin-left: ${x_start}px; margin-top: ${y_start}px; position: absolute; z-index: 1; pointer-events: none`;
    } else {
        img.style = `width: ${width}px; height: ${height}px; margin-left: ${x_start}px; margin-top: ${y_start}px; position: absolute; z-index: 1;`;
    }

    field.append(img);
}

