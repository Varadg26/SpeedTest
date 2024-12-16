from flask import Flask, jsonify, render_template
import speedtest

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Serves the HTML frontend

@app.route('/speedtest', methods=['GET'])
def speed_test():
    try:
        st = speedtest.Speedtest()
        st.get_best_server()

        download_speed = st.download() / 1_000_000  # Convert to Mbps
        upload_speed = st.upload() / 1_000_000  # Convert to Mbps
        ping = st.results.ping

        return jsonify({
            "ping": round(ping, 2),
            "download_speed": round(download_speed, 2),
            "upload_speed": round(upload_speed, 2)
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

