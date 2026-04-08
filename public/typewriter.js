// JavaScript for typewriter effect on homepage
// Types out "hi, i'm alice!" one character at a time, then blinks the cursor 3 times
document.addEventListener("DOMContentLoaded", function () {
  const text = "hi, i'm alice!";
  const typedText = document.getElementById("typed-text");
  const cursor = document.getElementById("cursor");
  let index = 0;

  const type = () => {
    typedText.textContent += text.charAt(index);
    index++;
    if (index < text.length) {
      setTimeout(type, 100);
    } else {
      blinkCursor(3);
    }
  };

  const blinkCursor = (blinks) => {
    let count = 0;
    const blinkInterval = setInterval(() => {
      cursor.style.visibility = (cursor.style.visibility === "visible") ? "hidden" : "visible";
      count++;
      if (count >= blinks * 2) {
        clearInterval(blinkInterval);
        cursor.style.visibility = "hidden";
      }
    }, 500);
  };

  type();
});
