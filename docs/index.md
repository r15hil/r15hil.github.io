<style>
  p {
    font-family: Arial, sans-serif;
    font-size: 18px;
    line-height: 1.5;
    margin-bottom: 20px;
  }

  span {
    font-weight: bold;
  }
</style>

<p>Today is: <span id="date"></span></p>
<!-- <p>Days since I was born: <span id="days"></span></p> -->

<script>
  // Set the target date
  const targetDate = new Date("1999-12-06");
  
  // Get the current date
  const currentDate = new Date();
  
  // Display the current date
  document.querySelector("#date").innerHTML = currentDate.toDateString();
  
  // Calculate the number of days between the target date and the current date
  const timeDiff = Math.abs(currentDate.getTime() - targetDate.getTime());
  const dayDiff = Math.ceil(timeDiff / (1000 * 3600 * 24));
  
  // Display the number of days
  document.querySelector("#days").innerHTML = dayDiff;
</script>

## [About Me](introduction/introduction.md)

Learn more about me.

## [Reading](books/books.md)

A list of books I've read, or currently reading, or plan to read.

## [Other](misc/misc.md)

<!-- BOUNCING OBJECT START -->
<style>
  #bouncer {
    position: fixed;
    top: 50px;
    left: 50px;
    width: 60px;
    height: 60px;
    border-radius: 50%;
    background: linear-gradient(135deg, #4caf50, #2196f3);
    box-shadow: 0 4px 8px rgba(0,0,0,0.3);
    pointer-events: none; /* so it doesn't block clicks */
    z-index: 9999;        /* always on top */
  }
</style>

<div id="bouncer"></div>

<script>
  (function() {
    const el = document.getElementById("bouncer");
    let x = 100, y = 100;
    let vx = 3, vy = 2; // velocity in px/frame

    function animate() {
      const w = window.innerWidth;
      const h = window.innerHeight;
      const rect = el.getBoundingClientRect();

      x += vx;
      y += vy;

      // Bounce on edges
      if (x <= 0 || x + rect.width >= w) {
        vx *= -1;
        x = Math.max(0, Math.min(x, w - rect.width));
      }
      if (y <= 0 || y + rect.height >= h) {
        vy *= -1;
        y = Math.max(0, Math.min(y, h - rect.height));
      }

      el.style.transform = `translate(${x}px, ${y}px)`;

      requestAnimationFrame(animate);
    }

    animate();
  })();
</script>
<!-- BOUNCING OBJECT END -->
