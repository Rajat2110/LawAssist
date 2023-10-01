// chatbot.js
document.addEventListener('DOMContentLoaded', function () {
    const chatForm = document.getElementById('chat-form');
    const chatMessages = document.getElementById('chat-messages');
    const userInput = document.getElementById('user-input');

    chatForm.addEventListener('submit', function (e) {
        e.preventDefault();

        const userMessage = userInput.value;
        userInput.value = '';

        // Display the user's message in the chat
        const userMessageDiv = document.createElement('div');
        userMessageDiv.className = 'user-message';
        userMessageDiv.innerHTML = `<strong>You:</strong> ${userMessage}`;
        chatMessages.appendChild(userMessageDiv);

        // Send the user's message to the server for processing
        fetch(chatForm.action, {
            method: 'POST',
            headers: {
                'X-CSRFToken': chatForm.elements.csrfmiddlewaretoken.value,
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ user_input: userMessage }),
        })
            .then((response) => response.json())
            .then((data) => {
                // Display the chatbot's response in the chat
                const chatbotMessageDiv = document.createElement('div');
                chatbotMessageDiv.className = 'chatbot-message';
                chatbotMessageDiv.innerHTML = `<strong>Chatbot:</strong> ${data.message}`;
                chatMessages.appendChild(chatbotMessageDiv);
            })
            .catch((error) => {
                console.error('Error:', error);
            });
    });
});
