from flask import *
import csv
app=Flask(__name__)
def read_csv(file_path):
    data=[]
    with open(file_path,'r') as file:
        csv_reader=csv.DictReader(file)
        for row in csv_reader:
            data.append(row)
    return data
def write_csv(file_path, data):
    with open(file_path,'w',newline='') as file:
        fieldnames = ['EMPID','Name','DOB','Department','Designation','no of years of Experience','no of leaves','Salary']
        writer = csv.DictWriter(file,fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

@app.route('/')
def index():
    data=read_csv('Employee.csv')
    return render_template('index.html',data=data)

@app.route('/add',methods=['post'])
def add():
    empid = request.form['empid']
    name= request.form['name']
    dob= request.form['dob']
    department= request.form['department']
    designation=request.form['designation']
    experience = request.form['experience']
    leaves_applied = request.form['leaves_applied']
    salary=request.form['salary']

    new_data ={
        'EMPID':empid,
        'Name':name,
        'DOB':dob,
        'Department':department,
        'Designation':designation,
        'no of years of Experience':experience,
        'no of leaves':leaves_applied,
        'Salary':salary
    }
    current_data = read_csv('Employee.csv')
    current_data.append(new_data)
    write_csv('Employee.csv',current_data)
    return redirect(url_for('index'))
@app.route('/delete/<empid>', methods=['POST'])
def delete(empid):
    current_data = read_csv('Employee.csv')
    updated_data = [row for row in current_data if row['EMPID'] != empid]

    write_csv('Employee.csv', updated_data)
    return redirect(url_for('index'))
if __name__ =="__main__":
    app.run(debug=True)




