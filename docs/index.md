# Rishil

- [Introduction](introduction/introduction.md) 
- [Experience](experience/experience.md)
- [AI generated things](ai/ai.md)
- [Books I've read](books/books.md)

<p>Today is: <span id="date"></span></p>
<p>Days since I was born: <span id="days"></span></p>

<script>
  // Set the target date
  const targetDate = new Date("1999-06-12");
  
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
