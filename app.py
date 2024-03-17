import os
from flask import Flask, send_from_directory, request, jsonify

# Set up the configuration directory for LANCEdb before importing your modules that might use it
os.environ['LANCEDB_CONFIG_DIR'] = os.path.join(os.getcwd(), 'lancedb_config')
if not os.path.exists(os.environ['LANCEDB_CONFIG_DIR']):
    os.makedirs(os.environ['LANCEDB_CONFIG_DIR'])

# Import your FinancialCrew classes from their respective modules
# It's important that this comes after the environment variable is set, 
# in case these modules make use of the LANCEdb configuration
from main import FinancialCrew as FinancialCrew1
from main2 import FinancialCrew as FinancialCrew2
from main3 import FinancialCrew as FinancialCrew3
from main4 import FinancialCrew as FinancialCrew4
from main5 import FinancialCrew as FinancialCrew5

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        data = request.get_json()
        company = data['company']
        bot_type = data['type']

        # Determine which FinancialCrew class to use based on the bot_type
        crew_class = {
            'financial': FinancialCrew1,
            'general': FinancialCrew2,
            'news': FinancialCrew3,
            'strategic': FinancialCrew4,
            'retail': FinancialCrew5
        }.get(bot_type, None)

        # Check if the bot_type is valid
        if not crew_class:
            return jsonify({'error': 'Invalid analysis type selected'}), 400

        # Instantiate the selected FinancialCrew class
        crew_instance = crew_class(company)
        # Assume the run() method processes and returns the analysis result
        result = crew_instance.run()

        # Check if the result is what you expect it to be
        if not result:
            raise ValueError("Result of analysis is empty.")

        return jsonify({'result': result})

    except KeyError as e:
        # If the key 'company' or 'type' does not exist in the JSON payload
        return jsonify({'error': f'Missing key in JSON payload: {e}'}), 400
    except ValueError as e:
        # If there's an issue with the returned result
        return jsonify({'error': str(e)}), 500
    except Exception as e:
        # For any other exceptions
        return jsonify({'error': f'An unexpected error occurred: {e}'}), 500

# Use the PORT environment variable if it's set, otherwise default to 5000
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
