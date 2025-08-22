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
    top: 0;
    left: 0;
    width: 60px;
    height: 60px;
    border-radius: 50%;
    background: linear-gradient(135deg, #4caf50, #2196f3);
    box-shadow: 0 4px 8px rgba(0,0,0,0.3);
    pointer-events: none;
    z-index: 9999;
    will-change: transform;
  }
</style>

<div id="bouncer"></div>

<script>
  (function () {
    const el = document.getElementById("bouncer");
    let x = 100, y = 100;
    let vx = 3, vy = 2;

    function step() {
      const maxX = window.innerWidth - el.offsetWidth;
      const maxY = window.innerHeight - el.offsetHeight;

      x += vx;
      y += vy;

      if (x <= 0 || x >= maxX) {
        vx *= -1;
        x = Math.max(0, Math.min(x, maxX));
      }
      if (y <= 0 || y >= maxY) {
        vy *= -1;
        y = Math.max(0, Math.min(y, maxY));
      }

      el.style.transform = `translate(${x}px, ${y}px)`;
      requestAnimationFrame(step);
    }

    // keep it in bounds on resize
    window.addEventListener("resize", () => {
      x = Math.min(x, window.innerWidth - el.offsetWidth);
      y = Math.min(y, window.innerHeight - el.offsetHeight);
    });

    step();
  })();
</script>
<!-- BOUNCING OBJECT END -->
