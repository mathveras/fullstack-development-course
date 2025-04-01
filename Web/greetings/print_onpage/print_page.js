// Ask the user its name.
userName = prompt("Enter your name: ");

// Verify if the user has actually entered something.
if (userName) {

    // Generate a welcome message.
    message = `Hi, ${userName}! You're much welcome!`;

    // Print a message on the console.
    console.log(message);

    // Print the message on an HTML element.
    welcomeElement = document.getElementById("welcome");
    welcomeElement.textContent = message;
}
else {
    errorElement = document.getElementById("error");
    errorElement.textContent = ("You need to enter a valid name!");

    errorElement.style.color = "red";
    errorElement.style.fontSize = "50px";
}

// Adds a style to the welcome element.
welcomeElement.style.color = "green";
welcomeElement.style.fontSize = "24px";
