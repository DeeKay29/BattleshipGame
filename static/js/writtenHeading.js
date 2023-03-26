const heading = 'Welcome in Battleship Game';
const timeBetweenLetters = 100;
const cursorBlinkInterval = 500;

let index = 0;

const addLetter = () => {
    const typewriter = document.getElementById('typewriter');
    const cursor = document.getElementById('cursor');

    // Add letter
    typewriter.textContent += heading.charAt(index);
    index++;

    // If all the text has already been typed, start blinking the cursor
    if (index === heading.length) {
        clearInterval(intervalId);
        setInterval(() => {
            cursor.style.visibility = cursor.style.visibility === 'hidden' ? 'visible' : 'hidden';
        }, cursorBlinkInterval);
    }
};

const intervalId = setInterval(addLetter, timeBetweenLetters);
