const searchInput = document.getElementById('dropdownSearch');
        const dropdownMenu = document.getElementById('dropdownMenu');

        // Show menu on focus
        searchInput.addEventListener('focus', () => {
            dropdownMenu.style.display = 'block';
        });

        // Hide menu on click outside
        document.addEventListener('click', (e) => {
            if (!e.target.closest('.dropdown')) {
                dropdownMenu.style.display = 'none';
            }
        });

        // Filter menu items
        searchInput.addEventListener('input', () => {
            const filter = searchInput.value.toLowerCase();
            const items = dropdownMenu.getElementsByClassName('dropdown-item');
            Array.from(items).forEach((item) => {
                const text = item.textContent.toLowerCase();
                item.style.display = text.includes(filter) ? 'block' : 'none';
            });
        });

        dropdownMenu.addEventListener('click', (e) => {
            if (e.target.classList.contains('dropdown-item')) {

                
                const regionName = e.target.dataset.region; // Ensure each dropdown-item has a data-region attribute
                changeCountyColor(regionName);

                const fileName = `../BackEnd/Data/HealthData/${regionName}.csv`;
        
                console.log('Selected region:', regionName);
                console.log('File name updated to:', fileName);
        
                // Fetch and process the data for the selected county
                fetchCountyCSVData(fileName, function(csvData) {
                    const { years, values } = processCountyHealthData(csvData);
        
                    // Render the line chart for the selected county
                    const container = document.querySelector('.statGrid');
                    const svg = document.getElementById('healthChart');
                    
                    // Dynamically resize and re-render the chart
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
        
                    // Call additional rendering functions as needed
                });
                   
                const CountyName = `../BackEnd/Data/CountyData/${regionName}.csv`;
        
                console.log('Selected region:', regionName);
                console.log('File name updated to:', CountyName);
        
                // Fetch and process the data for the selected county
                fetchCSVData(CountyName, function(csvData) {
                    const { labels, values } = processCSVData(csvData);
                    const container = document.querySelector('.chartGrid');
                    const svg = document.getElementById('lineChart');
    
                    // Resize observer for dynamic resizing
                    const observer = new ResizeObserver(() => {
                        const width = container.clientWidth;
                        const height = container.clientHeight;
                        renderChart(svg, values, labels, width, height);
                    });
                    observer.observe(container);
    
                    // Initial render
                    const initialWidth = container.clientWidth;
                    const initialHeight = container.clientHeight;
                    renderChart(svg, values, labels, initialWidth, initialHeight);
                });

                dropdownMenu.style.display = 'none'; // Close the dropdown

            }
            function changeCountyColor(countyClass) {


                allCounties.forEach(element => {
                    element.style.fill = 'white';
                  });


                const newColor = 'lightblue';  // Set a default color, e.g., red
                
                // Get all elements with the class matching the county name
                const countyElement = document.querySelectorAll(`.${countyClass}`);
                
                // Loop through each matching element and change its color
                countyElement.forEach(element => {
                    element.style.fill = newColor;  // Change the 'fill' color of the element
                });
            }
        });
