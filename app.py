from flask import Flask, request, jsonify
from PIL import Image
import io
import random

app = Flask(__name__)

@app.route('/diagnose', methods=['POST'])
def diagnose():
    if 'file' not in request.files:
        return jsonify({'status': 'error', 'message': 'Tiada gambar dimuat naik.'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'status': 'error', 'message': 'Fail kosong.'}), 400

    try:
        img = Image.open(file.stream)
        img = img.convert("RGB")

        # Simulated AI response (replace with real model later)
        simulated_diagnosis = random.choice([
            {"result": "Daun sihat", "suggestion": "Tiada rawatan diperlukan."},
            {"result": "Hawar Daun", "suggestion": "Gunakan fungisida kuprum & elakkan penyiraman petang."},
            {"result": "Kekurangan nutrien", "suggestion": "Tambah baja NPK seimbang & pantau tanah."},
        ])
        simulated_diagnosis['confidence'] = f"{random.randint(88, 99)}%"

        return jsonify({
            "status": "ok",
            "diagnosis": simulated_diagnosis['result'],
            "suggestion": simulated_diagnosis['suggestion'],
            "confidence": simulated_diagnosis['confidence']
        })

    except Exception as e:
        return jsonify({'status': 'error', 'message': f'Gagal menganalisa: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
