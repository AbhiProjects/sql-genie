from flask import Flask, request, jsonify

from utils import generate_llm_response

app = Flask(__name__)

@app.route('/ask', methods=['POST'])
def ask_sql_genie():
    """
    API endpoint that accepts a POST request with a JSON payload containing a query.
    The function processes the query using an LLM (via generate_llm_response) 
    and returns the result in a JSON response.
    """
    try:
        if request.is_json:
            data = request.get_json() 
            query = data.get('query')

            llm_response_text = generate_llm_response(query)
            llm_response = {
                'data': llm_response_text
            }
            return jsonify(llm_response)
        else:
            llm_response = {
                'error': 'Invalid input, expected JSON'
            }
            return jsonify(llm_response), 400
    except Exception as e:
        llm_response = {
            'data': ''
        }
        print(str(e))
        return jsonify(llm_response), 400
    
@app.errorhandler(404)
def not_found(e):
    """
    Handles HTTP 404 Not Found errors.
    Returns a JSON response indicating that the requested resource was not found.
    """
    return jsonify(error="Resource Not Found"), 404

@app.errorhandler(405)
def method_not_allowed(e):
    """
    Handles HTTP 405 Method Not Allowed errors.
    Returns a JSON response indicating that the method is not allowed.
    """
    return jsonify(error="Method Not Allowed"), 405

@app.errorhandler(500)
def internal_server_error(e):
    """
    Handles HTTP 500 Internal Server Error.
    Returns a JSON response indicating that there was a server error.
    """
    return jsonify(error="Internal Server Error"), 500


if __name__ == '__main__':
    app.run(debug=False)
