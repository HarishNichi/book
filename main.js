document.addEventListener("DOMContentLoaded", () => {
    document.body.classList.add('fade-in');

    // We can add this class to avoid the animation from re-triggering
    // if the user navigates back to the page.
    setTimeout(() => {
        document.body.classList.add('loaded');
    }, 500); // 500ms should match the animation duration
});