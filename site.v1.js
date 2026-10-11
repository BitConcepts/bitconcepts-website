// BitConcepts interstitial redirect — 5s countdown to Axiovex Systems.
// Cancellable via "Stay on this page", and cancelled automatically if the
// visitor heads to /research/ (that link is a normal navigation).
(function () {
  var DEST = "https://axiovexsystems.com/";
  var remaining = 5;
  var el = document.getElementById("seconds");
  var note = document.getElementById("countdown");
  var timer = setInterval(function () {
    remaining -= 1;
    if (remaining <= 0) {
      clearInterval(timer);
      window.location.replace(DEST);
      return;
    }
    if (el) el.textContent = String(remaining);
  }, 1000);
  var stay = document.getElementById("stay");
  if (stay) {
    stay.addEventListener("click", function (ev) {
      ev.preventDefault();
      clearInterval(timer);
      if (note) note.textContent = "Redirect paused — use the button above whenever you're ready.";
    });
  }
})();
