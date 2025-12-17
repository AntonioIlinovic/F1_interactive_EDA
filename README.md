# F1 Interactive EDA

Welcome to the F1 Interactive EDA, a dynamic data exploration platform for Formula 1 datasets. This tool is designed to provide an immersive and engaging way to analyze and visualize data from the world of Formula 1 racing.


## Accessing the Application

The application is available online and can be accessed via this link: [F1 Interactive EDA](https://f1-interactive-eda.onrender.com/).

Please note that the application is hosted on a free version of Render, which may result in longer loading times initially.


### Example Video and Screenshots

For a quick overview and demonstration of the F1 Interactive EDA, you can watch the [example video](./F1_Interactive_EDA_video.mp4). The video showcases the functionalities and features of the application, providing a glimpse into its capabilities. Here are also some example screenshots:

<img width="1914" height="952" alt="image" src="https://github.com/user-attachments/assets/718fec98-96eb-4a69-93f4-0378fdd9bcd4" />
<img width="1914" height="952" alt="image" src="https://github.com/user-attachments/assets/91cddfc3-fa75-4307-bbb2-f6118348b621" />
<img width="1914" height="952" alt="image" src="https://github.com/user-attachments/assets/fa8e01ed-07d8-497a-8c84-db4557f851a6" />
<img width="1914" height="952" alt="image" src="https://github.com/user-attachments/assets/d6721621-cc99-42d3-90dc-397dddd74589" />
<img width="1914" height="952" alt="image" src="https://github.com/user-attachments/assets/99fa012d-e878-45bc-861d-abdb9a221760" />
<img width="1914" height="952" alt="image" src="https://github.com/user-attachments/assets/441743ff-c7b8-4842-99ed-a4ff8e7f704e" />


## Purpose of the Application

The F1 Interactive EDA is not just about presenting predefined analyses; it's a platform for discovery and exploration. Users are encouraged to delve into the dataset through various visualizations, uncovering insights and patterns on their own. As such, the visualizations are designed to be as general as possible. This approach allows for the exploration of data across different seasons and contexts, acknowledging that some data may not be available for certain seasons or may not display as expected. This aspect is an intentional part of the exploratory journey.


## Dataset Source

The dataset powering this application is sourced from Kaggle and encompasses the Formula 1 World Championship data from 1950 to 2020. You can view the dataset here: [Kaggle Dataset](https://www.kaggle.com/datasets/rohanrao/formula-1-world-championship-1950-2020).

Please note that this dataset may not include the latest race information and might not be current with the most recent Formula 1 events.


## Application Structure

The application's code structure is based on a template provided by `helpedbyanerd`. The template is a multi-page app setup using the Plotly Dash package. For more details on the usage of this template, refer to this [blog post](https://medium.com/@helpedbyanerd/how-to-create-a-multipage-plotly-dash-application-in-2023-boilerplate-552c1fc7a00).

The template repository can be found here: [GitHub Repository](https://github.com/helpedbyanerd/plotly-dash-multipage-app-template).

## Running Locally

To run the application locally, follow these steps:

1. Clone the repository to your local machine.
2. Navigate to the project's root folder.
3. Install the necessary packages using the command:
  ```
  pip install -r requirements.txt
  ```
4. Run the Dash application using the command:
  ```
  python app.py
  ```
5. Access the Dash application at:
  ```
  http://127.0.0.1:8050/
  ```
