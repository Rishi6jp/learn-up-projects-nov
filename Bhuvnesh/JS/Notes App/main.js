const notesContainer = document.querySelector(".notes-container"); // Added dot for class selector
const createBtn = document.querySelector(".btn"); // Added dot for class selector
let notes = document.querySelectorAll(".input-box");

function showNotes() {
    notesContainer.innerHTML = localStorage.getItem("notes") || ""; // Handles case if no notes are stored
}
showNotes();

function updateStorage() {
    localStorage.setItem("notes", notesContainer.innerHTML);
}

createBtn.addEventListener("click", () => {
    let inputBox = document.createElement("p");
    let img = document.createElement("img");
    inputBox.className = "input-box";
    inputBox.setAttribute("contenteditable", "true");
    img.src = "./notes-app-img/images/delete.png";
    
    inputBox.appendChild(img); // Append img to inputBox
    notesContainer.appendChild(inputBox); // Append inputBox to notesContainer
    
    // Update storage on keyup for the new note
    inputBox.onkeyup = function () {
        updateStorage();
    };
    updateStorage(); // Update storage after adding a new note
});

notesContainer.addEventListener("click", function(e) {
    if (e.target.tagName === "IMG") {
        e.target.parentElement.remove();
        updateStorage();
    } else if (e.target.tagName === "P") {
        // Refresh notes collection
        notes = document.querySelectorAll(".input-box");
        notes.forEach(nt => {
            nt.onkeyup = function() {
                updateStorage();
            };
        });
    }
});

