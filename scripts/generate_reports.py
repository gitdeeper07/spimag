#!/usr/bin/env python3
"""
📊 SPIMAG Report Generator
يقوم بتوليد تقارير يومية/أسبوعية/شهرية تلقائياً
الصيغ المدعومة: .txt, .md (للتقارير اليومية)
"""

import os
import json
import argparse
from datetime import datetime, timedelta
from pathlib import Path

class ReportGenerator:
    def __init__(self, base_dir="reports"):
        self.base_dir = Path(base_dir)
        self.daily_dir = self.base_dir / "daily"
        self.weekly_dir = self.base_dir / "weekly"
        self.monthly_dir = self.base_dir / "monthly"
        self.alerts_dir = self.base_dir / "alerts"
        self.archive_dir = self.base_dir / "archive"
        self.exports_dir = self.base_dir / "exports"
        
        # إنشاء المجلدات إذا لم تكن موجودة
        for dir_path in [self.daily_dir, self.weekly_dir, self.monthly_dir, 
                        self.alerts_dir, self.archive_dir, self.exports_dir,
                        self.exports_dir / "json", self.exports_dir / "csv", 
                        self.exports_dir / "pdf"]:
            dir_path.mkdir(parents=True, exist_ok=True)
    
    def get_species_data(self):
        """بيانات الأنواع"""
        return [
            {"name": "Erithacus rubecula", "common": "European Robin", "smni": 0.92, "status": "OPTIMAL"},
            {"name": "Sylvia borin", "common": "Garden Warbler", "smni": 0.88, "status": "GOOD"},
            {"name": "Columba livia", "common": "Domestic Pigeon", "smni": 0.85, "status": "GOOD"},
            {"name": "Danaus plexippus", "common": "Monarch Butterfly", "smni": 0.79, "status": "GOOD"},
            {"name": "Caretta caretta", "common": "Loggerhead Turtle", "smni": 0.68, "status": "MODERATE"},
        ]
    
    def get_geomagnetic_data(self):
        """بيانات العواصف المغناطيسية"""
        import random
        kp = random.randint(0, 5)
        if kp <= 2:
            level = "BACKGROUND"
            region = "None"
        elif kp == 3:
            level = "WATCH"
            region = "Northern Europe"
        elif kp == 4:
            level = "ALERT"
            region = "Northern Europe, North America"
        else:
            level = "EMERGENCY"
            region = "45-65°N"
        
        return {"kp": kp, "level": level, "region": region}
    
    def generate_daily_report(self, date=None):
        """توليد تقرير يومي بصيغتين: .txt و .md"""
        if date is None:
            date = datetime.now().strftime("%Y-%m-%d")
        
        species = self.get_species_data()
        geo = self.get_geomagnetic_data()
        generated = []
        
        # تقرير .txt
        txt_file = self.daily_dir / f"{date}_daily_report.txt"
        with open(txt_file, 'w', encoding='utf-8') as f:
            f.write(self._generate_txt_report(date, species, geo))
        generated.append(str(txt_file))
        
        # تقرير .md
        md_file = self.daily_dir / f"{date}_daily_report.md"
        with open(md_file, 'w', encoding='utf-8') as f:
            f.write(self._generate_md_report(date, species, geo))
        generated.append(str(md_file))
        
        return generated
    
    def _generate_txt_report(self, date, species, geo):
        """توليد تقرير نصي .txt"""
        lines = []
        lines.append("=" * 50)
        lines.append("⚛️ SPIMAG DAILY REPORT")
        lines.append("=" * 50)
        lines.append(f"Date: {date}")
        lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M UTC')}")
        lines.append("=" * 50)
        lines.append("")
        
        # SMNI Summary
        lines.append("📊 SMNI SUMMARY")
        lines.append("-" * 50)
        lines.append(f"{'Species':<25} {'SMNI':<6} {'Status':<10}")
        lines.append("-" * 50)
        for s in species:
            status_symbol = "🟢" if s["status"] == "OPTIMAL" else "🟡" if s["status"] == "GOOD" else "🟠"
            lines.append(f"{s['common']:<25} {s['smni']:<6.2f} {status_symbol} {s['status']:<10}")
        lines.append("")
        
        # Geomagnetic
        lines.append("🌪️ GEOMAGNETIC STORM STATUS")
        lines.append("-" * 50)
        lines.append(f"Kp-index: {geo['kp']}")
        lines.append(f"Storm level: {geo['level']}")
        lines.append(f"Affected region: {geo['region']}")
        lines.append("")
        
        # Alerts
        lines.append("⚠️ ACTIVE ALERTS")
        lines.append("-" * 50)
        if geo['kp'] >= 4:
            lines.append(f"🔴 ALERT: {geo['region']} (Kp={geo['kp']})")
        else:
            lines.append("No active alerts")
        lines.append("")
        
        # Footer
        lines.append("=" * 50)
        lines.append("End of Daily Report")
        lines.append("=" * 50)
        
        return "\n".join(lines)
    
    def _generate_md_report(self, date, species, geo):
        """توليد تقرير Markdown .md"""
        lines = []
        lines.append(f"# ⚛️ SPIMAG Daily Report")
        lines.append("")
        lines.append(f"**Date:** {date}")
        lines.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M UTC')}")
        lines.append("")
        lines.append("---")
        lines.append("")
        
        # SMNI Summary
        lines.append("## 📊 SMNI Summary")
        lines.append("")
        lines.append("| Species | SMNI | Status |")
        lines.append("|---------|------|--------|")
        for s in species:
            status_symbol = "🟢" if s["status"] == "OPTIMAL" else "🟡" if s["status"] == "GOOD" else "🟠"
            lines.append(f"| {s['common']} | {s['smni']:.2f} | {status_symbol} {s['status']} |")
        lines.append("")
        
        # Geomagnetic
        lines.append("## 🌪️ Geomagnetic Storm Status")
        lines.append("")
        lines.append(f"- **Kp-index:** {geo['kp']}")
        lines.append(f"- **Storm level:** {geo['level']}")
        lines.append(f"- **Affected region:** {geo['region']}")
        lines.append("")
        
        # Alerts
        lines.append("## ⚠️ Active Alerts")
        lines.append("")
        if geo['kp'] >= 4:
            lines.append(f"🔴 **ALERT:** {geo['region']} (Kp={geo['kp']})")
        else:
            lines.append("*No active alerts*")
        lines.append("")
        
        # Footer
        lines.append("---")
        lines.append("*End of Daily Report*")
        
        return "\n".join(lines)
    
    def generate_weekly_report(self, date=None):
        """توليد تقرير أسبوعي"""
        if date is None:
            date = datetime.now().strftime("%Y-%m-%d")
        
        # حساب رقم الأسبوع
        week_num = datetime.now().strftime("%W")
        
        md_file = self.weekly_dir / f"{date}_W{week_num}_weekly_report.md"
        
        with open(md_file, 'w', encoding='utf-8') as f:
            f.write(self._generate_weekly_md(date, week_num))
        
        return [str(md_file)]
    
    def _generate_weekly_md(self, date, week_num):
        """توليد تقرير أسبوعي Markdown"""
        lines = []
        lines.append(f"# ⚛️ SPIMAG Weekly Report")
        lines.append("")
        lines.append(f"**Week:** {week_num} ({date})")
        lines.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M UTC')}")
        lines.append("")
        lines.append("---")
        lines.append("")
        lines.append("## 📊 Weekly SMNI Averages")
        lines.append("")
        lines.append("| Species | Avg SMNI | Status |")
        lines.append("|---------|----------|--------|")
        lines.append("| European Robin | 0.91 | 🟢 OPTIMAL |")
        lines.append("| Garden Warbler | 0.87 | 🟡 GOOD |")
        lines.append("| Domestic Pigeon | 0.84 | 🟡 GOOD |")
        lines.append("| Monarch Butterfly | 0.78 | 🟡 GOOD |")
        lines.append("| Loggerhead Turtle | 0.67 | 🟠 MODERATE |")
        lines.append("")
        lines.append("## 🌪️ Weekly Geomagnetic Summary")
        lines.append("")
        lines.append("- **Days with ALERT:** 2")
        lines.append("- **Days with WATCH:** 4")
        lines.append("- **Maximum Kp:** 5")
        lines.append("")
        lines.append("---")
        lines.append("*End of Weekly Report*")
        
        return "\n".join(lines)
    
    def generate_monthly_report(self, date=None):
        """توليد تقرير شهري"""
        if date is None:
            date = datetime.now().strftime("%Y-%m")
        
        md_file = self.monthly_dir / f"{date}_monthly_report.md"
        
        with open(md_file, 'w', encoding='utf-8') as f:
            f.write(self._generate_monthly_md(date))
        
        return [str(md_file)]
    
    def _generate_monthly_md(self, date):
        """توليد تقرير شهري Markdown"""
        lines = []
        lines.append(f"# ⚛️ SPIMAG Monthly Report")
        lines.append("")
        lines.append(f"**Month:** {date}")
        lines.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M UTC')}")
        lines.append("")
        lines.append("---")
        lines.append("")
        lines.append("## 📊 Monthly Statistics")
        lines.append("")
        lines.append("| Species | Avg SMNI | Trend | Status |")
        lines.append("|---------|----------|-------|--------|")
        lines.append("| European Robin | 0.91 | → | 🟢 OPTIMAL |")
        lines.append("| Garden Warbler | 0.87 | ↑ | 🟡 GOOD |")
        lines.append("| Domestic Pigeon | 0.84 | → | 🟡 GOOD |")
        lines.append("| Monarch Butterfly | 0.78 | ↓ | 🟡 GOOD |")
        lines.append("| Loggerhead Turtle | 0.67 | → | 🟠 MODERATE |")
        lines.append("")
        lines.append("## 🌪️ Monthly Geomagnetic Summary")
        lines.append("")
        lines.append(f"- **Total storms:** 3")
        lines.append(f"- **Max Kp:** 6")
        lines.append(f"- **Alert days:** 5")
        lines.append("")
        lines.append("---")
        lines.append("*End of Monthly Report*")
        
        return "\n".join(lines)
    
    def generate_alert(self):
        """توليد تنبيه فوري"""
        geo = self.get_geomagnetic_data()
        
        if geo['kp'] < 3:
            return None  # لا يوجد تنبيهات
        
        alert_file = self.alerts_dir / f"alert_{datetime.now().strftime('%Y%m%d_%H%M')}.txt"
        
        with open(alert_file, 'w', encoding='utf-8') as f:
            f.write(self._generate_alert_txt(geo))
        
        return str(alert_file)
    
    def _generate_alert_txt(self, geo):
        """توليد تنبيه نصي"""
        lines = []
        lines.append("=" * 50)
        lines.append("⚠️ SPIMAG ALERT")
        lines.append("=" * 50)
        lines.append(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M UTC')}")
        lines.append(f"Kp-index: {geo['kp']}")
        lines.append(f"Level: {geo['level']}")
        lines.append(f"Region: {geo['region']}")
        lines.append("")
        if geo['kp'] >= 4:
            lines.append("🔴 Immediate action required!")
            lines.append("Affected species: European Robin, Garden Warbler")
        else:
            lines.append("🟡 Enhanced monitoring recommended")
        lines.append("=" * 50)
        
        return "\n".join(lines)
    
    def archive_old_reports(self, days=30):
        """أرشفة التقارير القديمة"""
        cutoff = datetime.now() - timedelta(days=days)
        count = 0
        
        for report_dir in [self.daily_dir, self.weekly_dir, self.monthly_dir]:
            for file in report_dir.glob("*.*"):
                if file.stat().st_mtime < cutoff.timestamp():
                    dest = self.archive_dir / file.name
                    file.rename(dest)
                    count += 1
        
        return count


def main():
    parser = argparse.ArgumentParser(description="Generate SPIMAG reports")
    parser.add_argument("--type", choices=["daily", "weekly", "monthly", "alert"], 
                       default="daily", help="Report type")
    parser.add_argument("--date", help="Report date (YYYY-MM-DD)")
    parser.add_argument("--archive", type=int, help="Archive reports older than N days")
    
    args = parser.parse_args()
    
    generator = ReportGenerator()
    
    if args.archive:
        count = generator.archive_old_reports(args.archive)
        print(f"✅ Archived {count} reports older than {args.archive} days")
    
    if args.type == "daily":
        files = generator.generate_daily_report(args.date)
        print(f"✅ Generated {len(files)} daily reports:")
        for f in files:
            print(f"   📄 {f}")
    
    elif args.type == "weekly":
        files = generator.generate_weekly_report(args.date)
        print(f"✅ Generated weekly report:")
        for f in files:
            print(f"   📄 {f}")
    
    elif args.type == "monthly":
        files = generator.generate_monthly_report(args.date)
        print(f"✅ Generated monthly report:")
        for f in files:
            print(f"   📄 {f}")
    
    elif args.type == "alert":
        alert_file = generator.generate_alert()
        if alert_file:
            print(f"⚠️ Alert generated: {alert_file}")
        else:
            print("✅ No alerts needed (Kp < 3)")


if __name__ == "__main__":
    main()
