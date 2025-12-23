function updateSidebar(docName, historyHtml) {
    document.getElementById('sidebar-title').innerText = docName + " History";
    document.getElementById('lifecycle-content').innerHTML = historyHtml;

    // Highlights active row
    const rows = document.querySelectorAll('tr');
    rows.forEach(r => r.classList.remove('active'));
    event.currentTarget.classList.add('active');
}
