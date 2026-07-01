"""
Vercel serverless function — real Stripe Checkout Sessions API.
This is the one part of Clinic Maker that is fully live on Vercel: every
request here makes a real call to api.stripe.com and returns a real,
working checkout URL. No mocking, no simulation.
"""
import json
import os
import re
import urllib.parse
import urllib.request
from http.server import BaseHTTPRequestHandler

STRIPE_SECRET_KEY = os.environ.get("STRIPE_SECRET_KEY") or os.environ.get("STRIPE_API_KEY", "")

PRICE_MAP = {
    "$75": 7500, "$90": 9000, "$60": 6000,
    "$125": 12500, "$50": 5000,
}


class handler(BaseHTTPRequestHandler):
    def _cors(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")

    def do_OPTIONS(self):
        self.send_response(200)
        self._cors()
        self.end_headers()

    def do_POST(self):
        content_length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_length) if content_length else b"{}"

        try:
            data = json.loads(body.decode("utf-8"))
            visit_type = data.get("visit_type", "Telehealth Visit ($75)")
            name = data.get("name", "Patient")

            m = re.search(r"\$(\d+)", visit_type)
            amount = PRICE_MAP.get(f"${m.group(1)}", 7500) if m else 7500
            label = re.sub(r"\s*\(\$\d+\)", "", visit_type).strip()

            if not STRIPE_SECRET_KEY.startswith("sk_"):
                raise Exception("No valid Stripe key configured on this deployment")

            host = self.headers.get("Host", "")
            scheme = "https" if host else "http"
            base_url = f"{scheme}://{host}" if host else "http://localhost:3458"

            payload = urllib.parse.urlencode({
                "payment_method_types[]": "card",
                "mode": "payment",
                "success_url": f"{base_url}/?success=1",
                "cancel_url": f"{base_url}/?cancelled=1",
                "line_items[0][price_data][currency]": "usd",
                "line_items[0][price_data][unit_amount]": str(amount),
                "line_items[0][price_data][product_data][name]": label,
                "line_items[0][price_data][product_data][description]": f"Clearpoint Clinic — {name}",
                "line_items[0][quantity]": "1",
            }).encode()

            req = urllib.request.Request(
                "https://api.stripe.com/v1/checkout/sessions",
                data=payload,
                headers={
                    "Authorization": f"Bearer {STRIPE_SECRET_KEY}",
                    "Content-Type": "application/x-www-form-urlencoded",
                },
            )
            with urllib.request.urlopen(req) as resp:
                session = json.loads(resp.read())

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self._cors()
            self.end_headers()
            self.wfile.write(json.dumps({"url": session["url"], "id": session["id"]}).encode())
        except Exception as e:
            self.send_response(500)
            self.send_header("Content-Type", "application/json")
            self._cors()
            self.end_headers()
            self.wfile.write(json.dumps({"error": str(e)}).encode())
