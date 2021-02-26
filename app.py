from flask import Flask, render_template, request, redirect,url_for
import psycopg2
app = Flask(__name__)


@app.route('/',methods=['POST','GET'])
def search():

    return render_template('search.html')

@app.route('/nguirubi_thigio', methods=['POST','GET'])
def nguirubi_thigio():
    #parcel_id = input("Please enter parcel number")
    if request.method == 'POST':
        parcel_id = request.form['parcel_id']
    else:
        return "The parcel number does not exist "

    conn = psycopg2.connect(database="ndeiya_plots", user="postgres", password="1234", host="127.0.0.1", port="5432")

    cur = conn.cursor()

    if parcel_id[0] == '\'':
        pass
    else:
        parcel_id = "'" + parcel_id + "'"


    cur.execute("""SELECT * FROM nguirubi_thigio WHERE parcel_number = {}""".format(parcel_id))
    query_results = cur.fetchall()
    #print(query_results)

    #cur.execute("SELECT b.block_name, s.sheet_id sheet_id, p.parcel_id parcel_id, p.size size, p.owner_id owner_id, o.owner_name owner_name, o.owner_phone owner_phone FROM blocks b INNER JOIN sheet_number s ON b.block_id = s.block_id INNER JOIN parcels p ON s.sheet_id = p.sheet_id INNER JOIN owner o ON p.parcel_id = o.parcel_id ORDER BY parcel_id")

    #records = cur.fetchall()
   # print(records)

    conn.close()



    return render_template('index.html',parcel_id=parcel_id,query_results=query_results)

@app.route('/nachu_ndacha', methods=['POST','GET'])
def nachu_ndacha():
    #parcel_id = input("Please enter parcel number")
    if request.method == 'POST':
        parcel_id = request.form['parcel_id']
    else:
        return "The parcel number does not exist "

    conn = psycopg2.connect(database="ndeiya_plots", user="postgres", password="1234", host="127.0.0.1", port="5432")

    cur = conn.cursor()

    if parcel_id[0] == '\'':
        pass
    else:
        parcel_id = "'" + parcel_id + "'"


    cur.execute("""SELECT * FROM nachu_ndacha WHERE parcel_number= {}""".format(parcel_id))
    query_results = cur.fetchall()

    conn.close()

    return render_template('index.html',parcel_id=parcel_id,query_results=query_results)

@app.route('/nachu_mikuyuini', methods=['POST','GET'])
def nachu_mikuyuini():
    #parcel_id = input("Please enter parcel number")
    if request.method == 'POST':
        parcel_id = request.form['parcel_id']
    else:
        return "The parcel number does not exist "

    conn = psycopg2.connect(database="ndeiya_plots", user="postgres", password="1234", host="127.0.0.1", port="5432")

    cur = conn.cursor()

    if parcel_id[0] == '\'':
        pass
    else:
        parcel_id = "'" + parcel_id + "'"


    cur.execute("""SELECT * FROM nachu_mikuyuini WHERE parcel_number = {}""".format(parcel_id))
    query_results = cur.fetchall()

    conn.close()

    return render_template('index.html',parcel_id=parcel_id,query_results=query_results)

@app.route('/nguirubi_ndiuni', methods=['POST','GET'])
def nguirubi_ndiuni():
    #parcel_id = input("Please enter parcel number")
    if request.method == 'POST':
        parcel_id = request.form['parcel_id']
    else:
        return "The parcel number does not exist "

    conn = psycopg2.connect(database="ndeiya_plots", user="postgres", password="1234", host="127.0.0.1", port="5432")

    cur = conn.cursor()

    if parcel_id[0] == '\'':
        pass
    else:
        parcel_id = "'" + parcel_id + "'"


    cur.execute("""SELECT * FROM nguirubi_ndiuni WHERE parcel_number = {}""".format(parcel_id))
    query_results = cur.fetchall()

    conn.close()

    return render_template('index.html',parcel_id=parcel_id,query_results=query_results)



if __name__ == '__main__':
    app.run()
