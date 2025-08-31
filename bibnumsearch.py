from flask import Flask, request, render_template, jsonify, Response
from weasyprint import HTML
import bible  # assuming my_script.py is the name of your Python script

app = Flask(__name__)

#app.config['APPLICATION_ROOT'] = '/app'

@app.route('/submit', methods=['POST'])
def submit():
        my_number = request.form['my_number']
        result = bible.scriptures(my_number)
        return jsonify(result)

@app.route('/bible')
def bible_route():
        return render_template('index.html')

@app.route('/')
def root_route():
    return render_template('index.html')

@app.route('/download')
def download_pdf():
    # 1. Get the search number from the URL (e.g., ?number=911)
    search_number = request.args.get('number', '')
    if not search_number:
        # Handle cases where no number is provided
        return "Error: No search number provided.", 400

    # 2. Get the Bible verse results again using your existing logic
    results = bible.scriptures(search_number)

    # 3. Render the dedicated PDF template into an HTML string
    #    We pass the results and the search term to the template
    html_for_pdf = render_template('report_template.html', results=results, search_term=search_number)

    # 4. Use WeasyPrint to convert the HTML string into a PDF in memory
    pdf_bytes = HTML(string=html_for_pdf).write_pdf()

    # 5. Create a Flask Response to send the PDF back to the user
    return Response(
        pdf_bytes,
        mimetype='application/pdf',
        headers={'Content-Disposition': f'attachment;filename=results-{search_number}.pdf'}
    )


if __name__ == '__main__':
        app.run(host='0.0.0.0', debug=True)
