document.addEventListener('DOMContentLoaded', () => {
    const chatHistory = document.getElementById('chat-history');
    const userInput = document.getElementById('user-input');
    const sendBtn = document.getElementById('send-btn');
    const metricsDiv = document.getElementById('metrics');
    const sSpan = document.getElementById('s-value');
    const eSpan = document.getElementById('e-value');
    const iSpan = document.getElementById('i-value');

    // Load history on startup (optional)
    loadHistory();

    sendBtn.addEventListener('click', sendMessage);
    userInput.addEventListener('keydown', (e) => {
        if (e.key === 'Enter') sendMessage();
    });

    function sendMessage() {
        const message = userInput.value.trim();
        if (!message) return;
        // Add user message to chat
        appendMessage('user', message);
        userInput.value = '';
        // Show loading
        const loadingId = appendMessage('agent', 'Thinking...', true);

        fetch('/api/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message: message })
        })
        .then(response => response.json())
        .then(data => {
            // Remove loading message
            document.getElementById(loadingId)?.remove();
            if (data.response) {
                appendMessage('agent', data.response);
                // Show metrics if available
                if (data.s_value !== undefined) {
                    sSpan.textContent = data.s_value.toFixed(3);
                    eSpan.textContent = data.e_value.toFixed(3);
                    iSpan.textContent = data.i_value.toFixed(3);
                    metricsDiv.style.display = 'block';
                }
            } else {
                appendMessage('agent', 'Error: No response received.');
            }
        })
        .catch(error => {
            document.getElementById(loadingId)?.remove();
            appendMessage('agent', 'Error: Could not reach server.');
            console.error(error);
        });
    }

    function appendMessage(role, text, isTemp = false) {
        const msgDiv = document.createElement('div');
        msgDiv.className = `message ${role}`;
        if (isTemp) msgDiv.id = 'temp-' + Date.now();
        msgDiv.textContent = text;
        chatHistory.appendChild(msgDiv);
        chatHistory.scrollTop = chatHistory.scrollHeight;
        return msgDiv.id;
    }

    function loadHistory() {
        fetch('/api/history')
        .then(res => res.json())
        .then(data => {
            // Clear chat
            chatHistory.innerHTML = '';
            data.forEach(item => {
                appendMessage('user', item.user);
                appendMessage('agent', item.agent);
            });
        })
        .catch(err => console.warn('Could not load history', err));
    }
});
