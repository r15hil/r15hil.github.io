[__Back to home__](../index.md)

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

<script>
  function countYearOccurrences() {
    const currentYear = new Date().getFullYear();

    const bodyClone = document.body.cloneNode(true);
    const countListInClone = bodyClone.querySelector("#yearList");
    if (countListInClone) {
      countListInClone.remove();
    }
    const pageText = bodyClone.innerText;

    const yearRegex = /\b(20[1-9]\d|21\d{2})\b/g;
    const matches = pageText.match(yearRegex) || [];

    const yearOccurrences = matches.reduce((acc, year) => {
      acc[year] = (acc[year] || 0) + 1;
      return acc;
    }, {});

    const labels = [];
    const data = [];
    for (let year = 2016; year <= currentYear; year++) {
      labels.push(year.toString());
      data.push(yearOccurrences[year.toString()] || 0);
    }

    if (window.yearChart && typeof window.yearChart.destroy === "function") {
      window.yearChart.destroy();
    }

    const ctx = document.getElementById("yearChart").getContext("2d");
    window.yearChart = new Chart(ctx, {
      type: "bar",
      data: {
        labels: labels,
        datasets: [{
          label: "Books Read per Year",
          data: data,
          backgroundColor: 'rgba(75, 192, 192, 0.2)',
          borderColor: 'rgba(75, 192, 192, 1)',
          borderWidth: 1
        }]
      },
      options: {
        scales: {
          y: {
            beginAtZero: true,
            ticks: { stepSize: 1 }
          }
        }
      }
    });
  }

  document.addEventListener("DOMContentLoaded", countYearOccurrences);
</script>

<style>
  .book-line { position: relative; }
  .book-search {
    margin-left: 0.5rem;
    font-size: 0.95em;
    text-decoration: underline;
    text-underline-offset: 2px;
  }
</style>

<script>
  (function () {
    function attachGoogleSearchLinks() {
      // Find the "Books" section by id or text (covers your built HTML)
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

        // Visible link
        const link = document.createElement("a");
        link.className = "book-search";
        link.href = href;
        link.target = "_blank";
        link.rel = "noopener";
        link.textContent = "🔎 Search on Google";
        p.appendChild(link);

        // Click anywhere on the line to open search (except when clicking the link itself)
        p.addEventListener("click", (e) => {
          if (e.target.closest("a.book-search")) return; // let the link behave normally
          window.open(href, "_blank", "noopener");
        });

        // Keyboard accessible
        p.addEventListener("keydown", (e) => {
          if (e.key === "Enter" || e.key === " ") {
            e.preventDefault();
            window.open(href, "_blank", "noopener");
          }
        });
      });
    }

    if (document.readyState === "loading") {
      document.addEventListener("DOMContentLoaded", attachGoogleSearchLinks);
    } else {
      attachGoogleSearchLinks();
    }
  })();
</script>

<canvas id="yearChart" width="600" height="400"></canvas>

# Books I've read

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

