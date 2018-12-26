var board = `<table class='board shrink'>
  <tr>
    <td><div class='emptySpace'  id='{}0'></div></td>
    <td><div class='emptySpace'  id='{}1'>></div></td>
    <td><div class='emptySpace'  id='{}2'>-</div></td>
    <td><div class='emptySpace'  id='{}3'>-</div></td>
    <td><div class='emptySpace'  id='{}4'>o</div></td>
    <td><div class='emptySpace'  id='{}5'></div></td>
    <td><div class='emptySpace'  id='{}6'></div></td>
    <td><div class='emptySpace'  id='{}7'></div></td>
    <td><div class='emptySpace'  id='{}8'></div></td>
    <td><div class='emptySpace'  id='{}9'>></div></td>
    <td><div class='emptySpace'  id='{}10'>-</div></td>
    <td><div class='emptySpace'  id='{}11'>-</div></td>
    <td><div class='emptySpace'  id='{}12'>-</div></td>
    <td><div class='emptySpace'  id='{}13'>o</div></td>
    <td><div class='emptySpace'  id='{}14'></div></td>
    <td><div class='emptySpace'  id='{}15'></div></td>
  </tr>
  <tr>
    <td><div class='emptySpace'  id='{}59'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='yellowSafeSpace'  id='{}ys1'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='yellow'  id='{}ys'>0</div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='emptySpace'  id='{}16'>v</div></td>
  </tr>
  <tr>
    <td><div class='emptySpace'  id='{}58'>o</div></td>
    <td><div class='empty'></div></td>
    <td><div class='yellowSafeSpace'  id='{}ys2'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='green'  id='{}gh'>0</div></td>
    <td><div class='greenSafeSpace'  id='{}gs5'></div></td>
    <td><div class='greenSafeSpace'  id='{}gs4'></div></td>
    <td><div class='greenSafeSpace'  id='{}gs3'></div></td>
    <td><div class='greenSafeSpace'  id='{}gs2'></div></td>
    <td><div class='greenSafeSpace'  id='{}gs1'></div></td>
    <td><div class='emptySpace'  id='{}17'>|</div></td>
  </tr>
  <tr>
    <td><div class='emptySpace'  id='{}57'>|</div></td>
    <td><div class='empty'></div></td>
    <td><div class='yellowSafeSpace'  id='{}ys3'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='emptySpace'  id='{}18'>|</div></td>
  </tr>
  <tr>
    <td><div class='emptySpace'  id='{}56'>|</div></td>
    <td><div class='empty'></div></td>
    <td><div class='yellowSafeSpace'  id='{}ys4'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='green'  id='{}gs'>0</div></td>
    <td><div class='emptySpace'  id='{}19'>o</div></td>
  </tr>
  <tr>
    <td><div class='emptySpace'  id='{}55'>|</div></td>
    <td><div class='empty'></div></td>
    <td><div class='yellowSafeSpace'  id='{}ys5'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='emptySpace'  id='{}20'></div></td>
  </tr>
  <tr>
    <td><div class='emptySpace'  id='{}54'>^</div></td>
    <td><div class='empty'></div></td>
    <td><div class='yellow'  id='{}yh'>0</div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='emptySpace'  id='{}21'></div></td>
  </tr>
  <tr>
    <td><div class='emptySpace'  id='{}53'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'>S</div></td>
    <td><div class='empty'>O</div></td>
    <td><div class='empty'>R</div></td>
    <td><div class='empty'>R</div></td>
    <td><div class='empty'>Y</div></td>
    <td><div class='empty'>!</div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='emptySpace'  id='{}22'></div></td>
  </tr>
  <tr>
    <td><div class='emptySpace'  id='{}52'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='emptySpace'  id='{}23'></div></td>
  </tr>
  <tr>
    <td><div class='emptySpace'  id='{}51'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='blue'  id='{}bh'>0</div></td>
    <td><div class='empty'></div></td>
    <td><div class='emptySpace'  id='{}24'>v</div></td>
  </tr>
  <tr>
    <td><div class='emptySpace'  id='{}50'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='blueSafeSpace'  id='{}bs5'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='emptySpace'  id='{}25'>|</div></td>
  </tr>
  <tr>
    <td><div class='emptySpace'  id='{}49'>o</div></td>
    <td><div class='red'  id='{}rs'>0</div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='blueSafeSpace'  id='{}bs4'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='emptySpace'  id='{}26'>|</div></td>
  </tr>
  <tr>
    <td><div class='emptySpace'  id='{}48'>|</div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='blueSafeSpace'  id='{}bs3'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='emptySpace'  id='{}27'>|</div></td>
  </tr>
  <tr>
    <td><div class='emptySpace'  id='{}47'>|</div></td>
    <td><div class='redSafeSpace'  id='{}rs1'></div></td>
    <td><div class='redSafeSpace'  id='{}rs2'></div></td>
    <td><div class='redSafeSpace'  id='{}rs3'></div></td>
    <td><div class='redSafeSpace'  id='{}rs4'></div></td>
    <td><div class='redSafeSpace'  id='{}rs5'></div></td>
    <td><div class='red'  id='{}rh'>0</div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='blueSafeSpace'  id='{}bs2'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='emptySpace'  id='{}28'>o</div></td>
  </tr>
  <tr>
    <td><div class='emptySpace'  id='{}46'>^</div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='blue'  id='{}bs'>0</div></td>
    <td><div class='empty'></div></td>
    <td><div class='blueSafeSpace'  id='{}bs1'></div></td>
    <td><div class='empty'></div></td>
    <td><div class='emptySpace'  id='{}29'></div></td>
  </tr>
  <tr>
    <td><div class='emptySpace'  id='{}45'></div></td>
    <td><div class='emptySpace'  id='{}44'></div></td>
    <td><div class='emptySpace'  id='{}43'>o</div></td>
    <td><div class='emptySpace'  id='{}42'>-</div></td>
    <td><div class='emptySpace'  id='{}41'>-</div></td>
    <td><div class='emptySpace'  id='{}40'>-</div></td>
    <td><div class='emptySpace'  id='{}39'><</div></td>
    <td><div class='emptySpace'  id='{}38'></div></td>
    <td><div class='emptySpace'  id='{}37'></div></td>
    <td><div class='emptySpace'  id='{}36'></div></td>
    <td><div class='emptySpace'  id='{}35'></div></td>
    <td><div class='emptySpace'  id='{}34'>o</div></td>
    <td><div class='emptySpace'  id='{}33'>-</div></td>
    <td><div class='emptySpace'  id='{}32'>-</div></td>
    <td><div class='emptySpace'  id='{}31'><</div></td>
    <td><div class='emptySpace'  id='{}30'></div></td>
  </tr>
</table>`

var PLAYERS = ["y","g","b","r"];
var COLOR_TO_PLAYER = {yellow: "y",
                       green:  "g",
                       blue:   "b",
                       red:    "r"};
var PLAYER_TO_COLOR = {y: "yellow",
                       g: "green",
                       b: "blue",
                       r: "red"};
var INVALID_SPACES = {y: [16,31,46,24,39,54],
                      g: [1,9,31,46,39,54],
                      b: [1,9,16,46,24,54],
                      r: [1,9,16,31,24,39]};
var PLACE_STATES = ["emptySpace", "yellowSpace", "greenSpace", "blueSpace", "redSpace"]
var SLIDE_SPOTS = {1: ">", 2: "-", 3: "-", 4: "o",
                   9: ">", 10: "-", 11: "-", 12: "-", 13: "o",
                   16: "v", 17: "|", 18: "|", 19: "o",
                   24: "v", 25: "|", 26: "|", 27: "|", 28: "o",
                   31: "<", 32: "-", 33: "-", 34: "o",
                   39: "<", 40: "-", 41: "-", 42: "-", 43: "o",
                   46: "^", 47: "|", 48: "|", 49: "o",
                   54: "^", 55: "|", 56: "|", 57: "|", 58: "o"}

var globalGameState = {y:[],
                       g:[],
                       b:[],
                       r:[]};

function removePawn(player, spot) {
  globalGameState[player] = globalGameState[player].filter(a => a !== spot)
}

function addPawn(player, spot) {
  globalGameState[player].push(spot);
}

function selectPlace(clickedId) {
  if (clickedId.startsWith("y") ||
      clickedId.startsWith("g") ||
      clickedId.startsWith("r") ||
      clickedId.startsWith("b")) {
    if (clickedId.length > 2) {
      selectSafeZone(clickedId);
    } else {
      selectStartOrHome(clickedId);
    }
  } else {
    selectEdge(clickedId);
  }
  updateUI();
}

function updateUI() {
  // For debugging purposes
  document.getElementById("metadata").innerHTML = JSON.stringify(globalGameState);

  var errors = "";
  for (var i = 0; i < PLAYERS.length; i++) {
    var player = PLAYERS[i];
    var color = PLAYER_TO_COLOR[player];
    var numPawnsInPlay = globalGameState[player].length;
    if (numPawnsInPlay > 4) {
      errors += "Player " + color + " has more than 4 pawns in play ("+numPawnsInPlay+")<br />";
    } else if (numPawnsInPlay < 4) {
       errors += "Player " + color + " has less than 4 pawns in play ("+numPawnsInPlay+")<br />";
    }

    for (var n = 0; n < globalGameState[player].length; n++) {
      var playersInvalidSpaces = INVALID_SPACES[player];
      for (var j = 0; j < playersInvalidSpaces.length; j++) {
        if (globalGameState[player][n].startsWith("board") && playersInvalidSpaces[j] == parseInt(globalGameState[player][n].split(":")[1])) { 
          errors += "Player " + color + " has a pawn on the start of an opponents slide.<br />";
        }
      }
    }
  }
  document.getElementById("errors").innerHTML = errors;

  if (errors == "") {
    document.getElementById("go").innerHTML = "<button type=\"button\" onclick=\"analyzeBoard()\">Analyze</button>";
  } else {
    document.getElementById("go").innerHTML = "<button type=\"button\" disabled>Analyze</button>";
  }
}

function selectSafeZone(clickedId) {
  var player = clickedId.charAt(0);
  var elem = document.getElementById(clickedId);

  if (elem.innerHTML != "") {
    elem.innerHTML = "";
    removePawn(player, "safe:" + clickedId.slice(-1));
  } else {
    elem.innerHTML = "<div class=\""+elem.className.replace("SafeSpace","")+"Piece\"></div>";
    addPawn(player, "safe:" + clickedId.slice(-1));
  }
}

function selectEdge(clickedId) {
  var elem = document.getElementById(clickedId);
  var currentState = elem.className;
  var currentColor = currentState.replace("Space","");
  var currentNdx = PLACE_STATES.indexOf(currentState);
  var nextNdx = (currentNdx + 1) % 5;
  var nextState = PLACE_STATES[nextNdx];
  elem.className = nextState;
  var nextColor = nextState.replace("Space","");
  var player = COLOR_TO_PLAYER[nextColor];
  var prevPlayer = COLOR_TO_PLAYER[currentColor];

  if (nextState != "emptySpace") {
    elem.innerHTML = "<div class=\""+nextColor+"Piece\"></div>";
    addPawn(player, "board:"+clickedId);
  } else {
    var emptyValue = SLIDE_SPOTS[clickedId];
    if (typeof emptyValue === "undefined") {
      emptyValue = "";
    }
    elem.innerHTML = emptyValue;
  }

  if (currentState != "emptySpace") {
    removePawn(prevPlayer, "board:"+clickedId);
  }
}

function selectStartOrHome(clickedId) {
  var elem = document.getElementById(clickedId);
  var currentValue = parseInt(elem.innerHTML);
  var newValue = (currentValue + 1) % 5;
  elem.innerHTML = newValue;
  var player = clickedId.charAt(0);

  if (clickedId.endsWith("h")) {
    removePawn(player, 'home');
    for (var i = 0; i < newValue; i++) {
      addPawn(player, 'home')
    }
  } else {
    removePawn(player, 'start');
    for (var i = 0; i < newValue; i++) {
      addPawn(player, 'start')
    }
  }
}

function analyzeBoard() {
  var currentCardSelect = document.getElementById("currentCardSelect");
  var currentCard = currentCardSelect.options[currentCardSelect.selectedIndex].value.toLowerCase();
  var currentPlayerSelect = document.getElementById("currentPlayerSelect");
  var currentPlayer = currentPlayerSelect.options[currentPlayerSelect.selectedIndex].value;
  var xhr = new XMLHttpRequest();
  xhr.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            console.log(this);
            updateAnalysisResults(this)
        }
    };
  xhr.open("POST", "/", true);
  xhr.setRequestHeader('Content-Type', 'application/json');
  xhr.send(JSON.stringify({
      pawns: globalGameState,
      card: currentCard,
      player: currentPlayer
  }));
}

function updateAnalysisResults(serverResults) {
  var jsonResponse = JSON.parse(serverResults.response);
  var possibleMoves = jsonResponse["possibleGameStates"];
  var inputGameState = jsonResponse["inputState"];
  var numPossibleMoves = possibleMoves.length;

  if (numPossibleMoves == 0) {
    document.getElementById("results").innerHTML = "There are zero valid moves";
  } else if (numPossibleMoves == 1) {
    document.getElementById("results").innerHTML = "There is only 1 valid move";
  } else {
    document.getElementById("results").innerHTML = "There are "+numPossibleMoves+" possible moves";
  }

  var possibleMovesHtml = "";

  if (numPossibleMoves > 0) {
    for (var i = 0; i < numPossibleMoves; i++) {
      possibleMovesHtml += "<hr />";
      possibleMovesHtml += "<div class=\"resultContainer\">";
      possibleMovesHtml += "<div class=\"resultLabel\"><h3>Option "+(i+1)+"</h3></div>"
      possibleMovesHtml += "<div class=\"resultBoard\">"+createEmptyBoard(i)+"</div>";
      possibleMovesHtml += "<div class=\"resultAnalysis\">";
      possibleMovesHtml += createAnalysisTable(possibleMoves[i], inputGameState);
      possibleMovesHtml += "</div></div>";
    }
  }
  document.getElementById("possibleStates").innerHTML = possibleMovesHtml;

  for (var i = 0; i < numPossibleMoves; i++) {
    var possibleMove = possibleMoves[i]["gameState"];
    for (var j = 0; j < PLAYERS.length; j++) {
      var player = PLAYERS[j].toUpperCase();
      var playerMoves = possibleMove[player];
      for (var k = 0; k < playerMoves.length; k++) {
        setPawnOnBoard(i, playerMoves[k], player);
      }
    }
  }
}

function createAnalysisTable(possibleMove, inputState) {
  var startingDistances = inputState["distances"];
  var distances = possibleMove["distances"];
  var startingRFScores = inputState["rfScores"];
  var rfScores = possibleMove["rfScores"];
  var result = "<div class='divTable' style='width: 30px;border: 1px solid #000;' >";
  result += "<div class='divTableBody'>";
  result += "<div class='divTableRow'>";
  result += "<div class='divTableCell'>&nbsp;</div>";
  result += "<div class='divTableCell'>Yellow</div>";
  result += "<div class='divTableCell'>Green</div>";
  result += "<div class='divTableCell'>Blue</div>";
  result += "<div class='divTableCell'>Red</div>";
  result += "</div>";
  result += "<div class='divTableRow'>";
  result += "<div class='divTableCell'>rfScore</div>";
  result += "<div class='divTableCell'>"+distanceEntry(rfScores, startingRFScores, "Y")+"</div>";
  result += "<div class='divTableCell'>"+distanceEntry(rfScores, startingRFScores, "G")+"</div>";
  result += "<div class='divTableCell'>"+distanceEntry(rfScores, startingRFScores, "B")+"</div>";
  result += "<div class='divTableCell'>"+distanceEntry(rfScores, startingRFScores, "R")+"</div>";
  result += "</div>";
  result += "<div class='divTableRow'>";
  result += "<div class='divTableCell'>distances</div>";
  result += "<div class='divTableCell'>"+distanceEntry(distances, startingDistances, "Y")+"</div>";
  result += "<div class='divTableCell'>"+distanceEntry(distances, startingDistances, "G")+"</div>";
  result += "<div class='divTableCell'>"+distanceEntry(distances, startingDistances, "B")+"</div>";
  result += "<div class='divTableCell'>"+distanceEntry(distances, startingDistances, "R")+"</div>";
  result += "</div>";
  result += "</div>";
  result += "</div>";
  return result;
}

function scalingRound(num) {
  return Math.round(num * 100) / 100
}

function distanceEntry(newDistances, startingDistances, player) {
  var delta = scalingRound(newDistances[player] - startingDistances[player]);
  var deltaString = "";
  if (delta > 0) {
    deltaString = "(+"+delta+")";
  } else if (delta < 0) {
    deltaString = "("+delta+")";
  }
  return scalingRound(newDistances[player]) + deltaString;
}

function setPawnOnBoard(boardId, pawnPosition, player) {
  var playerLower = player.toLowerCase();
  var color = PLAYER_TO_COLOR[playerLower];
  if (pawnPosition.startsWith("board")) {
    elem = document.getElementById(boardId + "_" + pawnPosition.split(":")[1]);
    elem.className = color + "Space";
    elem.innerHTML = "<div class=\""+color+"Piece\"></div>";
  } else if (pawnPosition.startsWith("safe")) {
    elem = document.getElementById(boardId + "_" + playerLower + "s" + pawnPosition.split(":")[1]);
    elem.innerHTML = "<div class=\""+elem.className.replace("SafeSpace","")+"Piece\"></div>";
  } else if (pawnPosition == "home") {
    elem = document.getElementById(boardId + "_" + playerLower + "h");
    currentValue = parseInt(elem.innerHTML);
    newValue = (currentValue + 1);
    elem.innerHTML = newValue;
  } else {
    elem = document.getElementById(boardId + "_" + playerLower + "s");
    currentValue = parseInt(elem.innerHTML);
    newValue = (currentValue + 1);
    elem.innerHTML = newValue;
  }
}

function createEmptyBoard(id) {
  return board.split("{}").join(id+"_");
}