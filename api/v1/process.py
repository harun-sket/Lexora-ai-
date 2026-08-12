import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from languages.tamil.unified_engine import process


def handler(request):
    if request.method != "POST":
        return {
            "statusCode": 405,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps({
                "error": {
                    "code": "method_not_allowed",
                    "message": "Use POST."
                }
            }, ensure_ascii=False)
        }

    try:
        body = request.body

        if isinstance(body, bytes):
            body = body.decode("utf-8")

        if isinstance(body, str):
            body = json.loads(body)

        if not isinstance(body, dict):
            raise ValueError("Request body must be JSON.")

        text = body.get("text")

        if not isinstance(text, str):
            return {
                "statusCode": 400,
                "headers": {
                    "Content-Type": "application/json"
                },
                "body": json.dumps({
                    "error": {
                        "code": "invalid_input",
                        "message": "text must be a string."
                    }
                }, ensure_ascii=False)
            }

        result = process(text)

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps({
                "success": True,
                "data": result
            }, ensure_ascii=False, default=str)
        }

    except Exception as exc:
        print("LEXORA API ERROR:", repr(exc), file=sys.stderr)

        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps({
                "error": {
                    "code": "internal_error",
                    "message": str(exc)
                }
            }, ensure_ascii=False)
        }
