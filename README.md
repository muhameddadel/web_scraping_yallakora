<h1>YallaKora Web Scraping Project</h1>

<h2>Project Overview</h2>

<p>The YallaKora Web Scraping project aims to gather match details from the YallaKora website and save them in a CSV file. The project utilizes the BeautifulSoup library to parse the HTML content of the website and extract relevant information such as match results, teams, and match times.</p>

<h2>Getting Started</h2>

<ol>
  <li>Make sure you have Python installed on your machine.</li>
  <li>Clone this repository to your local machine:</li>
</ol>

<ol start="3">
  <li>Install the required dependencies using pip:</li>
</ol>

<pre><code>pip install beautifulsoup4 requests</code></pre>

<h2>Usage</h2>

<ol>
  <li>Run the <code>main.py</code> script:</li>
</ol>

<pre><code>python main.py</code></pre>

<ol start="2">
  <li>You will be prompted to enter a date in the format MM/DD/YYYY. The script will fetch match details for the specified date from the YallaKora website.</li>
  <li>The script will create a CSV file named <code>matches_details.csv</code> in the project directory. The CSV file will contain columns for championship title, team names, match time, and match result.</li>
</ol>

<h2>Dependencies</h2>

<ul>
  <li>BeautifulSoup: A library for parsing HTML and XML documents.</li>
  <li>requests: A library for making HTTP requests to web pages.</li>
  <li>csv: A library for reading and writing CSV files.</li>
</ul>

<h2>Examples</h2>

<img src="images/y1.PNG" alt="Image 1">
<img src="images/y2.PNG" alt="Image 2">