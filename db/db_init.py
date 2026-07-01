#!/usr/bin/env python3
import os
import sqlite3
import datetime
from pathlib import Path

def init_db():
    # Setup target directories relative to this file, so it works on any machine
    db_dir = str(Path(__file__).parent.parent / "app" / "db")
    os.makedirs(db_dir, exist_ok=True)
    db_path = os.path.join(db_dir, "database.sqlite")
    
    print(f"🔨 Initializing SQLite Database at: {db_path}...")
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Create the inquiries table matching our ClearClinic specifications
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS patient_inquiries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            visit_type TEXT NOT NULL,
            reason_preview TEXT NOT NULL,
            status TEXT NOT NULL,
            timestamp TEXT NOT NULL
        )
    """)
    
    # Check if we already have records; if so, skip insertions to prevent duplicates
    cursor.execute("SELECT COUNT(*) FROM patient_inquiries")
    if cursor.fetchone()[0] == 0:
        print("Inserting 3 baseline synthetic clinic inquiries...")
        synthetic_records = [
            (
                "Taylor M.", 
                "School / Work Absence Evaluation ($60)", 
                "Verify clinical recovery to approve note for Tuesday class return.", 
                "Pending SMS", 
                datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ),
            (
                "Pat R.", 
                "Standard Telehealth Visit ($75)", 
                "General wellness consult evaluation recommendation for seasonal sniffles.", 
                "Contacted", 
                (datetime.datetime.now() - datetime.timedelta(hours=2)).strftime("%Y-%m-%d %H:%M:%S")
            ),
            (
                "Alex T.",
                "Medication Refill Evaluation ($90)",
                "Standard assessment of chronic asthma inhaler compliance parameters.",
                "New Inquiry",
                (datetime.datetime.now() - datetime.timedelta(hours=5)).strftime("%Y-%m-%d %H:%M:%S")
            )
        ]
        
        cursor.executemany("""
            INSERT INTO patient_inquiries (name, visit_type, reason_preview, status, timestamp)
            VALUES (?, ?, ?, ?, ?)
        """, synthetic_records)
        conn.commit()
        print("✅ Pre-loaded 100% synthetic baseline data successfully.")
    else:
        print("ℹ️ Existing SQLite records found. Skipping baseline seed stage.")
        
    conn.close()
    print("✨ Database setup complete.")

if __name__ == "__main__":
    init_db()
