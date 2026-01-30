document.addEventListener("DOMContentLoaded", function () {
    // 🔹 Collapsible group logic
    document.querySelectorAll('.app-group h2').forEach(header => {
        header.addEventListener('click', () => {
            const group = header.parentElement;
            group.classList.toggle('collapsed');
        });
    });

    // 🔹 Sticky sidebar scroll logic
    const sidebar = document.querySelector('#nav-sidebar');

    // Restore previous scroll position if available
    if (sidebar && localStorage.getItem("sidebarScrollTop")) {
        sidebar.scrollTop = parseInt(localStorage.getItem("sidebarScrollTop"), 10);
    }

    // Save the scroll position before navigating away
    window.addEventListener("beforeunload", function () {
        if (sidebar) {
            localStorage.setItem("sidebarScrollTop", sidebar.scrollTop);
        }
    });
});
