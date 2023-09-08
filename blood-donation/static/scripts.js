// JavaScript to toggle the mobile menu
document.addEventListener("DOMContentLoaded", function () {
    const mobileMenuToggle = document.querySelector(".mobile-menu-toggle");
    const leftNavbar = document.querySelector("#left-navbar");

    mobileMenuToggle.addEventListener("click", function () {
        leftNavbar.classList.toggle("show");
        mobileMenuToggle.classList.toggle("open");
    });

    // JavaScript for handling the timeline events (if needed)
    const timelineEvents = document.querySelectorAll(".timeline-event");

    timelineEvents.forEach((event) => {
        event.addEventListener("click", () => {
            event.classList.toggle("active");
        });
    });

    // JavaScript for scrolling to the footer
    const scrollToFooterLink = document.getElementById('scrollToFooter');
    scrollToFooterLink.addEventListener('click', function(event) {
        event.preventDefault(); // Prevent the default link behavior (navigating to the anchor)
        
        const footer = document.getElementById('footer');
        footer.scrollIntoView({ behavior: 'smooth' });
    });

    // JavaScript for scrolling to the middle of the hero section
    const heroSection = document.querySelector('.hero-page');
    const scrollLinks = document.querySelectorAll('.scroll-to-hero');

    scrollLinks.forEach(link => {
        link.addEventListener('click', function (event) {
            event.preventDefault(); // Prevent the default link behavior (e.g., navigating to '#')

            // Calculate the position to scroll to (middle of the hero section)
            const heroTopOffset = heroSection.offsetTop;
            const heroHeight = heroSection.clientHeight;
            const scrollToY = heroTopOffset + heroHeight / 2;

            // Scroll to the calculated position with smooth behavior
            window.scrollTo({
                top: scrollToY,
                behavior: 'smooth'
            });
        });
    });

    // Scheduling JavaScript
    // Get the form element
    const appointmentForm = document.getElementById("appointment-form");

    appointmentForm.addEventListener("submit", function (e) {
        e.preventDefault();

        // Get the user input values
        const appointmentDate = document.getElementById("appointment-date").value;
        const appointmentTime = document.getElementById("appointment-time").value;

        // You can perform further actions with the appointment date and time here
        // For example, you can send them to a server using AJAX for backend processing

        // For this example, we'll just display a message
        alert(`Appointment scheduled for Date: ${appointmentDate}, Time: ${appointmentTime}`);
    });
});
