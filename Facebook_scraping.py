from flask import Flask, render_template
import psycopg2

app = Flask(__name__)
try:
    conn = psycopg2.connect(
        dbname="scrapingDB",
        user="postgres",
        password="password",
        host="localhost",  # Change this if using a remote server
        port="5432"  # Default PostgreSQL port
    )
    cur = conn.cursor()
    print("Connected to PostgreSQL successfully!")
except psycopg2.Error as e:
    print("Error connecting to PostgreSQL:", e)



@app.route('/')
def index():
    cur.execute("SELECT * FROM fb_scraping")
    data = cur.fetchall()
    print(data)
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)