fetch('/chart')
    .then(response => response.json())
    .then(chartData => {
        // Render the Altair chart using Vega-Embed
        vegaEmbed('#chart', chartData)
            .catch(error => console.error('Error rendering chart:', error));
    })
    .catch(error => console.error('Error fetching chart data:', error));
