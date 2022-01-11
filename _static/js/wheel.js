var neigh_size = js_vars.neigh_size;

let circleRadius = 45;
let wheelRadius = 180;
let DX = 500;
let DY = 500;
let border = 10;

let secondsAnimated = js_vars.secAnimation;
let nC = js_vars.nC;

var draw = SVG().addTo('#wheel-canvas').size(DX, DY);
// var rect = draw.rect(100, 100).attr({ fill: '#f06' })

function draw_lollipop(playerId, playerName, label) {

    var symbol = draw.symbol();
    var group = symbol.group().attr({id: playerId});
    var circle = symbol.circle(circleRadius).move(DX/2-circleRadius/2, 50);
    var line = symbol.line(DX/2, DY/2, DX/2, DY/2-wheelRadius).stroke({ width: 2, color: '#ccc'});
    var playerName = symbol.text(playerName).attr({x:DX/2, y:40}).font({anchor: "middle"});
    var playerStrategy = symbol.text(label).attr({x:DX/2, y:82}).font({anchor: "middle", size: 30}).attr({fill: "#f7f7f7"});
    group.add(line)
    group.add(circle)
    group.add(playerName)
    group.add(playerStrategy)
    return group
}

function shuffle(array) {
    let currentIndex = array.length,  randomIndex;

    // While there remain elements to shuffle...
    while (currentIndex != 0) {

      // Pick a remaining element...
      randomIndex = Math.floor(Math.random() * currentIndex);
      currentIndex--;

      // And swap it with the current element.
      [array[currentIndex], array[randomIndex]] = [
        array[randomIndex], array[currentIndex]];
    }

    return array;
  }

var playing_c = Array(nC).fill('C')
var playing_d = Array(nC).fill('D')
var strategies = playing_c.concat(playing_d)

if (js_vars.shuffle == true) {
    strategies = shuffle(strategies)
}

for (var i = 1; i <= neigh_size; i++) {
    var unit_shift = 360/neigh_size;
    var playerRotation = unit_shift*(i-1)+unit_shift/2;
    var strategy = strategies[i-1]
    if (strategy == 'C') {
        var strategyColor = '#f1a340'
        var lolli = draw_lollipop(i, '', 'C')
    } else {
        var strategyColor = '#998ec3'
        var lolli = draw_lollipop(i, '', 'D')
    }

    var lol = draw.use(lolli).attr({fill:'#f7f7f7'})
    lol.rotate(playerRotation, DX/2, DY/2)
    lol.delay(Math.random()*secondsAnimated*1000).animate().attr({fill: strategyColor})
}

var me = draw.circle(100).move(DX/2-50, DY/2-50).attr({fill: '#f7f7f7'});
var playerStrategy = draw.text("You").attr({x:DX/2, y:DY/2}).font({anchor: "middle", size: 30}).attr({fill: "black"});
