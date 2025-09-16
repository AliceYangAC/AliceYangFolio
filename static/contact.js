document.getElementById("submit-btn").addEventListener("click", function () {
  const name = document.getElementById("name").value.trim();
  const email = document.getElementById("email").value.trim();
  const message = document.getElementById("message").value.trim();
  const responseBox = document.getElementById("form-response");

  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

  if (!name || !email || !message) {
    responseBox.textContent = "Please fill out all fields.";
    responseBox.style.color = "red";
    return;
  }

  if (!emailRegex.test(email)) {
    responseBox.textContent = "Please enter a valid email address.";
    responseBox.style.color = "red";
    return;
  }

  const data = { name, email, message };

  fetch("https://formspree.io/f/mgvljwko", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "Accept": "application/json"
    },
    body: JSON.stringify(data)
  })
  .then(response => {
    if (response.ok) {
      responseBox.textContent = "Thanks for reaching out! I'll be in touch soon.";
      responseBox.style.color = "green";
      document.getElementById("contact-form").reset?.();
    } else {
      responseBox.textContent = "Oops! Something went wrong.";
      responseBox.style.color = "red";
    }
  })
  .catch(() => {
    responseBox.textContent = "Network error. Please try again later.";
    responseBox.style.color = "red";
  });
});
