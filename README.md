## Flask Application Design for Temple Discovery App

### HTML Files

**temples.html**: This file will display a list of all temples. It will include a table with the following columns:
- Temple Name
- Location
- Deities Worshipped

**temple.html**: This file will display detailed information about a specific temple. It will include:
- Temple name
- Location
- Deities worshipped
- History
- Architecture
- Current status
- Images of the temple

### Routes

**@app.route('/temples')**: This route will render the temples.html file, displaying the list of all temples.

**@app.route('/temple/<temple_name>')**: This route will render the temple.html file, displaying detailed information about the specified temple.

**@app.route('/add_temple', methods=['GET', 'POST'])**: This route will handle the addition of a new temple to the database. The GET request will render a form to add a new temple, and the POST request will process the form and add the temple to the database, redirecting to the temples.html page.

**@app.route('/edit_temple/<temple_name>', methods=['GET', 'POST'])**: This route will handle the editing of an existing temple. The GET request will render a form to edit the temple, and the POST request will process the form and update the temple in the database, redirecting to the temple.html page of the updated temple.

**@app.route('/delete_temple/<temple_name>')**: This route will handle the deletion of a temple from the database. It will redirect to the temples.html page after deleting the temple.

### Database

The application will use a database to store information about temples. The database will have a table named 'temples' with the following columns:
- Temple ID (primary key)
- Temple Name (unique)
- Location
- Deities Worshipped
- History
- Architecture
- Current Status (e.g., active, inactive, under renovation)
- Image URL