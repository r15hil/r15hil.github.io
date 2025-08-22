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

<!-- MULTIPLE BOUNCING BALLS START -->
<style>
  .bouncer {
    position: fixed;
    top: 0;
    left: 0;
    width: 60px;
    height: 60px;
    border-radius: 50%;
    pointer-events: none;
    z-index: 9999;
    will-change: transform;
  }
  #ball1 { background: linear-gradient(135deg, #4caf50, #2196f3); }
  #ball2 { background: linear-gradient(135deg, #ff9800, #f44336); }
  #ball3 { background: linear-gradient(135deg, #9c27b0, #e91e63); }
</style>

<div id="ball1" class="bouncer"></div>
<div id="ball2" class="bouncer"></div>
<div id="ball3" class="bouncer"></div>

<script>
(function() {
  const balls = [
    { el: document.getElementById("ball1"), x: 100, y: 100, vx: 3, vy: 2, r: 30 },
    { el: document.getElementById("ball2"), x: 200, y: 200, vx: -2, vy: 3, r: 30 },
    { el: document.getElementById("ball3"), x: 300, y: 150, vx: 2.5, vy: -2.5, r: 30 }
  ];

  function step() {
    const maxX = window.innerWidth;
    const maxY = window.innerHeight;

    // move + wall bounce
    balls.forEach(b => {
      b.x += b.vx;
      b.y += b.vy;

      if (b.x <= 0 || b.x + b.r * 2 >= maxX) {
        b.vx *= -1;
        b.x = Math.max(0, Math.min(b.x, maxX - b.r * 2));
      }
      if (b.y <= 0 || b.y + b.r * 2 >= maxY) {
        b.vy *= -1;
        b.y = Math.max(0, Math.min(b.y, maxY - b.r * 2));
      }
    });

    // ball-ball collision detection
    for (let i = 0; i < balls.length; i++) {
      for (let j = i + 1; j < balls.length; j++) {
        const bi = balls[i], bj = balls[j];
        const dx = (bi.x + bi.r) - (bj.x + bj.r);
        const dy = (bi.y + bi.r) - (bj.y + bj.r);
        const dist = Math.sqrt(dx * dx + dy * dy);
        if (dist < bi.r + bj.r) {
          // Simple elastic collision: swap velocities
          const tmpVx = bi.vx;
          const tmpVy = bi.vy;
          bi.vx = bj.vx;
          bi.vy = bj.vy;
          bj.vx = tmpVx;
          bj.vy = tmpVy;

          // Push them apart to avoid sticking
          const overlap = (bi.r + bj.r) - dist;
          const nx = dx / dist, ny = dy / dist;
          bi.x += nx * overlap / 2;
          bi.y += ny * overlap / 2;
          bj.x -= nx * overlap / 2;
          bj.y -= ny * overlap / 2;
        }
      }
    }

    // render
    balls.forEach(b => {
      b.el.style.transform = `translate(${b.x}px, ${b.y}px)`;
    });

    requestAnimationFrame(step);
  }

  window.addEventListener("resize", () => {
    balls.forEach(b => {
      b.x = Math.min(b.x, window.innerWidth - b.r * 2);
      b.y = Math.min(b.y, window.innerHeight - b.r * 2);
    });
  });

  step();
})();
</script>
<!-- MULTIPLE BOUNCING BALLS END -->
