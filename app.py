return """
<!DOCTYPE html>
<html>
<head>
<title>SMP Employee Tracker</title>

<style>

*{
margin:0;
padding:0;
box-sizing:border-box;
font-family:'Segoe UI',sans-serif;
}

body{
background:#eef3ff;
}

.header{
height:90px;
background:linear-gradient(90deg,#003b95,#0066ff,#7b2cff);
color:white;
display:flex;
justify-content:space-between;
align-items:center;
padding:0 40px;
}

.logo{
font-size:32px;
font-weight:bold;
}

.version{
background:#7a3cff;
padding:10px 20px;
border-radius:20px;
}

.container{
display:flex;
}

.sidebar{
width:250px;
height:calc(100vh - 90px);
background:#071c61;
color:white;
padding-top:30px;
}

.sidebar ul{
list-style:none;
}

.sidebar li{
padding:20px;
margin:10px;
border-radius:10px;
cursor:pointer;
}

.sidebar li:hover{
background:#0066ff;
}

.main{
flex:1;
padding:30px;
}

.card{
background:white;
padding:25px;
border-radius:20px;
box-shadow:0 4px 15px rgba(0,0,0,.08);
margin-bottom:20px;
}

.cards{
display:grid;
grid-template-columns:repeat(4,1fr);
gap:20px;
margin-bottom:25px;
}

.stat{
background:white;
padding:25px;
border-radius:15px;
text-align:center;
box-shadow:0 4px 15px rgba(0,0,0,.08);
}

.stat h2{
color:#005bea;
}

.form-grid{
display:grid;
grid-template-columns:1fr 1fr;
gap:20px;
}

input{
width:100%;
padding:12px;
border:1px solid #ccc;
border-radius:10px;
}

button{
width:100%;
padding:15px;
background:linear-gradient(90deg,#0099ff,#7a3cff);
border:none;
color:white;
font-size:18px;
border-radius:12px;
cursor:pointer;
}

table{
width:100%;
border-collapse:collapse;
margin-top:20px;
}

table th{
background:#005bea;
color:white;
padding:12px;
}

table td{
padding:12px;
border:1px solid #ddd;
text-align:center;
}

</style>
</head>

<body>

<div class="header">
<div class="logo">🚀 SMP Employee Tracker</div>
<div class="version">Version 2.0</div>
</div>

<div class="container">

<div class="sidebar">
<ul>
<li>🏠 Dashboard</li>
<li>👨 Employee List</li>
<li>📊 Reports</li>
<li>📈 Analytics</li>
<li>⚙ Settings</li>
<li>🚪 Logout</li>
</ul>
</div>

<div class="main">

<div class="cards">

<div class="stat">
<h2>5</h2>
<p>Total Employees</p>
</div>

<div class="stat">
<h2>4</h2>
<p>Departments</p>
</div>

<div class="stat">
<h2>2</h2>
<p>Projects</p>
</div>

<div class="stat">
<h2>100%</h2>
<p>Active</p>
</div>

</div>

<div class="card">

<h1>Employee Tracker Dashboard</h1>
<br>

<div class="form-grid">

<div>
<label>Employee Name</label><br><br>
<input type="text" placeholder="Enter Employee Name">
</div>

<div>
<label>Department</label><br><br>
<input type="text" placeholder="Enter Department">
</div>

</div>

<br>

<button>Track Employee</button>

<table>

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

</div>

</div>

</div>

</body>
</html>
"""
