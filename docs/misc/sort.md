# 🗂 Alphabetical Order Sorter

Enter a list of items (either comma-separated or each item on a new line), and click "Sort" to see them in alphabetical order. Use the toggle to sort in reverse order.

<form>
  <label for="inputItems">Enter items:</label><br>
  <textarea id="inputItems" rows="10" cols="50" placeholder="e.g., Apple, Orange, Banana or separated by new lines."></textarea><br><br>

  <label for="sortToggle" style="display: inline-block; font-size: 16px;">Sort in reverse order:</label>
  <label class="toggle-switch">
    <input type="checkbox" id="sortToggle">
    <span class="slider"></span>
  </label><br><br>

  <button type="button" onclick="sortAlphabetically()">Sort</button>
</form>

## 📝 Sorted Items:
<textarea id="outputItems" rows="10" cols="50" readonly placeholder="Your sorted items will appear here."></textarea>

<style>
  .toggle-switch {
    position: relative;
    display: inline-block;
    width: 50px;
    height: 25px;
  }

  .toggle-switch input {
    display: none;
  }

  .slider {
    position: absolute;
    cursor: pointer;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-color: #ccc;
    border-radius: 25px;
    transition: 0.4s;
  }

  .slider:before {
    position: absolute;
    content: "";
    height: 17px;
    width: 17px;
    left: 4px;
    bottom: 4px;
    background-color: white;
    border-radius: 50%;
    transition: 0.4s;
  }

  input:checked + .slider {
    background-color: #4caf50;
  }

  input:checked + .slider:before {
    transform: translateX(25px);
  }
</style>

<script>
  function sortAlphabetically() {
    const input = document.getElementById('inputItems').value.trim();
    const reverseOrder = document.getElementById('sortToggle').checked;

    if (!input) {
      alert("Please enter some items to sort.");
      return;
    }

    // Detect input format: comma-separated or newline-separated
    const isCommaSeparated = input.includes(',');

    // Split items based on the detected format
    const items = isCommaSeparated
      ? input.split(',').map(item => item.trim())
      : input.split('\n').map(item => item.trim());

    // Sort items alphabetically (normal or reverse)
    const sortedItems = items
      .filter(item => item) // Remove empty items
      .sort((a, b) => (reverseOrder ? b.localeCompare(a) : a.localeCompare(b)));

    // Output sorted items in the same format
    const output = isCommaSeparated ? sortedItems.join(', ') : sortedItems.join('\n');
    document.getElementById('outputItems').value = output;
  }
</script>
