from flask import Flask, render_template, request, jsonify
import wordninja
from spellchecker import SpellChecker

spell = SpellChecker()

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
   return render_template('index.html') 


@app.route("/spellChecker", methods = ['GET'])
def update_pdf_page_status():
   if request.method == 'GET':
      print("Spell checker api invoked")
      #get the API parameters
      text = request.args.get("str")
      # Get the one `most likely` answer
      correctedText = spell.correction(text)

      #split the composite words
      w = wordninja.split(correctedText)
      words = w
      return jsonify({"message":"success", "words": words})
		
if __name__ == '__main__':
   app.run(host='0.0.0.0')
