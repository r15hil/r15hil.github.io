# 🎉 URL Query Parameter Reader 🎉

[__Back to home__](../index.md)

This page reads values from the URL query parameters and displays them in a fun way. Just add your query parameters to the URL (e.g., `?name=Rishil&favoriteColor=blue`).

<div id="funContent">
  <!-- The content will appear here -->
</div>

<script>
  function getQueryParams() {
    const queryString = window.location.search;
    const urlParams = new URLSearchParams(queryString);
    const params = {};
    urlParams.forEach((value, key) => {
      params[key] = value;
    });
    return params;
  }

  function displayFunContent(params) {
    const container = document.getElementById("funContent");
    container.innerHTML = ""; // Clear existing content

    if (Object.keys(params).length === 0) {
      container.innerHTML = "<p style='font-size: 18px;'>No query parameters found! Try adding some to the URL, like <code>?name=John&favoriteColor=blue</code>.</p>";
      return;
    }

    for (const [key, value] of Object.entries(params)) {
      const element = document.createElement("div");
      element.style.margin = "10px 0";
      element.style.padding = "10px";
      element.style.background = "#f9f9f9";
      element.style.border = "1px solid #ddd";
      element.style.borderRadius = "8px";
      element.style.fontSize = "20px";
      element.style.animation = "fadeIn 1s";
      element.innerHTML = `<strong>${key}:</strong> <span style="color: #4caf50;">${value}</span>`;
      container.appendChild(element);
    }
  }

  // CSS for animation
  const style = document.createElement("style");
  style.innerHTML = `
    @keyframes fadeIn {
      from {
        opacity: 0;
        transform: translateY(-10px);
      }
      to {
        opacity: 1;
        transform: translateY(0);
      }
    }
  `;
  document.head.appendChild(style);

  // Read query params and display them
  const params = getQueryParams();
  displayFunContent(params);
</script>
