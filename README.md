# Clinic Maker (☤)

**Clinic Maker** is a Hermes-powered business launch agent engineered to streamline the setup of secure cash-pay clinical micropractices. With a single command, clinicians can bypass administrative complexity and automatically configure a fully functioning web presence, patient inquiry queue, checkout integration layout, and automated follow-ups—all running inside a high-security container.

---

## 💡 The Core Problem & Vision

Launching a modern, cash-pay clinic currently requires navigating multiple complex SaaS platforms—from website builders to patient intakes, database tables, SMS follow-up engines, and payment links. Most medical professionals would rather focus on direct patient care than handle manual software operations.

Clinic Maker demonstrates how **Hermes Agent** can act as a secure, autonomous operations manager. It automatically provisions a localized, synthetic clinical launch stack that is:
1. **Frictionless:** Fully bootstraps a clean web presence and intake pipeline in seconds.
2. **Compliant By Design:** Maintains a strict diagnostic wall and zero-PHI constraint.
3. **Pre-Audited:** Constrained by kernel-level security rules before execution.

---

## 🛡️ NVIDIA NemoClaw Sandboxed Security

Clinical operations involve sensitive procedures, financial architectures, and operational configurations. Running an autonomous execution script safely requires a robust guardrail framework.

Clinic Maker features a production-ready declarative security configuration modeled directly on the **NVIDIA NemoClaw & OpenShell** sandboxing specifications:

- **Filesystem Boundaries (Landlock):** The agent runs with extreme least-privilege constraints. It operates entirely as read-only across major system assets, restricting write access strictly to `/app/output` and `/app/db`.
- **Egress Network Policies:** Outbound requests are blocked by default. Network egress is explicitly restricted to designated hosts (`api.stripe.com`, `api.twilio.com`, and `inference.local` via the OpenShell local gateway). This keeps sensitive model auth secrets isolated on the operator's host machine.
- **Human-In-The-Loop Approval Gates:** Clinic Maker enforces explicit, interactive user approval triggers inside the CLI tool prior to conducting database creation, Stripe layout assemblies, or code mutations.

---

## 💳 Stripe Projects & Messaging Integration

We utilize robust mocking layers to trace payment setups:
* **Stripe Project Configuration:** Compiles sample checkouts and test session mapping without exposing operational credentials.
* **Twilio SMS Follow-up Logs:** Monitors localized intake registrations and prints real-time transactional logs representing the delivery of patient booking text confirmations.

---

## 🚀 How to Run the Sandboxed Simulation

### 1. Pre-requisites
- **Python 3.x**
- Any modern web browser.

### 2. Launch the Operator Agent
Run the sandboxed supervisor setup script locally:
```bash
python3 clinic-maker.py
```
*Simply press `y` to approve target triggers (mocking the NemoClaw approval gates).*

### 3. Open the ClearClinic Front-End Portal
To browse the modern interactive interface, open `/app/index.html` in your favorite browser.
- Try submitting a synthetic booking inquiry.
- Check the real-time **Stripe Integration & Twilio SMS Sandbox Logs** panels at the bottom of the dashboard to see the background operational logs in action!

---

## ⚕️ Safety Bounds & Disclaimer
> **This is a synthetic healthcare business operations demonstration.** 
> It is strictly meant for administrative, planning, and deployment simulations. This repository does not collect or process real Protected Health Information (PHI) or personal details, nor does it diagnose, recommend medical treatments, or conduct clinical triaging. All patient files, names, and inquiry details are fully simulated mockup configurations.
