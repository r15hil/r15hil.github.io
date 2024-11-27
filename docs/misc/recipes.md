# 🍴 Recipe URL Fetcher 🍴

Click the button below to fetch random recipe URLs from the Gousto API via a public proxy!

<div style="margin-top: 20px;">
  <button onclick="fetchRecipeUrls()">Fetch Recipes</button>
</div>

## 📝 Recipe URLs:
<ul id="recipeUrls" style="margin-top: 20px; font-size: 18px;"></ul>

<script>
  async function fetchRecipeUrls() {
    const recipeUrlsList = document.getElementById("recipeUrls");
    recipeUrlsList.innerHTML = "<li>Loading recipes...</li>";

    try {
      // Generate a random offset for the API call
      const randomOffset = 16 * Math.floor(Math.random() * 330);

      // API endpoint with proxy
      const apiUrl = `https://cors-anywhere.herokuapp.com/https://production-api.gousto.co.uk/cmsreadbroker/v1/recipes?limit=16&offset=${randomOffset}`;

      // Fetch data from the API via the proxy
      const response = await fetch(apiUrl);

      // Check if the response is OK
      if (!response.ok) {
        throw new Error(`API request failed with status ${response.status}`);
      }

      // Parse the JSON response
      const data = await response.json();

      // Extract the recipe URLs
      const entries = data.data.entries;
      const urls = entries.map(entry => entry.url);

      // Display the URLs on the page
      recipeUrlsList.innerHTML = urls
        .map(url => `<li><a href="${url}" target="_blank">${url}</a></li>`)
        .join("");

      if (urls.length === 0) {
        recipeUrlsList.innerHTML = "<li>No recipes found.</li>";
      }
    } catch (error) {
      // Handle errors and display a message
      recipeUrlsList.innerHTML = `<li style="color: red;">Error fetching recipes: ${error.message}</li>`;
    }
  }
</script>
