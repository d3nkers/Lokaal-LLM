document.addEventListener("DOMContentLoaded", () => {
    document.getElementById("user-input").addEventListener("keypress", function(event) {
        if (event.key === "Enter") {
            sendMessage();
        }
    });
});

function sendMessage() {
    let userInput = document.getElementById("user-input").value.trim();
    if (userInput === "") return;

    let chatOutput = document.getElementById("chat-output");
    chatOutput.innerHTML += `<div><b>Jij:</b> ${userInput}</div>`;

    document.getElementById("user-input").value = "";

    fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: userInput, model: "llama3" })
    })
    .then(response => response.json())
    .then(data => {
        chatOutput.innerHTML += `<div><b>Pindahoofd:</b> ${data.response}</div>`;
        chatOutput.scrollTop = chatOutput.scrollHeight;
    })
    .catch(error => {
        chatOutput.innerHTML += `<div><b>!!Fout:</b> Kan geen verbinding maken met de server.</div>`;
    });
}
