function generatePrompt() {
    const topic = document.getElementById("topicInput").value;
    
    if (!topic) {
        alert("Please enter a topic.");
        return;
    }

    fetch("/generate-prompt", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ topic: topic })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("result").innerText = data.generated_prompt;
    })
    .catch(error => console.error("Error:", error));
}
