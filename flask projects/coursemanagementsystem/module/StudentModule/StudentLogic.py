import psycopg2
from flask import app, redirect, render_template, url_for, request


@app.route('/view_students')
def view_students():
    conn = psycopg2.connect(
        database="CMS", user='postgres',
        password='admin',
        host='127.0.0.1', port='5432'
    )
    cursor = conn.cursor()
    # Fetch all student records
    cursor.execute('''
        SELECT * FROM StudentDetails
    ''')
    students = cursor.fetchall()

    conn.close()

    return render_template('Faculty/view_students.html', students=students)

@app.route('/crud')
def crud_display():
    return render_template('Faculty/crud.html')


def get_student_by_id(student_id):
    conn = psycopg2.connect(
        database="CMS", user='postgres',
        password='admin',
        host='127.0.0.1', port='5432'
    )
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM StudentDetails WHERE student_id = %s', (student_id,))
    student = cursor.fetchone()
    conn.close()
    return student

@app.route('/update')
def student_update():
    return render_template('Faculty/update_student.html')

@app.route('/update_student/<int:student_id>', methods=['GET', 'POST'])
def update_student(student_id):
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        phone_number = request.form['phone_number']
        aadhar_number = request.form['aadhar_number']
        email_id = request.form['email_id']

        conn = psycopg2.connect(
            database="CMS", user='postgres',
            password='admin',
            host='127.0.0.1', port='5432'
        )
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE StudentDetails 
            SET name = %s, age = %s, phone_number = %s, aadhar_number = %s, email_id = %s
            WHERE student_id = %s
        ''', (name, age, phone_number, aadhar_number, email_id, student_id))
        conn.commit()
        conn.close()

        return redirect(url_for('home'))

    student = get_student_by_id(student_id)
    if student:
        return render_template('Faculty/view_students.html', student=student)
    else:
        return 'Student not found'


@app.route('/delete_student/<int:student_id>', methods=['POST'])
def delete_student(student_id):
    # student_id = request.form['student_id']
    # Delete student record from the database
    conn = psycopg2.connect(
        database="CMS", user='postgres',
        password='admin',
        host='127.0.0.1', port='5432'
    )
    cursor = conn.cursor()
    cursor.execute('DELETE FROM studentdetails WHERE student_id = %s', (student_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('view_students'))


if __name__ == '__main__':
    app.run(debug=True)
