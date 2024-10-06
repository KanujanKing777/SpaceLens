document.addEventListener('DOMContentLoaded', () => {
    // Select DOM elements
    const datasetSelect = document.getElementById('dataset-select');
    const visualizationType = document.getElementById('visualization-type');
    const metricsCheckboxes = document.querySelectorAll('input[name="metrics"]');
    const startDate = document.getElementById('start-date');
    const endDate = document.getElementById('end-date');
    const graphContainer = document.getElementById('graph-container');
    const zoomInBtn = document.getElementById('zoom-in');
    const zoomOutBtn = document.getElementById('zoom-out');
    const resetFiltersBtn = document.getElementById('reset-filters');
    const viewSimilarBtn = document.getElementById('view-similar-experiments');
  
    // Load JSON data
    let jsonData = {};
  
    async function loadDataset(dataset) {
      const filePath = `Structured Data/${dataset}.json`;
      const response = await fetch(filePath);
      jsonData[dataset] = await response.json();
      displayOverview(jsonData[dataset]);
    }
  
    function displayOverview(data) {
      graphContainer.innerHTML = `<p>Dataset Overview: ${data.summary}</p>`;
      // Additional code to generate graphs based on the data
    }
  
    // Event listeners for user interaction
    datasetSelect.addEventListener('change', () => {
      const selectedDataset = datasetSelect.value;
      if (selectedDataset === 'OSD-379' || selectedDataset === 'OSD-665') {
        loadDataset(selectedDataset);
      } else {
        graphContainer.innerHTML = `<p>Searching other datasets...</p>`;
      }
    });
  
    visualizationType.addEventListener('change', () => {
      // Update graph visualization based on the type
      const selectedType = visualizationType.value;
      updateGraphType(selectedType);
    });
  
    function updateGraphType(type) {
      switch(type) {
        case 'timeline':
          displayTimeline();
          break;
        case 'comparison':
          displayComparison();
          break;
        case 'subject':
          displaySubjectData();
          break;
      }
    }
  
    function displayTimeline() {
      graphContainer.innerHTML = `<p>Displaying Timeline View...</p>`;
      // Code to display timeline data
    }
  
    function displayComparison() {
      graphContainer.innerHTML = `<p>Displaying Comparison View...</p>`;
      // Code to display comparison view
    }
  
    function displaySubjectData() {
      graphContainer.innerHTML = `<p>Displaying Subject Data View...</p>`;
      // Code to display subject data
    }
  
    // Filter data by selected metrics
    metricsCheckboxes.forEach(checkbox => {
      checkbox.addEventListener('change', () => {
        const selectedMetrics = Array.from(metricsCheckboxes)
                                     .filter(cb => cb.checked)
                                     .map(cb => cb.value);
        updateMetrics(selectedMetrics);
      });
    });
  
    function updateMetrics(metrics) {
      graphContainer.innerHTML = `<p>Selected Metrics: ${metrics.join(', ')}</p>`;
      // Code to update graph based on selected metrics
    }
  
    // Filter data by time frame
    startDate.addEventListener('change', updateTimeFrame);
    endDate.addEventListener('change', updateTimeFrame);
  
    function updateTimeFrame() {
      const start = startDate.value;
      const end = endDate.value;
      graphContainer.innerHTML = `<p>Time Frame: ${start} to ${end}</p>`;
      // Code to filter data based on selected time frame
    }
  
    // Zoom and reset controls
    zoomInBtn.addEventListener('click', () => {
      graphContainer.innerHTML = `<p>Zooming In...</p>`;
      // Code to zoom in
    });
  
    zoomOutBtn.addEventListener('click', () => {
      graphContainer.innerHTML = `<p>Zooming Out...</p>`;
      // Code to zoom out
    });
  
    resetFiltersBtn.addEventListener('click', () => {
      graphContainer.innerHTML = `<p>Resetting Filters...</p>`;
      // Code to reset filters
    });
  
    // View similar experiments
    viewSimilarBtn.addEventListener('click', () => {
      graphContainer.innerHTML = `<p>Displaying similar experiments...</p>`;
      // Code to fetch and display similar experiments
    });
  });
  