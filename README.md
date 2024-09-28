## Home Page Layout

### Buttons/Components on Home Page:

1. **Select Dataset (Dropdown or Buttons)**
   - Options:
     - **OSD-379 (Rodent Research Reference Mission-1)**
     - **OSD-665 (Rodent Research-23)**
     - **Search Other Datasets (NASA OSDR)**

2. **Visualization Type (Dropdown or Buttons)**
   - Options:
     - **Timeline View**  
       Displays a timeline of events like launch, in-flight phase, post-flight data collection.
     - **Comparison View**  
       Displays side-by-side comparisons between groups, e.g., control vs. treatment, or pre-flight vs. post-flight.
     - **Subject Data View**  
       Displays individual subject data like physiological or genetic changes.

3. **Metrics to Display (Checkboxes or Dropdown)**
   - Options:
     - **Physiological Data** (Weight, activity levels, etc.)
     - **Genetic Expression** (If available)
     - **Behavioral Data**
     - **Treatment Effects**
     - **Statistical Insights** (Summary metrics, significant results)

4. **Filter by Time Frame (Slider or Date Range Input)**
   - Choose specific time intervals (e.g., only in-flight data, post-flight data, or full mission timeline).

5. **Interactive Graph Controls (Buttons)**
   - **Zoom In/Out** (For timeline and graphs)
   - **Switch View (Gene Expression vs. Behavioral Data)**
   - **Reset Filters** (Returns to default settings)

6. **View Similar Experiments (Button)**
   - Clicking this will show a list of other relevant experiments from NASA’s OSDR with similar parameters (e.g., tissue samples, treatment methods, or subjects).

### What Happens When Buttons are Clicked:

1. **Dataset Selection (OSD-379 or OSD-665):**
   - On selection, the main panel displays an overview of the dataset:
     - **Number of subjects**
     - **Treatment applied**
     - **Key experiment stages**
     - **Summary statistics**
   - Buttons to view **detailed graphs** or **experiment metadata** will become active.

2. **Visualization Type:**
   - **Timeline View**:  
     Shows a horizontal timeline displaying key experimental stages (launch, in-flight phase, return). Clicking on each stage will bring up data specific to that period (e.g., genetic or physiological data).
   - **Comparison View**:  
     Displays two side-by-side graphs (e.g., control vs. experimental group) to compare the effects of different conditions.
   - **Subject Data View**:  
     Shows detailed data for individual subjects, which could be viewed in a table or graph format.

3. **Metrics to Display:**
   - When checkboxes are selected (e.g., physiological data, gene expression), the visualizations update to reflect those metrics, either as line graphs, bar charts, or pie charts.
   - When **statistical insights** is selected, the tool shows a summary of significant results, such as changes in activity levels or significant gene expression alterations.

4. **Time Frame Filter:**
   - Adjusting the time frame dynamically updates the graph or timeline to focus on the selected time period (e.g., zooming into the in-flight phase of the experiment).

5. **Zoom In/Out & Reset Filters:**
   - **Zoom In/Out** allows the user to focus on specific time intervals or data points in greater detail.
   - **Reset Filters** reverts the view back to the original dataset and timeline overview.

6. **View Similar Experiments:**
   - Clicking this button opens a list or gallery of other space-based biological experiments within NASA OSDR. Users can compare datasets, treatments, or other experimental factors.

### Additional Interactive Features:
- **Hover over data points**: Displays detailed information about that data point (e.g., time, treatment, subject ID, and value).
- **Download Data/Graph (Button)**: Allows users to export the displayed data or graph as CSV, JSON, or PNG.

