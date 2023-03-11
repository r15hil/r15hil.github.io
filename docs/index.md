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
## [Personal Projects](projects/projects.md)

See some of my the stuff I do randomly.

## [Experience](experience/experience.md)

Learn more about my professional experience, including my work history and skills.
## [Books I've Read](books/books.md)

A list of books I've read, or currently reading, or plan to read.

## [Reviews](reviews/reviews.md)

Some reviews of places I've been to or things I've done.

## [Miscellaneous](misc/misc.md)

Here's some stuff that doesn't fit anywhere else but I want to document somewhere.