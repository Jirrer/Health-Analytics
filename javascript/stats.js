let selectedCountyHealth = null; // Store the selected county health element
const defaultCountyRegionFile  = "../BackEnd/Data/HealthData/emptyHealth.csv"; // Default health data CSV path

// Function to fetch CSV data based on selected county region
function fetchCountyCSVData(url, callback) {
    fetch(url)
        .then(response => response.text())
        .then(csvText => {
            Papa.parse(csvText, {
                header: true,
                dynamicTyping: true,
                complete: function(results) {
                    callback(results.data);
                }
            });
        })
        .catch(error => console.error('Error fetching CSV:', error));
}

function processHealthData(input) {
    if (input == 1) {return 300} 
    else {return 300 - (input * 3.75);}
}



// Process CSV data to extract labels (Years) and values (Factors) for county health data
function processCountyHealthData(data) {
    const years = [];
    const values = [];

    data.forEach(row => {
        if (row['Outcome'] != null && !isNaN(row['Outcome'])) {
            years.push(row['Year']);
            const processedValue = processHealthData(parseFloat(row['Outcome']));
            values.push(processedValue);
        }
    });

    return { years, values };
}


// Function to render the line chart for county health data
function renderCountyHealth(svg, data, years, width, height) {
    const padding = 30;
    const shift = 35;

    svg.innerHTML = '';

    const fixedMaxValue = 300;
    const xStep = (width - 2 * padding - shift) / (years.length - 1);
    const yStep = (height - 2 * padding) / fixedMaxValue;

    const line = document.createElementNS('http://www.w3.org/2000/svg', 'polyline');
    const linePoints = data.map((value, index) => {
        const x = padding + index * xStep + shift;
        const y = height - padding - value * yStep;
        return `${x},${y}`;
    }).join(' ');  
    line.setAttribute('points', linePoints);
    line.setAttribute('class', 'line');
    line.setAttribute('stroke', '#66ccff');  
    line.setAttribute('stroke-width', '3');
    line.setAttribute('fill', 'none');  
    svg.appendChild(line);

    data.forEach((value, index) => {
        const x = padding + index * xStep + shift;
        const y = height - padding - value * yStep;
        const point = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
        point.setAttribute('cx', x);
        point.setAttribute('cy', y);
        point.setAttribute('r', 2);
        point.setAttribute('class', 'point');
        svg.appendChild(point);
    });

    years.forEach((year, index) => {
        const x = padding + index * xStep + shift;
        const y = height - padding + 20;
        const text = document.createElementNS('http://www.w3.org/2000/svg', 'text');
        text.setAttribute('x', x - 10);
        text.setAttribute('y', y);
        text.setAttribute('class', 'label');
        text.textContent = year;
        svg.appendChild(text);
    });

    const customLabels = ['80','70','60','50','40','30','20','10','1'];

    const numberOfLabels = customLabels.length;
    const maxCustomLabelValue = 300;
    for (let i = 0; i < numberOfLabels; i++) {
        const yValue = maxCustomLabelValue * (i / (numberOfLabels - 1));
        const yPosition = height - padding - (yValue * yStep);

        const horizontalLine = document.createElementNS('http://www.w3.org/2000/svg', 'line');
        horizontalLine.setAttribute('x1', 65);
        horizontalLine.setAttribute('y1', yPosition);
        horizontalLine.setAttribute('x2', width - padding);
        horizontalLine.setAttribute('y2', yPosition);
        horizontalLine.setAttribute('stroke', 'gray');
        horizontalLine.setAttribute('stroke-width', '1');
        svg.appendChild(horizontalLine);

        const label = document.createElementNS('http://www.w3.org/2000/svg', 'text');
        label.setAttribute('x', 60);
        label.setAttribute('y', yPosition + 5);
        label.setAttribute('text-anchor', 'end');
        label.setAttribute('font-size', '12');
        label.setAttribute('fill', 'black');
        label.textContent = customLabels[i];
        svg.appendChild(label);
    }
}

// Function to initialize the chart with the default county region data
function initializeDefaultCountyRegion() {
    const container = document.querySelector('.statGrid');
    const svg = document.getElementById('healthChart');

    // Fetch and process data for the default county region
    fetchCountyCSVData(defaultCountyRegionFile, function(csvData) {
        const { years, values } = processCountyHealthData(csvData);

        // Resize observer for dynamic resizing
        const observer = new ResizeObserver(() => {
            const width = container.clientWidth;
            const height = container.clientHeight;
            renderCountyHealth(svg, values, years, width, height);
        });
        observer.observe(container);

        // Initial render
        const initialWidth = container.clientWidth;
        const initialHeight = container.clientHeight;
        renderCountyHealth(svg, values, years, initialWidth, initialHeight);
    });
}

// Event listener for clicking on a county region
document.querySelectorAll('svg [class]').forEach(region => {
    region.addEventListener('mousedown', (event) => {
        if (event.button === 0) { // Left click
            // Change the color of the selected county region
            selectedCountyHealth = region;

            // Update the file name for the selected county region
            const regionName = region.getAttribute('class'); // Get the county region's name from its class
            const fileName = `../BackEnd/Data/HealthData/${regionName}.csv`;

            // Fetch and process the data for the selected county region
            fetchCountyCSVData(fileName, function(csvData) {
                const { years, values } = processCountyHealthData(csvData);
                const container = document.querySelector('.statGrid');
                const svg = document.getElementById('healthChart');

                // Resize observer for dynamic resizing
                const observer = new ResizeObserver(() => {
                    const width = container.clientWidth;
                    const height = container.clientHeight;
                    renderCountyHealth(svg, values, years, width, height);
                });
                observer.observe(container);

                // Initial render
                const initialWidth = container.clientWidth;
                const initialHeight = container.clientHeight;
                renderCountyHealth(svg, values, years, initialWidth, initialHeight);
            });
        }
    });
});

// Initialize the chart with the default county region on page load
initializeDefaultCountyRegion();
