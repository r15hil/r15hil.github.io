---
title: Home
---

<section class="hero">
  <p class="eyebrow">Personal site</p>
  <h1>Rishil</h1>
  <p class="lede">A small, self-contained website for notes, reading, and practical tools. It stays markdown-first, so adding a page is still just adding a file.</p>
  <p class="date-pill">Today is <span id="date"></span></p>
</section>

<section class="quick-links" aria-label="Main sections">
  <a class="quick-card" href="{{ '/introduction/introduction.html' | relative_url }}">
    <strong>About Me</strong>
    <span>A short introduction and background.</span>
  </a>
  <a class="quick-card" href="{{ '/books/books.html' | relative_url }}">
    <strong>Reading</strong>
    <span>Books read, current reads, ratings, and recommendations.</span>
  </a>
  <a class="quick-card" href="{{ '/misc/misc.html' | relative_url }}">
    <strong>Misc</strong>
    <span>Small utilities, recipes, experiments, and notes.</span>
  </a>
</section>
