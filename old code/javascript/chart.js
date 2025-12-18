let selectedCounty = null; 
const defaultCountyFile = "../BackEnd/Data/CountyData/emptyChart.csv"; // Default county CSV path
const allCounties = document.querySelectorAll('.Alcona, .Alger, .Allegan, .Alpena, .Antrim, .Arenac, .Baraga, .Barry, .Bay, .Benzie, .Berrien, .Branch, .Calhoun, .Cass, .Charlevoix, .Cheboygan, .Chippewa, .Clare, .Clinton, .Crawford, .Delta, .Dickinson, .Eaton, .Emmet, .Genesee, .Gladwin, .Gogebic, .GrandTraverse, .Gratiot, .Hillsdale, .Houghton, .Huron, .Ingham, .Ionia, .Iosco, .Isabella, .Iron, .Jackson, .Kalamazoo, .Kalkaska, .Kent, .Keweenaw, .Lake, .Lapeer, .Leelanaw, .Lenawee, .Luce, .Livingston, .Mackinac, .Macomb, .Manistee, .Mason, .Mecosta, .Menominee, .Midland, .Missaukee, .Monroe, .Montcalm, .Montmorency, .Muskegon, .Newaygo, .Oakland, .Oceana, .Ogemaw, .Osceola, .Ottawa, .PresqueIsle, .Roscommon, .Saginaw, .Sanilac, .Schoolcraft, .Shiawassee, .St_Clair, .St_Joseph, .Tuscola, .VanBuren, .Washtenaw, .Wayne, .Wexford, .Oscoda, .Otsego, .Marquette, .Ontonagon');

function fetchCSVData(url, callback) {
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

function processData(input) {
    if (input <= 10000) {
        return (input / 100) / 2;
    } else if (input < 200000) {
        return (input / 1000) + 50;
    } else if (input >= 200000) {
        return (input / 2000) + 150;
    } else {
        return 0;
    }
}

function processCSVData(data) {
    const labels = [];
    const values = [];

    data.forEach(row => {
        if (row['Value'] != null && !isNaN(row['Value'])) {
            labels.push(row['Year']);
            const processedValue = processData(parseFloat(row['Value']));
            values.push(processedValue);
        }
    });

    return { labels, values };
}

function renderChart(svg, inputData, labels, width, height) {
    const padding = 30;
    const shift = 35;

    svg.innerHTML = '';

    const fixedMaxValue = 300;
    const xStep = (width - 2 * padding - shift) / (labels.length - 1);
    const yStep = (height - 2 * padding) / fixedMaxValue;

    const line = document.createElementNS('http://www.w3.org/2000/svg', 'polyline');
    const linePoints = inputData.map((value, index) => {
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

    inputData.forEach((value, index) => {
        const x = padding + index * xStep + shift;
        const y = height - padding - value * yStep;
        const point = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
        point.setAttribute('cx', x);
        point.setAttribute('cy', y);
        point.setAttribute('r', 2);
        point.setAttribute('class', 'point');
        svg.appendChild(point);
    });

    labels.forEach((label, index) => {
        const x = padding + index * xStep + shift;
        const y = height - padding + 20;
        const text = document.createElementNS('http://www.w3.org/2000/svg', 'text');
        text.setAttribute('x', x - 10);
        text.setAttribute('y', y);
        text.setAttribute('class', 'label');
        text.textContent = label;
        svg.appendChild(text);
    });

    const customLabels = ['$0','$10,000', '$50,000', '$100,000', '$150,000', '$200,000', '$300,000'];

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

function initializeDefaultCounty() {
    const container = document.querySelector('.chartGrid');
    const svg = document.getElementById('lineChart');

    fetchCSVData(defaultCountyFile, function(csvData) {
        const { labels, values } = processCSVData(csvData);

        const observer = new ResizeObserver(() => {
            const width = container.clientWidth;
            const height = container.clientHeight;
            renderChart(svg, values, labels, width, height);
        });
        observer.observe(container);

        const initialWidth = container.clientWidth;
        const initialHeight = container.clientHeight;
        renderChart(svg, values, labels, initialWidth, initialHeight);
    });
}

document.querySelectorAll('svg [class]').forEach(county => {
    county.addEventListener('mousedown', (event) => {
        if (event.button === 0) { // Left click
            allCounties.forEach(element => {
                element.style.fill = 'white';
              });

            selectedCounty = county;
            county.style.fill = 'lightblue'; 

            const countyName = county.getAttribute('class'); 
            const fileName = `../BackEnd/Data/CountyData/${countyName}.csv`;

            fetchCSVData(fileName, function(csvData) {
                const { labels, values } = processCSVData(csvData);
                const container = document.querySelector('.chartGrid');
                const svg = document.getElementById('lineChart');

                const observer = new ResizeObserver(() => {
                    const width = container.clientWidth;
                    const height = container.clientHeight;
                    renderChart(svg, values, labels, width, height);
                });
                observer.observe(container);

                const initialWidth = container.clientWidth;
                const initialHeight = container.clientHeight;
                renderChart(svg, values, labels, initialWidth, initialHeight);
            });
        }
    });
});

initializeDefaultCounty();
