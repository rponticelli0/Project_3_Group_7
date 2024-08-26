document.addEventListener('DOMContentLoaded', function() {
    fetch('/data')
        .then(response => response.json())
        .then(data => {
            const container = document.getElementById('data-container');
            data.forEach(row => {
                const rowDiv = document.createElement('div');
                rowDiv.innerHTML = `
                    <p>Twitch Monthly: ${row.twitch_monthly}</p>
                    <p>Steam Twitch Aggregate: ${row.steam_twitch_agg}</p>
                    <p>Tags: ${row.tags}</p>
                    <hr>
                `;
                container.appendChild(rowDiv);
            });
        })
        .catch(error => console.error('Error fetching data:', error));
});
