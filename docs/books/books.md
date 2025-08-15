[__Back to home__](../index.md)

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

<!-- BAR GRAPH START -->
<script>
  function buildStackedReadsChart() {
    const currentYear = new Date().getFullYear();

    const booksHeader =
      document.getElementById("books") ||
      Array.from(document.querySelectorAll("h2"))
        .find(h => h.textContent.trim().toLowerCase() === "books");
    if (!booksHeader) return;

    const bookLines = [];
    let el = booksHeader.nextElementSibling;
    while (el && el.tagName !== "H2") {
      if (el.tagName === "P") bookLines.push(el);
      el = el.nextElementSibling;
    }

    const years = [];
    const byYear = {};
    for (let y = 2016; y <= currentYear; y++) {
      years.push(String(y));
      byYear[y] = { enjoyed: 0, ok: 0, meh: 0 };
    }

    const yearRegex = /\b(20\d{2}|21\d{2})\b/g;

    bookLines.forEach(p => {
      const t = p.textContent || "";
      if (!t.trim().startsWith("✅")) return;

      const matches = t.match(yearRegex);
      if (!matches) return;
      const year = Number(matches[matches.length - 1]);
      if (!byYear[year]) return;

      const enjoyed = t.includes("👍");
      const ok = t.includes("🆗");
      const meh = t.includes("😕");

      if (enjoyed) byYear[year].enjoyed++;
      else if (ok) byYear[year].ok++;
      else if (meh) byYear[year].meh++;
      else byYear[year].ok++;
    });

    const enjoyedData = years.map(y => byYear[Number(y)].enjoyed);
    const okData = years.map(y => byYear[Number(y)].ok);
    const mehData = years.map(y => byYear[Number(y)].meh);

    if (window.yearChart && typeof window.yearChart.destroy === "function") {
      window.yearChart.destroy();
    }

    const ctx = document.getElementById("yearChart").getContext("2d");
    window.yearChart = new Chart(ctx, {
      type: "bar",
      data: {
        labels: years,
        datasets: [
          {
            label: "👍 Enjoyed",
            data: enjoyedData,
            backgroundColor: "rgba(0, 128, 0, 0.6)", // green
            borderColor: "rgba(0, 128, 0, 1)",
            borderWidth: 1,
            stack: "reads"
          },
          {
            label: "🆗 Ok",
            data: okData,
            backgroundColor: "rgba(255, 206, 86, 0.6)", // yellow
            borderColor: "rgba(255, 206, 86, 1)",
            borderWidth: 1,
            stack: "reads"
          },
          {
            label: "😕 Meh",
            data: mehData,
            backgroundColor: "rgba(255, 99, 132, 0.6)", // red
            borderColor: "rgba(255, 99, 132, 1)",
            borderWidth: 1,
            stack: "reads"
          }
        ]
      },
      options: {
        responsive: true,
        scales: {
          x: { stacked: true },
          y: {
            stacked: true,
            beginAtZero: true,
            ticks: { stepSize: 1 }
          }
        },
        plugins: {
          tooltip: {
            callbacks: {}
          },
          legend: { position: "top" },
          title: {
            display: true,
            text: "Books Read per Year (stacked by rating)"
          }
        }
      }
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", buildStackedReadsChart);
  } else {
    buildStackedReadsChart();
  }
</script>

<!-- BAR GRAPH END -->

<!-- SEARCH FEATURE START -->
<style>
  /* Toggle styles */
  #search-toggle-wrap { margin: 0.5rem 0 1rem; }
  .search-toggle {
    display: inline-flex; align-items: center; gap: 0.5rem; cursor: pointer; user-select: none;
  }
  .search-toggle input { display: none; }
  .search-toggle .slider {
    position: relative; width: 44px; height: 24px; border-radius: 999px;
    background: #bbb; transition: background 0.2s ease;
  }
  .search-toggle .slider::after {
    content: ""; position: absolute; top: 2px; left: 2px; width: 20px; height: 20px;
    border-radius: 50%; background: #fff; box-shadow: 0 1px 2px rgba(0,0,0,.2);
    transition: transform 0.2s ease;
  }
  .search-toggle input:checked + .slider { background: #4caf50; }
  .search-toggle input:checked + .slider::after { transform: translateX(20px); }
  .search-toggle .label-text { font-weight: 600; }

  /* Book search link; hidden unless Search mode is ON */
  .book-line { position: relative; }
  .book-search {
    margin-left: 0.5rem;
    font-size: 0.95em;
    text-decoration: underline;
    text-underline-offset: 2px;
    display: none; /* default hidden */
  }
  body.search-mode-on .book-search { display: inline; }
  /* Optional: show pointer when search mode is on to hint clickability */
  body.search-mode-on .book-line { cursor: pointer; }
</style>

<script>
  (function () {
    function attachGoogleSearchLinks() {
      const booksHeader =
        document.getElementById("books") ||
        Array.from(document.querySelectorAll("h2"))
          .find(h => h.textContent.trim().toLowerCase() === "books");
      if (!booksHeader) return;

      // Collect only the paragraphs that belong to the Books section
      const lines = [];
      let el = booksHeader.nextElementSibling;
      while (el && el.tagName !== "H2") {
        if (el.tagName === "P") lines.push(el);
        el = el.nextElementSibling;
      }

      const emojiRegex = /[📚✅👍🆗😕❤️]/g;

      function makeQueryFrom(text) {
        const noEmojis = text.replace(emojiRegex, "").trim();
        const beforeDash = noEmojis.split(" - ")[0].trim(); // prefer title/author part
        return encodeURIComponent(beforeDash || noEmojis);
      }

      lines.forEach(p => {
        if (p.dataset.gsearchApplied) return; // prevent duplicates
        p.dataset.gsearchApplied = "1";
        p.classList.add("book-line");
        p.tabIndex = 0;

        const raw = p.textContent || "";
        const q = makeQueryFrom(raw);
        const href = `https://www.google.com/search?q=${q}`;

        // Small visible link (only shown when search mode is ON via CSS)
        const link = document.createElement("a");
        link.className = "book-search";
        link.href = href;
        link.target = "_blank";
        link.rel = "noopener";
        link.textContent = "🔎";
        link.setAttribute("aria-label", "Search this book on Google");
        p.appendChild(link);

        // Click/keyboard: only active when Search mode is ON
        const openIfSearchMode = (e, viaKeyboard = false) => {
          const on = document.body.classList.contains("search-mode-on");
          if (!on) return;
          if (viaKeyboard) e.preventDefault();
          window.open(href, "_blank", "noopener");
        };

        p.addEventListener("click", (e) => {
          // Let the link behave normally
          if (e.target.closest("a.book-search")) return;
          openIfSearchMode(e, false);
        });

        p.addEventListener("keydown", (e) => {
          if (e.key === "Enter" || e.key === " ") openIfSearchMode(e, true);
        });
      });
    }

    function setupSearchModeToggle() {
      const toggle = document.getElementById("searchModeToggle");
      if (!toggle) return;

      // Initial state: OFF (no class)
      const apply = () => {
        if (toggle.checked) {
          document.body.classList.add("search-mode-on");
        } else {
          document.body.classList.remove("search-mode-on");
        }
      };

      toggle.addEventListener("change", apply);
      apply(); // set initial
    }

    function init() {
      attachGoogleSearchLinks();
      setupSearchModeToggle();
    }

    if (document.readyState === "loading") {
      document.addEventListener("DOMContentLoaded", init);
    } else {
      init();
    }
  })();
</script>
<!-- SEARCH FEATURE END -->

<canvas id="yearChart" width="600" height="400"></canvas>

# Books I've read

<!-- SEARCH MODE TOGGLE START -->
<div id="search-toggle-wrap">
  <label class="search-toggle">
    <input type="checkbox" id="searchModeToggle" />
    <span class="slider"></span>
    <span class="label-text">Search mode</span>
  </label>
</div>
<!-- SEARCH MODE TOGGLE END-->

## Key
📚 Reading | ✅ Read | 👍 Enjoyed | 🆗 Ok | 😕 Meh | ❤️ Recommend |

## Books

📚 The Man in the High Castle: Philip K. Dick

📚 Nexus: Yuval Noah Harari

📚 Mahabharata: Interpreted and Retold by Krishna Dharma

✅ Killers of the Flower Moon: David Grann - July 2025 🆗

✅ When: Daniel H. Pink - July 2025 🆗

✅ Butter: Asako Yuzuki - June 2025 👍❤️

✅ Heaven: Mieko Kawakami - April 2025 👍

✅ A History of Burning: Janika Oza - March 2025 👍

✅ Who Moved My Cheese?: Dr Spencer Johnson - March 2025 🆗

✅ Shantaram: Gregory David Roberts - February 2025 👍❤️

✅ Men Are from Mars, Women Are from Venus: John Gray - November 2024 🆗

✅ Ultra-Processed People: Chris van Tulleken - October 2024 👍

✅ Troy: Stephen Fry - October 2024 👍

✅ Heroes: Stephen Fry - September 2024 👍❤️

✅ Four Thousand Weeks: Oliver Burkeman - August 2024 👍

✅ God Emperor of Dune: Frank Herbert - August 2024 😕

✅ Children of Dune: Frank Herbert - July 2024 👍

✅ My Experiments with Truth: M.K. Gandhi - June 2024 👍

✅ Dune Messiah: Frank Herbert - June 2024 👍

✅ The Alchemist: Paulo Coelho - June 2024 ❤️

✅ Born to Run: Christopher McDougall - May 2024 ❤️

✅ Dune: Frank Herbert - May 2024 ❤️

✅ The Psychology of Money: Morgan Housel - April 2024 🆗

✅ A Wizard of Earthsea: Ursula K. Le Guin - March 2024 👍

✅ Fahrenheit 451: Ray Bradbury - February 2024 👍

✅ Surely You're Joking, Mr. Feynman!: Richard P. Feynman - December 2023 👍

✅ What Does It All Mean?: Thomas Nagel - December 2023 👍

✅ Pachinko: Min Jin Lee - November 2023 👍❤️

✅ Where the Crawdads Sing: Delia Owens - October 2023 👍

✅ Surviving to Drive: Guenther Steiner - August 2023 👍

✅ The Art of War: Sun Tzu - August 2023 🆗

✅ Essentialism: Greg McKeown - August 2023 🆗

✅ Kafka on the Shore: Haruki Murakami - August 2023 👍

✅ The Kite Runner: Khaled Hosseini - July 2023 👍

✅ Uncommon Wealth: Kojo Koram - June 2023 🆗

✅ Flowers for Algernon: Daniel Keyes - May 2023 👍❤️

✅ Can't Hurt Me: David Goggins - May 2023 👍

✅ This is Going to Hurt: Adam Kay - April 2023 👍

✅ The Defining Decade: Why Your Twenties Matter: Meg Jay - March 2023 🆗

✅ How to Win Friends and Influence People: Dale Carnegie - March 2023 👍

✅ Rebel Ideas: Matthew Syed - February 2023 🆗

✅ Mythos: Stephen Fry - January 2023 👍❤️

✅ 1984: George Orwell - December 2022 👍

✅ Animal Farm: George Orwell - November 2022 👍

✅ Bhagavad Gita: Introduced & Translated by Eknath Easwaran - November 2022 👍❤️

✅ Prisoners of Geography: Tim Marshall - October 2022 👍

✅ Sapiens: Yuval Noah Harari - October 2022 👍❤️

✅ Brave New World: Aldous Huxley - October 2022 👍

✅ Tools of Titans: Tim Ferriss - March 2021 🆗

✅ The Chimp Paradox: Steve Peters - February 2021 👍❤️

✅ Atomic habits: James Clear - January 2021 🆗

✅ When Breath Becomes Air: Paul Kalanithi - January 2018 👍

✅ Colorless: Haruki Murakami - October 2017 👍

✅ The Humans: Matt Haig - August 2017 🆗

✅ Lord of the Flies: William Golding - November 2016 👍 



## Reading List

🔜 I, Superorganism - Jon Turney

🔜 Guns, Germs, and Steel - Jared Diamond

🔜 Thinking, Fast and Slow - Daniel Kahneman

🔜 Why We Sleep - Matthew Walker

🔜 The ONE Thing - Gary Keller and Jay Papasan

🔜 The Beekeeper of Aleppo - Christy Lefteri

🔜 The 4-Hour Work Week - Tim Ferriss

🔜 Deep Work - Cal Newport

