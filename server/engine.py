from pathlib import Path
import sys

from flask import Flask, request, jsonify


# Project root
ROOT = Path(__file__).resolve().parent.parent

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


from languages.tamil.unified_engine import process


app = Flask(__name__)


@app.get("/health")
def health():
    return jsonify({
        "status": "ok",
        "engine": "lexora-tamil",
        "version": "1.0"
    })


@app.post("/process")
def process_text():

    body = request.get_json(
        silent=True
    ) or {}

    text = body.get("text")

    if not isinstance(text, str) or not text.strip():

        return jsonify({
            "error": {
                "code": "invalid_text",
                "message": "text must be a non-empty string"
            }
        }), 400

    try:

        result = process(text)

        return jsonify({
            "status": "success",
            "results": result
        })

    except Exception as exc:

        return jsonify({
            "error": {
                "code": "engine_error",
                "message": str(exc)
            }
        }), 500


if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=8000
    )
