from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <body style="font-family:Arial;text-align:center">

    <h1>Employee Tracker</h1>
    <h3>Version 1.0</h3>

    <table border="1" cellpadding="10" align="center">
        <tr>
            <th>Employee ID</th>
            <th>Name</th>
            <th>Department</th>
        </tr>

        <tr>
            <td>EMP001</td>
            <td>Sampath</td>
            <td>DevOps</td>
        </tr>

        <tr>
            <td>EMP002</td>
            <td>Ram</td>
            <td>Windows Admin</td>
        </tr>

        <tr>
            <td>EMP003</td>
            <td>Jay</td>
            <td>Cloud Engineer</td>
        </tr>

        <tr>
            <td>EMP004</td>
            <td>Ayyapa</td>
            <td>DevOps Engineer</td>
        </tr>

        <tr>
            <td>EMP005</td>
            <td>Siva</td>
            <td>Linux Administrator</td>
        </tr>

    </table>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
