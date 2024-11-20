[__Back to home__](../index.md)

# 🎅 Secret Santa Generator with Optional Exclusion Groups 🎅

Enter a comma-separated list of names below, optionally define exclusion groups, and click "Generate Secret Santa" to get the pairings.

<form>
  <label for="names">Enter names (comma-separated):</label><br>
  <textarea id="names" rows="4" cols="50" placeholder="e.g., Alice, Bob, Charlie, Dave"></textarea><br><br>

  <label for="groups">Optional: Enter exclusion groups (format: {Name1, Name2}, {Name3, Name4}):</label><br>
  <textarea id="groups" rows="4" cols="50" placeholder="e.g., {Alice, Bob}, {Charlie, Dave}"></textarea><br><br>

  <button type="button" onclick="generateSecretSanta()">Generate Secret Santa</button>
</form>

## 🎉 Secret Santa Pairings:
<ul id="results"></ul>

<script>
  function parseGroups(groupsInput, names) {
    const groups = [];
    if (!groupsInput.trim()) return groups; // Return empty groups if none are provided
    groupsInput.split('},').forEach(group => {
      const members = group.replace(/[{}]/g, '').split(',').map(name => name.trim()).filter(name => name);
      if (members.every(member => names.includes(member))) {
        groups.push(members);
      }
    });
    return groups;
  }

  function isValidAssignment(assignments, groups) {
    if (groups.length === 0) return true; // If no groups, all assignments are valid
    return groups.every(group => 
      group.every(giver => !group.includes(assignments[giver]))
    );
  }

  function shuffleArray(array) {
    for (let i = array.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [array[i], array[j]] = [array[j], array[i]];
    }
  }

  function generateSecretSanta() {
    const namesInput = document.getElementById('names').value.trim();
    const groupsInput = document.getElementById('groups').value.trim();

    if (!namesInput) {
      alert("Please enter a list of names.");
      return;
    }

    const names = namesInput.split(',').map(name => name.trim()).filter(name => name);
    if (names.length < 2) {
      alert("Please enter at least two names.");
      return;
    }

    const groups = parseGroups(groupsInput, names);

    let assignments = {};
    let shuffledNames = [...names];
    let attempts = 0;

    do {
      shuffleArray(shuffledNames);
      assignments = {};
      for (let i = 0; i < names.length; i++) {
        assignments[names[i]] = shuffledNames[i];
      }
      attempts++;
      if (attempts > 1000) {
        alert("Unable to generate a valid Secret Santa assignment with the given exclusions.");
        return;
      }
    } while (!isValidAssignment(assignments, groups) || 
             Object.entries(assignments).some(([giver, receiver]) => giver === receiver));

    const results = document.getElementById('results');
    results.innerHTML = '';

    Object.entries(assignments).forEach(([giver, receiver]) => {
      const li = document.createElement('li');
      li.textContent = `${giver} -> ${receiver}`;
      results.appendChild(li);
    });
  }
</script>
