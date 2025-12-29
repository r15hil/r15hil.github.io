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


<canvas id="yearChart" width="600" height="400"></canvas>

<!-- VIEW TOGGLE + BOOKSHELF (GROUPED BY YEAR, READING NOW, RECOMMENDED) + MODAL -->
<style>
  /* Toggle UI */
  #view-toggle { margin: .75rem 0 1rem; }
  .vtoggle { display: inline-flex; align-items: center; gap: .5rem; cursor: pointer; user-select: none; }
  .vtoggle input { display: none; }
  .vtoggle .slider {
    position: relative; width: 44px; height: 24px; border-radius: 999px;
    background: #bbb; transition: background .2s ease;
  }
  .vtoggle .slider::after {
    content: ""; position: absolute; top: 2px; left: 2px; width: 20px; height: 20px;
    border-radius: 50%; background: #fff; box-shadow: 0 1px 2px rgba(0,0,0,.2);
    transition: transform .2s ease;
  }
  .vtoggle input:checked + .slider { background: #4caf50; }
  .vtoggle input:checked + .slider::after { transform: translateX(20px); }
  .vtoggle .label-text { font-weight: 600; }

  /* Show/Hide logic */
  /* Add .book-raw to your original <p> lines via JS and toggle with body class */
  body.bookshelf-mode .book-raw { display: none; }
  body:not(.bookshelf-mode) .bookshelf-wrap { display: none; }

  /* Shelf visuals */
  .year-shelf { margin: 1.25rem 0 1.75rem; }
  .year-shelf h3 { margin: 0 0 .5rem; font-size: 1.1rem; letter-spacing: .3px; }
  .bookshelf {
    display: flex; flex-wrap: wrap; gap: 8px;
    padding: 12px;
    background: #8b5a2b;                 /* wood */
    border: 8px solid #5c3a1e;
    border-radius: 8px;
    box-shadow: inset 0 2px 6px rgba(0,0,0,0.45);
    position: relative;
  }
  .bookshelf::before {
    content: ""; position: absolute; inset: -10px -8px auto -8px; height: 10px;
    background: linear-gradient(#6d4423, #5c3a1e);
    border-top-left-radius: 8px; border-top-right-radius: 8px;
  }

  .book-spine {
    position: relative;
    writing-mode: vertical-rl;
    transform: rotate(180deg);
    font-size: 0.86rem; line-height: 1.1;
    font-weight: 700; color: #fff; text-align: center;
    padding: 6px 2px;
    border-radius: 4px;
    flex: 0 0 30px;              /* spine width */
    height: 200px;               /* spine height */
    overflow: hidden;
    box-shadow: 0 2px 4px rgba(0,0,0,.25);
    user-select: none;
    cursor: pointer;
    transition: transform .12s ease;
  }
  .book-spine:focus { outline: 2px dashed rgba(255,255,255,.7); outline-offset: 2px; }
  .book-spine:hover { transform: rotate(180deg) scale(1.03); }

  /* Color coding */
  .spine-enjoyed { background: #2e7d32; }  /* green */
  .spine-ok      { background: #f1c232; }  /* yellow */
  .spine-meh     { background: #e53935; }  /* red */
  .spine-reading { background: #607d8b; }  /* slate */
  .spine-neutral { background: #1976d2; }  /* blue */

  /* tiny top end-cap */
  .book-spine::after {
    content: "";
    position: absolute; top: 3px; left: 50%; transform: translateX(-50%);
    width: 60%; height: 3px; border-radius: 2px;
    background: rgba(255,255,255,0.35);
  }

  /* ⭐ Recommended (👍 + ❤️) */
  .spine-reco {
    background: linear-gradient(180deg, #f7d774, #e0a300);
    color: #2a2000;
    box-shadow: 0 0 0 2px #9a6b00 inset, 0 4px 8px rgba(0,0,0,.35);
  }
  .spine-reco .ribbon {
    position: absolute; top: 4px; right: 4px;
    transform: rotate(90deg); font-size: 12px;
    filter: drop-shadow(0 1px 1px rgba(0,0,0,.3));
    pointer-events: none;
  }

  /* Modal */
  .book-modal {
    position: fixed; inset: 0;
    display: none;
    align-items: center; justify-content: center;
    z-index: 10000;
  }
  .book-modal.show { display: flex; }
  .book-modal .backdrop {
    position: absolute; inset: 0; background: rgba(0,0,0,.5);
  }
  .book-modal .card {
    position: relative; z-index: 1;
    width: min(560px, 92vw);
    background: #fff; color: #111; border-radius: 12px;
    box-shadow: 0 10px 30px rgba(0,0,0,.4);
    padding: 16px 18px 12px;
    animation: pop .12s ease-out;
  }
  @keyframes pop { from { transform: translateY(6px) scale(.98); opacity: .8; } }
  .book-modal .title { font-size: 1.1rem; font-weight: 700; margin: 0 0 8px; }
  .book-modal .meta  { font-size: .95rem; margin: 0 0 10px; color: #333; }
  .book-modal .reactions { font-size: 1.1rem; margin-bottom: 6px; }
  .book-modal .raw { margin-top: 8px; font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; font-size: .88rem; color: #444; background: #f7f7f7; padding: 8px; border-radius: 8px; }
  .book-modal .close {
    position: absolute; top: 8px; right: 10px; border: 0; background: none;
    font-size: 22px; cursor: pointer; line-height: 1;
  }
  .book-modal .search-btn {
    display: inline-block;
    margin-top: 8px;
    padding: 6px 12px;
    font-size: .9rem;
    font-weight: 600;
    color: #fff;
    background: #1976d2;
    border: none;
    border-radius: 6px;
    cursor: pointer;
    text-decoration: none;
  }
  .book-modal .search-btn:hover { background: #0d47a1; }
</style>

<!-- View toggle control -->
<div id="view-toggle">
  <label class="vtoggle">
    <input type="checkbox" id="bookshelfToggle">
    <span class="slider"></span>
    <span class="label-text">Bookshelf mode</span>
  </label>
</div>

<!-- Modal root -->
<div id="bookModal" class="book-modal" aria-hidden="true">
  <div class="backdrop" data-close="1"></div>
  <div class="card" role="dialog" aria-modal="true" aria-labelledby="bookModalTitle">
    <button class="close" title="Close" aria-label="Close" data-close="1">×</button>
    <div id="bookModalTitle" class="title"></div>
    <div class="meta"></div>
    <div class="reactions"></div>
    <div class="raw"></div>
    <a id="bookSearchLink" class="search-btn" target="_blank" rel="noopener">🔎 Search on Google</a>
  </div>
</div>

<script>
(function () {
  function initBookshelf() {
    // Default to bookshelf mode (toggle is checked in markup)
    const toggle = document.getElementById('bookshelfToggle');
    const applyMode = () => {
      if (toggle.checked) document.body.classList.add('bookshelf-mode');
      else document.body.classList.remove('bookshelf-mode');
      // Close modal if switching off
      if (!toggle.checked) {
        const modal = document.getElementById('bookModal');
        if (modal.classList.contains('show')) {
          modal.classList.remove('show'); modal.setAttribute('aria-hidden','true');
          document.body.style.overflow="";
        }
      }
    };
    toggle.addEventListener('change', applyMode);
    applyMode();

    const booksHeader =
      document.getElementById('books') ||
      Array.from(document.querySelectorAll('h2')).find(h => h.textContent.trim().toLowerCase() === 'books');
    if (!booksHeader) return;

    // Collect original book <p> lines (until next H2)
    const lines = [];
    let el = booksHeader.nextElementSibling;
    while (el && el.tagName !== 'H2') {
      if (el.tagName === 'P') { lines.push(el); el.classList.add('book-raw'); }
      el = el.nextElementSibling;
    }
    if (!lines.length) return;

    const READING_KEY = 'Reading Now';
    const yearRe  = /\b(20\d{2}|21\d{2})\b/g;
    const emojiRe = /[📚✅👍🆗😕❤️]/g;

    const buckets = new Map(); // key -> items

    function classifySpine(text) {
      const hasEnjoyed = text.includes('👍');
      const hasOk      = text.includes('🆗');
      const hasMeh     = text.includes('😕');
      const hasReco    = text.includes('❤️');
      const noYear     = !text.match(yearRe); // no year = currently reading
      if (hasEnjoyed && hasReco) return 'spine-reco';
      if (noYear)     return 'spine-reading';
      if (hasEnjoyed) return 'spine-enjoyed';
      if (hasOk)      return 'spine-ok';
      if (hasMeh)     return 'spine-meh';
      return 'spine-neutral';
    }
    function mainTitle(text) {
      const withoutEmojis = text.replace(emojiRe, '').trim();
      const main = withoutEmojis.split(' - ')[0].trim(); // strip trailing " - Month Year"
      return main || withoutEmojis;
    }
    function lastYear(text) {
      const m = text.match(yearRe);
      return m ? m[m.length - 1] : null;
    }
    function reactionsText(text) {
      const r = [];
      if (text.includes('👍')) r.push('👍 Enjoyed');
      if (text.includes('🆗')) r.push('🆗 Ok');
      if (text.includes('😕')) r.push('😕 Meh');
      if (text.includes('❤️')) r.push('❤️ Recommend');
      if (text.trim().startsWith('📚') || !lastYear(text)) r.push('📚 Reading');
      return r.join(' · ');
    }
    function stripEmojis(text) {
      return text.replace(emojiRe, '').trim();
    }

    // Build buckets
    lines.forEach(p => {
      const raw = p.textContent || '';
      const y = lastYear(raw) || READING_KEY;
      const cls = classifySpine(raw);
      const title = mainTitle(raw);
      if (!buckets.has(y)) buckets.set(y, []);
      buckets.get(y).push({ raw, title, cls, year: y, p });
    });

    // Sort shelves: "Reading Now" first, then years desc
    const keys = Array.from(buckets.keys()).sort((a, b) => {
      if (a === READING_KEY && b !== READING_KEY) return -1;
      if (b === READING_KEY && a !== READING_KEY) return 1;
      if (a === READING_KEY && b === READING_KEY) return 0;
      return Number(b) - Number(a);
    });

    // Build bookshelf container once
    const wrapAll = document.createElement('div');
    wrapAll.className = 'bookshelf-wrap';
    booksHeader.insertAdjacentElement('afterend', wrapAll);

    // Modal refs
    const modal   = document.getElementById('bookModal');
    const titleEl = modal.querySelector('.title');
    const metaEl  = modal.querySelector('.meta');
    const reactEl = modal.querySelector('.reactions');
    const rawEl   = modal.querySelector('.raw');
    const searchEl= document.getElementById('bookSearchLink');
    let lastFocus = null;

    function openBookModal(item) {
      lastFocus = document.activeElement;
      titleEl.textContent = item.title;
      metaEl.textContent  = item.year === READING_KEY ? 'Reading Now' : `Year: ${item.year}`;
      reactEl.textContent = reactionsText(item.raw);
      rawEl.textContent   = item.raw;
      const q = encodeURIComponent(stripEmojis(item.title));
      searchEl.href = `https://www.google.com/search?q=${q}`;

      modal.classList.add('show');
      modal.setAttribute('aria-hidden','false');
      modal.querySelector('.close').focus();
      document.body.style.overflow='hidden';
    }
    function closeBookModal() {
      modal.classList.remove('show');
      modal.setAttribute('aria-hidden','true');
      document.body.style.overflow='';
      if (lastFocus && lastFocus.focus) lastFocus.focus();
    }
    modal.addEventListener('click',(e)=>{ if (e.target.dataset.close) closeBookModal(); });
    window.addEventListener('keydown',(e)=>{ if (e.key==='Escape' && modal.classList.contains('show')) closeBookModal(); });

    // Build shelves + spines
    keys.forEach(key => {
      const group = buckets.get(key);
      const sec = document.createElement('section');
      sec.className = 'year-shelf';

      const h3 = document.createElement('h3');
      h3.textContent = String(key);
      sec.appendChild(h3);

      const shelf = document.createElement('div');
      shelf.className = 'bookshelf';

      group.forEach(item => {
        const spine = document.createElement('div');
        spine.className = `book-spine ${item.cls}`;
        spine.title = item.raw; // native tooltip
        spine.textContent = item.title;
        spine.tabIndex = 0;

        if (item.cls === 'spine-reco') {
          const rib = document.createElement('div');
          rib.className = 'ribbon';
          rib.textContent = '⭐';
          spine.appendChild(rib);
        }

        spine.addEventListener('click', () => openBookModal(item));
        spine.addEventListener('keydown', (e) => {
          if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); openBookModal(item); }
        });

        shelf.appendChild(spine);
      });

      sec.appendChild(shelf);
      wrapAll.appendChild(sec);
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initBookshelf);
  } else {
    initBookshelf();
  }
})();
</script>
<!-- END VIEW TOGGLE + BOOKSHELF -->



# Books I've read

## Key
📚 Reading | ✅ Read | 👍 Enjoyed | 🆗 Ok | 😕 Meh | ❤️ Recommend |

## Books

✅ The Hotel Avocado: Bob Mortimer - December 2025 👍

✅ Hitchhiker's Guide to the Galaxy: Douglas Adams - December 2025 👍

✅ Pride and Prejudice: Jane Austen - December 2025 👍

✅ Mahabharata: Interpreted and Retold by Krishna Dharma - December 2025 👍

✅ White Nights: Fyodor Dostoyevsky - October 2025 👍

✅ Nexus: Yuval Noah Harari - September 2025 👍❤️

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

✅ The Alchemist: Paulo Coelho - June 2024 👍❤️

✅ Born to Run: Christopher McDougall - May 2024 👍❤️

✅ Dune: Frank Herbert - May 2024 👍❤️

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
