(function () {
  var today = document.getElementById("today");
  if (today) {
    today.textContent = "Today is " + new Date().toLocaleDateString(undefined, {
      weekday: "long",
      year: "numeric",
      month: "long",
      day: "numeric"
    });
  }

  var dateInline = document.getElementById("date");
  if (dateInline) {
    dateInline.textContent = new Date().toDateString();
  }
})();
