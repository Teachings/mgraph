const graphDiv = document.getElementById('graph');
const stateDiv = document.getElementById('state');

const ws = new WebSocket("ws://127.0.0.1:8000/ws");

ws.onmessage = function(event) {
    const data = JSON.parse(event.data);
    graphDiv.innerHTML = data.graph;
    stateDiv.textContent = JSON.stringify(data.state, null, 2);
    if (data.completed) {
        ws.close();
    }
};

ws.onclose = function(event) {
    console.log('WebSocket connection closed:', event);
};

ws.onerror = function(error) {
    console.error('WebSocket error observed:', error);
};