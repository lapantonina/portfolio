$( document ).ready( addEventListener );

  let x = 1;
  let y = 1;
  let current_cell_id = "cell_" + x + "_" + y;
  $("#" + current_cell_id).removeClass("invsbl");


let keys = {};
addEventListener("keydown", function(event) { 
  keys[event.keyCode] = true;
  switch(event.keyCode){
    case 37: case 39: case 38:  case 40: event.preventDefault()
    if (event.keyCode == 37)
      move_left("left");
    else if (event.keyCode == 38)
      move_up("up");
    else if (event.keyCode == 39)
      move_right("right");
    else if (event.keyCode == 40)
      move_down("down");
    }
  },
false);

addEventListener('keyup', function(event) {
  keys[event.keyCode] = false;
  },
false);


function move_down() {
       
  let down_ceil_id = "ceil_" + (x+1) + "_" + y;
  if ($("#"+down_ceil_id).hasClass("finish")) {
    if (!document.getElementById('tracking').checked) {
      $("#" + current_cell_id).addClass("invsbl");
    }
    else {
      $("#" + current_cell_id).addClass("semi-invsbl");
    }
    let maze = document.getElementById("maze")
    let gif = document.getElementById("gif")
    maze.classList.add("secret");
    gif.classList.remove("secret");      
  }

  else if (!document.getElementById(down_ceil_id)) {
    if (!document.getElementById('tracking').checked) {
      $("#" + current_cell_id).addClass("invsbl");
    }
    else {
      $("#" + current_cell_id).addClass("semi-invsbl");
    }
    x = x + 1;
    current_cell_id = "cell_" + x + "_" + y;
    $("#" + current_cell_id).removeClass("invsbl");
    $("#" + current_cell_id).removeClass("semi-invsbl");
  }
}


function move_up() {
       
  let up_ceil_id = "ceil_" + x + "_" + y;
  if (!document.getElementById(up_ceil_id))  {
    if (!document.getElementById('tracking').checked) {
      $("#" + current_cell_id).addClass("invsbl");
    }
    else {
      $("#" + current_cell_id).addClass("semi-invsbl");
    }
    x = x - 1;
    current_cell_id = "cell_" + x + "_" + y;
    $("#" + current_cell_id).removeClass("invsbl");
    $("#" + current_cell_id).removeClass("semi-invsbl");
  }
}


function move_left() {
     
  let left_wall_id = "wall_" + x + "_" + y;
  if (!document.getElementById(left_wall_id))  {
    if (!document.getElementById('tracking').checked) {
      $("#" + current_cell_id).addClass("invsbl");
    }
    else {
      $("#" + current_cell_id).addClass("semi-invsbl");
    }
    y = y - 1;
    current_cell_id = "cell_" + x + "_" + y;
    $("#" + current_cell_id).removeClass("invsbl");
    $("#" + current_cell_id).removeClass("semi-invsbl");
  }   
}


function move_right() {

  let right_wall_id = "wall_" + x + "_" + (y+1);
  if (!document.getElementById(right_wall_id))  {
    if (!document.getElementById('tracking').checked) {
      $("#" + current_cell_id).addClass("invsbl");
    }
    else {
      $("#" + current_cell_id).addClass("semi-invsbl");
    }
    y = y + 1;
    current_cell_id = "cell_" + x + "_" + y;
    $("#" + current_cell_id).removeClass("invsbl");
    $("#" + current_cell_id).removeClass("semi-invsbl");
  }   
}