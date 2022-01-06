
var n_C = {{ n_C }};
var n_D = {{ n_D }};
var n_C_1 = {{ n_C }} - 1;

var neigh_size = n_C + n_D;
var list = [9, 3, 15, 17, 5, 10, 7, 11, 12, 1, 14, 13, 16, 8, 6, 18, 2, 0, 4, 19];

for (var i = 2; i <= neigh_size; i++) {

    if (i <= n_C){ //Cooperators
    console.log('#player-' + String(i) +' circle')
    document.querySelector('#player-' + String(i) +' circle').style.fill = "#97cef0";
    document.querySelector('#player-' + String(i) +' .e').textContent = "C";
    }
    else { //Non-cooperators
    document.querySelector('#player-' + String(i) +' circle').style.fill = "#c64d9c";
    document.querySelector('#player-' + String(i) +' .e').textContent = "N";
    }
}
