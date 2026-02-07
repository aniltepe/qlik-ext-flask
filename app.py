from flask import Flask, request, make_response, jsonify
from flask_cors import CORS
import services.ops as ops
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, static_folder='./build', static_url_path='/')
cors = CORS(app)
QLIK_WS_CERT_PATH = os.getenv("QLIK_WS_CERT_PATH")

# statik dosyalar yani ön-yüz dosyaları (html, js, css) döndürülür
@app.route('/')
def index():
    return app.send_static_file('index.html')

# ön-yüz hangi modda (add, edit, delete) açılırsa açılsın, bu endpoint'e gelir (meta modları hariç)
# ilgili appid ve dbtable çifti için tanımlanmış field tanımları döndürülür
@app.route("/api/columns")
def get_columns():
    appid = request.args.get("appid")
    dbtable = request.args.get("dbtable")
    fields = ops.get_columns(appid, dbtable)
    return jsonify(fields)

# ön-yüz addmeta modunda açıldığında ve kayıt girilip kaydet butonuna basıldığında bu endpoint'e gelir
# body'de field array'i barındırır, bu field'lar farklı appid ve dbtable çiftine sahip olmayabilir
@app.route('/api/addmetabulk', methods=["POST"])
def add_meta_bulk():
    # print(request.json)
    ops.add_meta_bulk(request.json)
    response = jsonify({'status': 'OK'})
    return response

# metadata kayıtlarının BI developer'lar tarafından düzenlenmesi için planlanmıştır ancak ilerletilmemiştir
# burada yapılması planlanan işlemler çok zaman almadan BI dev tarafından manuel yapılabilir
@app.route('/api/editmetabulk', methods=["POST"])
def edit_meta_bulk():
    # print(request.json)
    ops.edit_meta_bulk(request.json)
    response = jsonify({'status': 'OK'})
    return response

# son-kullanıcı (iş birimi) tarafından girilen satırların geldiği endpoint'tir
# gönderilen kayıtlar ilişkili (QDE_ prefix'li) veri tabanı tablosuna insert edilir
@app.route('/api/addbulk', methods=["POST"])
def add_bulk():
    # print(request.json)
    appid = request.args.get("appid")
    dbtable = request.args.get("dbtable")
    ops.add_bulk(request.json, appid, dbtable)
    response = jsonify({'status': 'OK'})
    return response

# son-kullanıcı (iş birimi) tarafından düzenlenen satırların geldiği endpoint'tir
# gönderilen kayıtlar ilişkili (QDE_ prefix'li) veri tabanı tablosunda update edilir
@app.route('/api/editbulk', methods=["POST"])
def edit_bulk():
    # print(request.json)
    appid = request.args.get("appid")
    dbtable = request.args.get("dbtable")
    ops.edit_bulk(request.json, appid, dbtable)
    response = jsonify({'status': 'OK'})
    return response

# son-kullanıcı (iş birimi) tarafından silinen satırların geldiği endpoint'tir
# gönderilen kayıtlar ilişkili (QDE_ prefix'li) veri tabanı tablosunda delete edilir
@app.route('/api/deletebulk', methods=["POST"])
def delete_bulk():
    # print(request.json)
    appid = request.args.get("appid")
    dbtable = request.args.get("dbtable")
    ops.delete_bulk(request.json, appid, dbtable)
    response = jsonify({'status': 'OK'})
    return response

# ön-yüz delete veya edit modunda açıldığında bu endpoint'e gelir (meta modları hariç)
# QDE_ prefix'li veri tabanı tablosundaki kayıtları döndürür
@app.route('/api/rows', methods=["GET"])
def get_rows():
    dbtable = request.args.get("dbtable")
    rows = ops.get_rows(dbtable)
    response = jsonify(rows)
    return response

# ön-yüz editmeta modunda açıldığında bu endpoint'e gelir
# QlikDataEntryMeta tablosundaki tüm kayıtları döndürür
# editmeta modu aslında field tanım kayıtlarında (metadata), düzenleme yapmak için planlanmıştır
# sonradan ön-yüzde tüm alanlar disabled yapılarak sadece detay görüntülemek için kullanılmaktadır
# qlik'te editmeta modunu açan butonun label'ı "DETAY" olarak değiştirilse de modun adı editmeta kalmıştır
@app.route('/api/rowsmeta', methods=["GET"])
def get_rows_meta():
    rows = ops.get_rows_meta()
    response = jsonify(rows)
    return response

# ön-yüz add modunda açıldığında son-kullanıcıya "CSV YÜKLE" butonu gösterilir, bu butona tıklayarak csv dosyası yüklendinde bu endpoint'e gelir
# csv dosyası parse edilir ve iki boyutlu array olarak ön-yüze döndürülür
@app.route('/api/uploadcsv', methods=["GET", "POST"])
def upload_csv():
    if request.method == 'POST':
        response = ops.upload_csv(request.files["file"], request.form["filename"])
        return jsonify(response)
    else:
        response = jsonify({'status': 'OK'})
        return response

# ön-yüz add modunda açıldığında son-kullanıcıya "EXCEL YÜKLE" butonu gösterilir, bu butona tıklayarak xlsx dosyası yüklendinde bu endpoint'e gelir
# xlsx dosyası parse edilir ve iki boyutlu array olarak ön-yüze döndürülür
@app.route('/api/uploadxls', methods=["GET", "POST"])
def upload_xls():
    if request.method == 'POST':
        response = ops.upload_xls(request.files["file"], request.form["filename"])
        return jsonify(response)
    else:
        response = jsonify({'status': 'OK'})
        return response

if __name__ == '__main__':
    app.run(port=5001, host='0.0.0.0')