#!/usr/bin/env python3
import sys
import socket
from datetime import datetime
import dns.resolver
import dns.exception

# ANSI color codes for neon effects
class Colors:
    BOLD = '\033[1m'
    NEON_GREEN = '\033[92m'
    NEON_RED = '\033[91m'
    NEON_BLUE = '\033[94m'
    NEON_YELLOW = '\033[93m'
    NEON_PURPLE = '\033[95m'
    NEON_CYAN = '\033[96m'
    NEON_ORANGE = '\033[38;5;208m'
    NEON_PINK = '\033[38;5;201m'
    RESET = '\033[0m'

TLDS = [
    "com", "org", "net", "edu", "gov", "mil", "int",
    "biz", "info", "name", "pro", "aero", "asia", "cat",
    "coop", "jobs", "mobi", "museum", "tel", "travel",
    "xxx", "xyz", "club", "online", "shop", "site", "tech",
    "store", "space", "website", "cloud", "host", "press",
    "digital", "media", "news", "design", "art", "photo",
    "video", "music", "film", "tv", "radio", "fm",
    "ir", "af", "al", "dz", "as", "ad", "ao", "ai", "aq", "ag", "ar",
    "am", "aw", "au", "at", "az", "bs", "bh", "bd", "bb", "by",
    "be", "bz", "bj", "bm", "bt", "bo", "ba", "bw", "br", "io",
    "bn", "bg", "bf", "bi", "kh", "cm", "ca", "cv", "ky", "cf",
    "td", "cl", "cn", "cx", "cc", "co", "km", "cd", "cg", "ck",
    "cr", "hr", "cu", "cy", "cz", "dk", "dj", "dm", "do", "ec",
    "eg", "sv", "gq", "er", "ee", "et", "fk", "fo", "fj", "fi",
    "fr", "gf", "pf", "tf", "ga", "gm", "ge", "de", "gh", "gi",
    "gr", "gl", "gd", "gp", "gu", "gt", "gg", "gn", "gw", "gy",
    "ht", "hn", "hk", "hu", "is", "in", "id", "iq", "ie",
    "im", "il", "it", "jm", "jp", "je", "jo", "kz", "ke", "ki",
    "kp", "kr", "kw", "kg", "la", "lv", "lb", "ls", "lr", "ly",
    "li", "lt", "lu", "mo", "mk", "mg", "mw", "my", "mv", "ml",
    "mt", "mh", "mq", "mr", "mu", "yt", "mx", "fm", "md", "mc",
    "mn", "me", "ms", "ma", "mz", "mm", "na", "nr", "np", "nl",
    "nc", "nz", "ni", "ne", "ng", "nu", "nf", "mp", "no", "om",
    "pk", "pw", "ps", "pa", "pg", "py", "pe", "ph", "pn", "pl",
    "pt", "pr", "qa", "ro", "ru", "rw", "re", "bl", "sh", "kn",
    "lc", "mf", "pm", "vc", "ws", "sm", "st", "sa", "sn", "rs",
    "sc", "sl", "sg", "sk", "si", "sb", "so", "za", "gs", "es",
    "lk", "sd", "sr", "sj", "sz", "se", "ch", "sy", "tw", "tj",
    "tz", "th", "tl", "tg", "tk", "to", "tt", "tn", "tr", "tm",
    "tc", "tv", "ug", "ua", "ae", "gb", "us", "uy", "uz", "vu",
    "ve", "vn", "vg", "vi", "wf", "eh", "ye", "zm", "zw"
]

def check_domain(domain):
    try:
        resolver = dns.resolver.Resolver()
        resolver.nameservers = ['8.8.8.8', '1.1.1.1']
        resolver.timeout = 2
        resolver.lifetime = 2
        
        answers = resolver.resolve(domain, 'A')
        if answers:
            return True, str(answers[0])
        return False, None
    except (dns.exception.DNSException, socket.error):
        return False, None

def print_neon(text, color=Colors.NEON_CYAN, bold=True):
    bold_code = Colors.BOLD if bold else ''
    print(f"{bold_code}{color}{text}{Colors.RESET}")

def test_domain(name):
    total = len(TLDS)
    found = []
    not_found = []
    last_domains = []
    
    print_neon("\n🔍 Starting domain testing for: " + name, Colors.NEON_PURPLE)
    print_neon("=" * 60, Colors.NEON_PINK)
    print_neon(f"⏰ Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", Colors.NEON_YELLOW)
    print_neon("🌐 Using Google DNS (8.8.8.8) for accurate results", Colors.NEON_BLUE)
    print_neon("-" * 60, Colors.NEON_ORANGE)
    
    for index, tld in enumerate(TLDS, 1):
        domain = f"{name}.{tld}"
        found_status, ip = check_domain(domain)
        
        if found_status:
            found.append((domain, ip))
            status = "✅"
            color = Colors.NEON_GREEN
            result_line = f"{status} {domain}  ➜  {ip}"
        else:
            not_found.append(domain)
            status = "❌"
            color = Colors.NEON_RED
            result_line = f"{status} {domain}  ➜  Not found"
        
        last_domains.append(result_line)
        if len(last_domains) > 5:
            last_domains.pop(0)
        
        progress = (index / total) * 100
        
        # Clear previous lines and show progress
        sys.stdout.write('\033[2J\033[H')
        
        print_neon("\n🔍 Starting domain testing for: " + name, Colors.NEON_PURPLE)
        print_neon("=" * 60, Colors.NEON_PINK)
        print_neon(f"⏰ Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", Colors.NEON_YELLOW)
        print_neon("🌐 Using Google DNS (8.8.8.8) for accurate results", Colors.NEON_BLUE)
        print_neon("-" * 60, Colors.NEON_ORANGE)
        
        # Progress bar
        bar_length = 50
        filled = int(bar_length * index / total)
        bar = '█' * filled + '░' * (bar_length - filled)
        print_neon(f"\r📊 Progress: {bar} {index}/{total} ({progress:.1f}%)", Colors.NEON_CYAN)
        
        # Statistics
        print_neon(f"✅ Found: {len(found)}  ❌ Not found: {len(not_found)}", Colors.NEON_GREEN if found else Colors.NEON_RED)
        print_neon("-" * 60, Colors.NEON_ORANGE)
        
        # Show last 5 results
        for line in last_domains:
            if "✅" in line:
                print_neon(line, Colors.NEON_GREEN)
            else:
                print_neon(line, Colors.NEON_RED)
        
        sys.stdout.flush()
    
    # Final results
    print("\n" + "=" * 60)
    print_neon(f"📋 FINAL RESULTS FOR: {name}", Colors.NEON_PURPLE)
    print("=" * 60)
    
    for domain, ip in found:
        print_neon(f"✅ {domain}  ➜  {ip}", Colors.NEON_GREEN)
    
    for domain in not_found:
        print_neon(f"❌ {domain}  ➜  Not found", Colors.NEON_RED)
    
    print("\n" + "=" * 60)
    print_neon("📊 STATISTICS:", Colors.NEON_PINK)
    print_neon("-" * 30, Colors.NEON_PINK)
    print_neon(f"✅ Found     : {len(found)}", Colors.NEON_GREEN)
    print_neon(f"❌ Not Found : {len(not_found)}", Colors.NEON_RED)
    print_neon(f"📦 Total     : {total}", Colors.NEON_YELLOW)
    print_neon(f"📈 Found Rate: {(len(found)/total)*100:.2f}%", Colors.NEON_BLUE if (len(found)/total)*100 > 50 else Colors.NEON_ORANGE)
    print("=" * 60)
    print_neon(f"⏰ Finished at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", Colors.NEON_YELLOW)

def main():
    # Clear screen
    sys.stdout.write('\033[2J\033[H')
    
    print_neon("=" * 60, Colors.NEON_PINK)
    print_neon("🌐 DOMAIN SCANNER v1.0", Colors.NEON_PURPLE)
    print_neon("🔍 Ultimate Domain TLD Checker", Colors.NEON_BLUE)
    print_neon("< Created by Malicious > TG : @M4lic1ous", Colors.NEON_BLUE)
    print_neon("=" * 60, Colors.NEON_PINK)
    
    domain_name = input(f"\n{Colors.BOLD}{Colors.NEON_YELLOW}📝 Enter domain name (without extension): {Colors.RESET}").strip()
    
    if not domain_name:
        print_neon("❌ Domain name cannot be empty!", Colors.NEON_RED)
        sys.exit(1)
    
    try:
        import dns.resolver
    except ImportError:
        print_neon("dnspython is not installed !", Colors.NEON_YELLOW)
        import subprocess
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "dnspython"])
            import dns.resolver
        except Exception as e:
            print_neon(f"❌ Failed to install dnspython: {e}", Colors.NEON_RED)
            print_neon("💡 Please install manually: pip install dnspython", Colors.NEON_ORANGE)
            sys.exit(1)
    
    test_domain(domain_name)

if __name__ == "__main__":
    main()
