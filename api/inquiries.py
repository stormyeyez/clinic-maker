"""
Vercel serverless function — static demo patient data.
IMPORTANT (honest limitation): Vercel serverless functions have no persistent
filesystem, so SQLite can't live here. This endpoint returns the same fixed
synthetic demo records every time — it does NOT persist new writes. The full
live version (real SQLite reads/writes) runs locally via `python3 clinic-maker.py`.
The Stripe checkout endpoint (api/stripe/checkout.py) IS fully live here.
"""
import json
from http.server import BaseHTTPRequestHandler

DEMO_INQUIRIES = [
    {"id": 6, "name": "Riley B.", "visit_type": "Medication Refill Evaluation ($90)",
     "reason_preview": "Monthly refill request for blood pressure medication, stable readings.",
     "status": "Pending SMS", "timestamp": "2026-06-30 05:48:20"},
    {"id": 5, "name": "Jordan K.", "visit_type": "Standard Telehealth Visit ($75)",
     "reason_preview": "General wellness consult and seasonal allergy review.",
     "status": "Pending SMS", "timestamp": "2026-06-30 05:02:55"},
    {"id": 3, "name": "Alex T.", "visit_type": "Medication Refill Evaluation ($90)",
     "reason_preview": "Standard assessment of chronic asthma inhaler compliance parameters.",
     "status": "New Inquiry", "timestamp": "2026-06-29 23:57:39"},
    {"id": 2, "name": "Pat R.", "visit_type": "Standard Telehealth Visit ($75)",
     "reason_preview": "General wellness consult evaluation recommendation for seasonal sniffles.",
     "status": "Contacted", "timestamp": "2026-06-30 02:57:39"},
    {"id": 1, "name": "Taylor M.", "visit_type": "School / Work Absence Evaluation ($60)",
     "reason_preview": "Verify clinical recovery to approve note for Tuesday class return.",
     "status": "Pending SMS", "timestamp": "2026-06-30 04:57:39"},
]


class handler(BaseHTTPRequestHandler):
    def _cors(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")

    def do_OPTIONS(self):
        self.send_response(200)
        self._cors()
        self.end_headers()

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self._cors()
        self.end_headers()
        self.wfile.write(json.dumps(DEMO_INQUIRIES).encode())

    def do_POST(self):
        # Honest no-op: this deployment has no persistent storage, so we
        # acknowledge the request but do not fabricate a saved record.
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self._cors()
        self.end_headers()
        self.wfile.write(json.dumps({
            "status": "demo_only",
            "note": "This Vercel deployment shows static demo data — patient writes require the local backend (python3 clinic-maker.py) with a real SQLite database."
        }).encode())
