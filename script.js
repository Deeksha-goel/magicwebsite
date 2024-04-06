document
  .getElementById("contactForm")
  .addEventListener("submit", function (event) {
    event.preventDefault(); // Prevent the form from submitting

    // Get values from form inputs
    var name = document.getElementById("name").value;
    var email = document.getElementById("email").value;
    var message = document.getElementById("message").value;

    // Log values to console (replace this with your own logic)
    console.log("Name: ", name);
    console.log("Email: ", email);
    console.log("Message: ", message);

    // Clear form fields
    document.getElementById("name").value = "";
    document.getElementById("email").value = "";
    document.getElementById("message").value = "";

    // Alert message (replace this with your own logic)
    alert("Your message has been sent!");
  });
