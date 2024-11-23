[__Back to home__](../index.md)

# 🗂 Alphabetical Order Sorter

Enter a list of items (either comma-separated or each item on a new line), and click "Sort" to see them in alphabetical order.

<form>
  <label for="inputItems">Enter items:</label><br>
  <textarea id="inputItems" rows="10" cols="50" placeholder="e.g., Apple, Orange, Banana or on newlines"></textarea><br><br>
  
  <button type="button" onclick="sortAlphabetically()">Sort</button>
</form>

## 📝 Sorted Items:
<textarea id="outputItems" rows="10" cols="50" readonly placeholder="Your sorted items will appear here."></textarea>

<script>
  function sortAlphabetically() {
    const input = document.getElementById('inputItems').value.trim();
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

    // Sort items alphabetically
    const sortedItems = items.filter(item => item).sort((a, b) => a.localeCompare(b));

    // Output sorted items in the same format
    const output = isCommaSeparated ? sortedItems.join(', ') : sortedItems.join('\n');
    document.getElementById('outputItems').value = output;
  }
</script>
