#!/usr/bin/env python3
import sys
import socket
from datetime import datetime
import dns.resolver
import dns.exception


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
    "com", "org", "net", "edu", "gov", "mil", "int", "biz", "info", "name", "pro", "aero", "asia", "cat",
    "coop", "jobs", "mobi", "museum", "tel", "travel", "xxx", "xyz", "club", "online", "shop", "site", "tech",
    "store", "space", "website", "cloud", "host", "press", "digital", "media", "news", "design", "art", "photo",
    "video", "music", "film", "tv", "radio", "fm", "cc", "st",
    "abogado", "academy", "accountant", "accountants", "actor", "ads", "adult", "agency", "airforce", "apartments",
    "app", "army", "associates", "attorney", "auction", "audio", "auto", "band", "bank", "bar", "bargains", "beer",
    "bet", "bike", "bing", "black", "blackfriday", "blog", "blue", "boats", "boo", "book", "bot", "boutique",
    "build", "builders", "business", "cab", "cafe", "cam", "camera", "camp", "capital", "car", "cards", "care",
    "careers", "cars", "casa", "cash", "casino", "catering", "center", "ceo", "chat", "cheap", "christmas",
    "chrome", "church", "city", "claims", "cleaning", "click", "clinic", "clothing", "coach", "codes", "coffee",
    "college", "community", "company", "computer", "condos", "construction", "consulting", "contact", "contractors",
    "cooking", "cool", "country", "coupons", "courses", "credit", "creditcard", "cricket", "cruises", "dad",
    "dance", "dating", "day", "deal", "dealer", "deals", "degree", "delivery", "democrat", "dental", "dentist",
    "desi", "dev", "diamonds", "diet", "direct", "directory", "discount", "doctor", "dog", "domains", "download",
    "earth", "eco", "education", "email", "energy", "engineer", "engineering", "enterprises", "equipment", "esq",
    "estate", "events", "exchange", "expert", "exposed", "express", "fail", "faith", "family", "fans", "farm",
    "fashion", "feedback", "finance", "financial", "fish", "fishing", "fit", "fitness", "flights", "florist",
    "flowers", "football", "forex", "forsale", "foundation", "fun", "fund", "furniture", "futbol", "gallery",
    "games", "garden", "gay", "gift", "gifts", "give", "glass", "global", "gmail", "goo", "google", "gop",
    "graphics", "gratis", "green", "gripe", "grocery", "group", "guide", "guitars", "guru", "haus", "health",
    "healthcare", "heart", "help", "hiphop", "hiv", "hockey", "holdings", "holiday", "home", "horse", "hospital",
    "hosting", "hot", "hotel", "house", "how", "homes", "icu", "immo", "immobilien", "inc", "industries", "ing",
    "ink", "institute", "insure", "international", "investments", "irish", "jetzt", "jewelry", "juegos", "kaufen",
    "kim", "kitchen", "kiwi", "koeln", "krd", "kred", "lacaixa", "land", "law", "lawyer", "lease", "legal",
    "lgbt", "life", "lighting", "limited", "limo", "link", "loans", "lol", "london", "love", "ltd", "ltda",
    "luxe", "luxury", "madrid", "maison", "management", "market", "marketing", "markets", "mba", "memorial",
    "men", "menu", "miami", "microsoft", "money", "mortgage", "motorcycles", "mov", "movie", "navy", "network",
    "ninja", "nyc", "one", "ong", "onl", "ooo", "page", "partners", "parts", "party", "pet", "pharmacy", "photo",
    "photography", "photos", "pics", "pictures", "pin", "pink", "pizza", "place", "plumbing", "plus", "poker",
    "porn", "prime", "prod", "productions", "prof", "properties", "property", "protection", "pubs", "qpon",
    "racing", "realestate", "realty", "recipes", "red", "rehab", "reise", "reisen", "ren", "rent", "rentals",
    "repair", "report", "republican", "rest", "restaurant", "reviews", "rip", "rocks", "rodeo", "rugby", "run",
    "ryukyu", "saarland", "sale", "samsung", "sarl", "scot", "security", "services", "sex", "sexy", "shiksha",
    "shoes", "show", "singles", "ski", "skin", "soccer", "social", "software", "solar", "solutions", "soy",
    "sport", "spreadbetting", "srl", "stream", "studio", "study", "style", "sucks", "supplies", "supply",
    "support", "surf", "surgery", "suzuki", "swiss", "systems", "taipei", "tattoo", "tax", "taxi", "team",
    "technology", "tennis", "theatre", "tickets", "tienda", "tips", "tires", "tirol", "today", "tokyo", "tools",
    "top", "tours", "town", "toys", "trade", "trading", "training", "tube", "university", "uno", "vacations",
    "vegas", "ventures", "versicherung", "vet", "viajes", "villas", "vin", "vip", "vision", "vodka", "vote",
    "voting", "voto", "voyage", "wales", "wang", "watch", "webcam", "wedding", "whoswho", "wien", "wiki", "win",
    "wine", "work", "works", "world", "wtc", "wtf", "xin", "yachts", "yandex", "yoga", "yokohama", "youtube",
    "zip", "zone", "zuerich", "music",
    "ac", "ad", "ae", "af", "ag", "ai", "al", "am", "ao", "aq", "ar", "as", "at", "au", "aw", "ax", "az",
    "ba", "bb", "bd", "be", "bf", "bg", "bh", "bi", "bj", "bl", "bm", "bn", "bo", "bq", "br", "bs", "bt",
    "bv", "bw", "by", "bz", "ca", "cd", "cf", "cg", "ch", "ci", "ck", "cl", "cm", "cn", "co", "cr", "cu",
    "cv", "cw", "cx", "cy", "cz", "de", "dj", "dk", "dm", "do", "dz", "ec", "ee", "eg", "eh", "er", "es",
    "et", "eu", "fi", "fj", "fk", "fm", "fo", "fr", "ga", "gb", "gd", "ge", "gf", "gg", "gh", "gi", "gl",
    "gm", "gn", "gp", "gq", "gr", "gs", "gt", "gu", "gw", "gy", "hk", "hm", "hn", "hr", "ht", "hu", "id",
    "ie", "il", "im", "in", "io", "iq", "ir", "is", "it", "je", "jm", "jo", "jp", "ke", "kg", "kh", "ki",
    "km", "kn", "kp", "kr", "kw", "ky", "kz", "la", "lb", "lc", "li", "lk", "lr", "ls", "lt", "lu", "lv",
    "ly", "ma", "mc", "md", "me", "mf", "mg", "mh", "mk", "ml", "mm", "mn", "mo", "mp", "mq", "mr", "ms",
    "mt", "mu", "mv", "mw", "mx", "my", "mz", "na", "nc", "ne", "nf", "ng", "ni", "nl", "no", "np", "nr",
    "nu", "nz", "om", "pa", "pe", "pf", "pg", "ph", "pk", "pl", "pm", "pn", "pr", "ps", "pt", "pw", "py",
    "qa", "re", "ro", "rs", "ru", "rw", "sa", "sb", "sc", "sd", "se", "sg", "sh", "si", "sj", "sk", "sl",
    "sm", "sn", "so", "sr", "ss", "st", "sv", "sx", "sy", "sz", "tc", "td", "tf", "tg", "th", "tj", "tk",
    "tl", "tm", "tn", "to", "tr", "tt", "tv", "tw", "tz", "ua", "ug", "uk", "us", "uy", "uz", "va", "vc",
    "ve", "vg", "vi", "vn", "vu", "wf", "ws", "ye", "yt", "za", "zm", "zw"
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
            result_line = f"✅ {domain}  ➜  {ip}"
        else:
            not_found.append(domain)
            result_line = f"❌ {domain}  ➜  Not found"

        last_domains.append(result_line)
        if len(last_domains) > 5:
            last_domains.pop(0)

        progress = (index / total) * 100

        sys.stdout.write('\033[2J\033[H')

        print_neon("\n🔍 Starting domain testing for: " + name, Colors.NEON_PURPLE)
        print_neon("=" * 60, Colors.NEON_PINK)
        print_neon(f"⏰ Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", Colors.NEON_YELLOW)
        print_neon("🌐 Using Google DNS (8.8.8.8) for accurate results", Colors.NEON_BLUE)
        print_neon("-" * 60, Colors.NEON_ORANGE)

        bar_length = 50
        filled = int(bar_length * index / total)
        bar = '█' * filled + '░' * (bar_length - filled)
        print_neon(f"\r📊 Progress: {bar} {index}/{total} ({progress:.1f}%)", Colors.NEON_CYAN)

        print_neon(f"✅ Found: {len(found)}  ❌ Not found: {len(not_found)}", Colors.NEON_GREEN if found else Colors.NEON_RED)
        print_neon("-" * 60, Colors.NEON_ORANGE)

        for line in last_domains:
            if "✅" in line:
                print_neon(line, Colors.NEON_GREEN)
            else:
                print_neon(line, Colors.NEON_RED)

        sys.stdout.flush()

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
        print_neon("⚠️  dnspython is not installed. Installing...", Colors.NEON_YELLOW)
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
