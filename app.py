from flask import Flask, jsonify, render_template
import matplotlib.pyplot as plt
from io import BytesIO
import base64

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/hello')
def hello():
    # Your API logic here
    return jsonify({'message': 'Hello from API!'})

@app.route('/api/generate_chart')
def generate_chart():
    # Sample data
    categories = ['Category A', 'Category B', 'Category C']
    values = [20, 35, 25]

    # Create a bar chart
    plt.bar(categories, values)

    # Save the plot to a BytesIO object
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close()

    # Convert the BytesIO object to base64 for embedding in HTML
    chart_data = base64.b64encode(buffer.read()).decode('utf-8')

    return jsonify({'chart_data': chart_data})

if __name__ == '__main__':
    app.run(debug=True)
