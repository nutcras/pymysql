from flask import Flask, jsonify
import pymysql
import time

app = Flask(__name__)

# ข้อมูลการเชื่อมต่อฐานข้อมูล
db_config = {
    'host': 'mysql',  # ใช้ชื่อบริการใน docker-compose หรือ IP ของเซิร์ฟเวอร์
    'port': 3306,
    'user': 'root',
    'password': '1234',
    'database': 'transfer'
}

# รอให้ MySQL พร้อม
def wait_for_db():
    while True:
        try:
            connection = pymysql.connect(**db_config)
            connection.close()  # ปิดการเชื่อมต่อ
            break  # ออกจากลูปเมื่อเชื่อมต่อสำเร็จ
        except pymysql.MySQLError as e:
            print(f"เกิดข้อผิดพลาดในการเชื่อมต่อฐานข้อมูล: {e}")
            time.sleep(5)  # รอ 5 วินาทีก่อนพยายามเชื่อมต่ออีกครั้ง

# ฟังก์ชันที่จะถูกเรียกเมื่อเข้าถึง API
@app.route('/', methods=['GET'])
def get_transfer_data():
    try:
        # ส่งข้อความแจ้งเตือนว่าการเชื่อมต่อสำเร็จ
        return jsonify({"message": "เชื่อมต่อฐานข้อมูลสำเร็จ!"}), 200
    except pymysql.MySQLError as e:
        return jsonify({"error": str(e)}), 500

# ฟังก์ชันที่จะถูกเรียกเมื่อเข้าถึง
@app.route('/qa-exam/transfer', methods=['GET'])
def getQaExam():
    try:
        # ส่งข้อความแจ้งเตือนว่าการเชื่อมต่อสำเร็จ
        return jsonify({"message": "เชื่อมต่อ API! qa-exam/transfer"}), 200
    except pymysql.MySQLError as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    wait_for_db()  # รอให้ MySQL พร้อม
    app.run(host='0.0.0.0', port=8080)  # รันแอปพลิเคชัน Flask
