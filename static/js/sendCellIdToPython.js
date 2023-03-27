document.addEventListener('DOMContentLoaded', (event) => {
    var cells = document.querySelectorAll('.board-cell');
    cells.forEach((cell) => {
        cell.addEventListener('click', () => {
            var cellId = this.getAttribute('id');
            sendCellIdToPython(cellId);
        });
    });
});

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
