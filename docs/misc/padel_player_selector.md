[__Back to home__](../index.md)

# 🎾 Random Padel Player Selector 🎾

Enter the names of four players below and click "Select Player" to find out who will serve first!

<form>
  <label for="player1">Player 1:</label><br>
  <input type="text" id="player1" placeholder="Enter Player 1's name"><br><br>

  <label for="player2">Player 2:</label><br>
  <input type="text" id="player2" placeholder="Enter Player 2's name"><br><br>

  <label for="player3">Player 3:</label><br>
  <input type="text" id="player3" placeholder="Enter Player 3's name"><br><br>

  <label for="player4">Player 4:</label><br>
  <input type="text" id="player4" placeholder="Enter Player 4's name"><br><br>

  <button type="button" onclick="selectRandomPlayer()">Select Player</button>
</form>

## 🎉 Selected Player:
<p id="result" style="font-weight: bold; font-size: 1.5em; color: green;">No player selected yet.</p>

<script>
  function selectRandomPlayer() {
    const players = [
      document.getElementById('player1').value.trim(),
      document.getElementById('player2').value.trim(),
      document.getElementById('player3').value.trim(),
      document.getElementById('player4').value.trim()
    ];

    const validPlayers = players.filter(player => player !== '');
    if (validPlayers.length < 4) {
      alert("Please enter names for all 4 players.");
      return;
    }

    const randomIndex = Math.floor(Math.random() * validPlayers.length);
    const selectedPlayer = validPlayers[randomIndex];

    document.getElementById('result').innerText = `🏆 ${selectedPlayer} will serve first! 🏆`;
  }
</script>
