[__Back to home__](../index.md)

# Secret Santa Generator

Enter a comma-separated list of names below, and click "Generate Secret Santa" to get the pairings.

<form>
  <label for="names">Enter names (comma-separated):</label><br>
  <textarea id="names" rows="5" cols="50" placeholder="e.g., Alice, Bob, Charlie, Dave"></textarea><br><br>
  <button type="button" onclick="generateSecretSanta()">Generate Secret Santa</button>
</form>

## Results
<ul id="results"></ul>

<script>
  function shuffleArray(array) {
    for (let i = array.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [array[i], array[j]] = [array[j], array[i]];
    }
  }

  function generateSecretSanta() {
    const namesInput = document.getElementById('names').value.trim();
    if (!namesInput) {
      alert("Please enter a list of names.");
      return;
    }

    const names = namesInput.split(',').map(name => name.trim()).filter(name => name);
    if (names.length < 2) {
      alert("Please enter at least two names.");
      return;
    }

    const originalNames = [...names];
    shuffleArray(names);

    // Ensure no one gets themselves
    for (let i = 0; i < names.length; i++) {
      if (names[i] === originalNames[i]) {
        shuffleArray(names);
        i = -1; // Restart the check
      }
    }

    const results = document.getElementById('results');
    results.innerHTML = '';

    for (let i = 0; i < originalNames.length; i++) {
      const li = document.createElement('li');
      li.textContent = `${originalNames[i]} -> ${names[i]}`;
      results.appendChild(li);
    }
  }
</script>
