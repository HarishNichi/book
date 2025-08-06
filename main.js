document.addEventListener("DOMContentLoaded", () => {
    document.body.classList.add('fade-in');

    // We can add this class to avoid the animation from re-triggering
    // if the user navigates back to the page.
    setTimeout(() => {
        document.body.classList.add('loaded');
    }, 500); // 500ms should match the animation duration

    const pages = document.querySelectorAll('.page-content-container');
    const prevButton = document.getElementById('prev-page');
    const nextButton = document.getElementById('next-page');
    const pageNumber = document.getElementById('page-number');

    let currentPage = 0;

    function showPage(pageIndex) {
        pages.forEach((page, index) => {
            if (index === pageIndex) {
                page.style.display = 'block';
            } else {
                page.style.display = 'none';
            }
        });
        pageNumber.textContent = `Page ${pageIndex + 1}`;
        prevButton.disabled = pageIndex === 0;
        nextButton.disabled = pageIndex === pages.length - 1;
    }

    prevButton.addEventListener('click', () => {
        if (currentPage > 0) {
            currentPage--;
            showPage(currentPage);
        }
    });

    nextButton.addEventListener('click', () => {
        if (currentPage < pages.length - 1) {
            currentPage++;
            showPage(currentPage);
        }
    });

    showPage(currentPage);
});