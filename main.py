from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # Получаем данные из формы
        email = request.form.get("email")
        message = request.form.get("message")
        
        # Обработка (ничего не сохраняем, просто выводим)
        print(f"Email: {email}, Message: {message}")
        
        # Возвращаем успешный ответ в формате JSON
        return jsonify({"status": "success", "message": "Message sent!"})
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)