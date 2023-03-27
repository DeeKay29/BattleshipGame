// Get all the cell IDs and send them to the server
document.addEventListener('DOMContentLoaded', (event) => {
    var cells = document.querySelectorAll('.board-cell');
    cells.forEach((cell) => {
        cell.addEventListener('click', () => {
            var cellId = this.getAttribute('id');
            sendCellIdToPython(cellId);
        });
    });
});

// Function to send the cell ID to the server using fetch
const sendCellIdToPython = (cellId) => {
    fetch('/', {
        method: 'POST',
        body: JSON.stringify({ cellId: cellId }),
        headers: { 'Content-Type': 'application/json' },
    })
        .then((response) => response.json())
        .then((data) => console.log(data))
        .catch((error) => console.error(error));
};
