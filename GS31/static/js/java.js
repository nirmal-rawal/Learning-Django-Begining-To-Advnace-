// script.js

document.addEventListener('DOMContentLoaded', function() {
    const contactForm = document.getElementById('contactForm');
    
    contactForm.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevents the default form submission
        
        // Display a message when the form is submitted
        alert('Thank you for your message!');
        
        // Clear the form
        contactForm.reset();
    });
});
