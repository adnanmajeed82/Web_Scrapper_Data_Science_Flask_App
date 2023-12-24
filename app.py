from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)


# Function to perform web scraping
def scrape_website(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract information based on the specific HTML structure of the website
            # Replace the following lines with your scraping logic
            title = soup.title.text
            paragraphs = soup.find_all('p')
            content = '\n'.join([p.text for p in paragraphs])

            return {'title': title, 'content': content}
        else:
            return {'error': f'Error: {response.status_code}'}
    except Exception as e:
        return {'error': str(e)}


# Define a route for the home page
@app.route('/')
def index():
    return render_template('index.html')


# Define a route to handle form submission
@app.route('/scrape', methods=['POST'])
def scrape():
    if request.method == 'POST':
        url = request.form['url']
        result = scrape_website(url)
        return render_template('result.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
