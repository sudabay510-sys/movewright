from helpers import L, LM, opt, env_names

Q = [
    {"id": "weeks", "type": "choice", "prompt": "How far away is your move?",
     "options": [opt("2", "Under 3 weeks"), opt("5", "3–6 weeks"), opt("9", "6–10 weeks"), opt("12", "10+ weeks")]},
    {"id": "size", "type": "choice", "prompt": "How big is the home you’re leaving?",
     "options": [opt("studio", "Studio / room"), opt("1br", "1 bedroom"), opt("2br", "2–3 bedrooms"), opt("house", "4+ bedrooms / large house")]},
    {"id": "distance", "type": "choice", "prompt": "How far are you moving?",
     "options": [opt("local", "Same city"), opt("region", "Within the state"), opt("long", "Another state"), opt("intl", "Another country")]},
    {"id": "method", "type": "choice", "prompt": "How are you moving your stuff?",
     "options": [opt("diy", "DIY with a rental truck"), opt("labor", "Hired labor only"), opt("full", "Full-service movers"), opt("pod", "Portable container"), opt("unsure", "Not decided")]},
    {"id": "household", "type": "choice", "multi": True, "prompt": "Who’s moving with you?", "help": "Select all that apply.",
     "options": [opt("solo", "Just me"), opt("partner", "Partner / roommates"), opt("kids", "Kids"), opt("pets", "Pets"), opt("plants", "A lot of plants")]},
    {"id": "declutter", "type": "choice", "prompt": "How much do you need to declutter?",
     "options": [opt("little", "Very little"), opt("some", "Some closets & drawers"), opt("lots", "A lot"), opt("estate", "A whole household’s worth")]},
    {"id": "stress", "type": "choice", "prompt": "What stresses you most?",
     "options": [opt("packing", "Packing"), opt("logistics", "Booking movers & dates"), opt("admin", "Address changes & utilities"), opt("kids", "Keeping kids/pets settled"), opt("budget", "Staying on budget")]},
    {"id": "hours", "type": "choice", "prompt": "Hours per week you can give the move?",
     "options": [opt("3", "Under 3"), opt("6", "3–8"), opt("10", "8+")]},
]


def plan(a):
    w = int(a.get("weeks", "5"))
    hh = a.get("household") or []
    extra = []
    if "kids" in hh:
        extra.append("Pack a ‘first night’ box per kid: pajamas, a comfort item, a favorite snack.")
    if "pets" in hh:
        extra.append("Ask your vet for records and find a vet near the new home before moving day.")
    if a.get("distance") in ("long", "intl"):
        extra.append("Check vehicle registration, license, and voter registration rules for your new state or country on official sites.")
    return {
        "title": f"Movewright {w}-week move plan — {L(Q[1]['options'], a.get('size'))}, {L(Q[2]['options'], a.get('distance')).lower()}",
        "summary": f"Moving method: {L(Q[3]['options'], a.get('method')).lower()}. Declutter load: {L(Q[5]['options'], a.get('declutter')).lower()}. Biggest stress: {L(Q[6]['options'], a.get('stress')).lower()}. Movewright is a checklist plan — we don’t book movers or guarantee costs.",
        "preview_sections": [
            {"title": "This week (unlocked)", "bullets": ["Pick your moving day and write it at the top of one shared list.", "Get at least 2–3 written mover or truck quotes and check reviews and licensing (US interstate movers: FMCSA lookup).", "Start declutter with the room you use least."] + extra},
            {"title": "Packing room order", "bullets": ["Storage / garage → guest room → books & decor → closets → kitchen (leave 1 week of basics) → bathroom → bedroom last."]},
            {"title": "Address & utilities", "body": "Set up USPS mail forwarding on the official usps.com site, schedule utility shut-off and start dates, and update your bank, employer, and insurance."},
        ],
        "locked_sections": [
            {"title": "Week-by-week countdown", "teaser": f"All {w} weeks, task by task, sized to your hours."},
            {"title": "Room-by-room packing lists", "teaser": "What to pack when, and how to label boxes."},
            {"title": "Moving-day run sheet", "teaser": "Hour-by-hour plan and an open-first box list."},
            {"title": "First-week setup module", "teaser": "Unpacking order and new-home safety checks."},
        ],
    }


BRAND = {
    "name": "Movewright", "slug": "movewright", "port": 5111,
    "tagline": "A week-by-week moving plan, from first box to first night.",
    "eyebrow": "For households on the move",
    "hero_title": "Move without the last-week meltdown.",
    "hero_lede": "Tell Movewright your move date, home size, and how you’re moving. Get a week-by-week plan for decluttering, packing, booking, and address changes.",
    "cta_primary": "Plan my move", "cta_short": "Start quiz",
    "cta_band_title": "One list. Every week. Then the keys.",
    "cta_band_text": "A plan that fits your timeline, your home, and your people.",
    "honesty_line": "Checklist planning only. We don’t book movers or guarantee costs.",
    "audience_line": "Renters, homeowners, and families moving across town or across the country.",
    "personas": [
        {"title": "First big move", "text": "Leaving a first apartment and not sure where to start."},
        {"title": "Family move", "text": "Kids, pets, and a new school to plan around."},
        {"title": "Long-distance mover", "text": "New state, new license, new everything."},
    ],
    "journey": [
        {"stage": "Decide", "pain": "Not sure DIY or movers.", "fix": "A quote checklist and comparison steps."},
        {"stage": "Declutter", "pain": "Too much stuff, too little time.", "fix": "Room order starting with the least-used space."},
        {"stage": "Pack", "pain": "The kitchen is still full the night before.", "fix": "A room-by-room packing sequence."},
        {"stage": "Arrive", "pain": "Can’t find the sheets on night one.", "fix": "Open-first boxes and a first-week setup."},
    ],
    "how_steps": [
        {"title": "Quiz your move", "text": "Date, size, distance, method, and household."},
        {"title": "Preview your plan", "text": "This week’s tasks and packing order unlocked."},
        {"title": "Join the founding list", "text": "No charge today — we’ll email when checkout opens."},
    ],
    "features": [
        {"title": "Week-by-week countdown", "text": "Sized to your move date and hours."},
        {"title": "Packing order", "text": "Room sequence and labeling system."},
        {"title": "Moving-day run sheet", "text": "Hour-by-hour plan."},
        {"title": "Fixed term", "text": "Pay for your move window — not forever."},
    ],
    "sample_peek": ["2–3 written quotes", "Least-used room first", "USPS forwarding on official site", "Open-first box"],
    "trust_points": [
        {"title": "No mover kickbacks", "text": "We don’t sell your info to moving companies."},
        {"title": "Official links only", "text": "USPS, FMCSA, and DMV steps point to official sites."},
        {"title": "Fixed-term pricing", "text": "Built for your move window, not endless billing."},
    ],
    "faq": [
        {"q": "Do you book movers for me?", "a": "No. We give a checklist for comparing quotes and checking licensing."},
        {"q": "Will it save me money?", "a": "We can’t promise savings. Planning ahead usually helps you compare options calmly."},
        {"q": "Why a fixed term instead of monthly?", "a": "Moves end. Plans run for your move window and don’t auto-renew."},
    ],
    "pricing": [
        {"id": "8w", "name": "8-week move plan", "intro": "$19", "period": "one-time, 8 weeks", "renewal": "no auto-renewal", "renewal_note": "One-time price for the full term. Does not auto-renew.", "includes": ["Week-by-week countdown", "Packing lists", "Moving-day run sheet"]},
        {"id": "12w", "name": "12-week move + settle", "intro": "$29", "period": "one-time, 12 weeks", "renewal": "no auto-renewal", "renewal_note": "One-time price for the full term. Does not auto-renew.", "featured": True, "includes": ["Everything in 8-week", "First-week setup module", "Kids & pets add-ons"]},
    ],
    "disclaimer_short": "Checklist planning only. We don’t book movers, guarantee costs, or give legal advice about leases.",
    "disclaimer_long": "Movewright provides general moving-planning checklists. It does not book or recommend specific movers, guarantee costs or timelines, or give legal advice about leases, contracts, or deposits. Verify mover licensing and official requirements yourself. No payments are processed on this site.",
    "font_url": "https://fonts.googleapis.com/css2?family=Anton&family=Manrope:wght@400;500;700;800&display=swap",
    "fonts": ("Bricolage Grotesque", "Manrope"),
    "questions": Q, "generate_plan": plan,
    "voice": "Upbeat project manager with a tape gun: clear, kind, slightly funny.",
    "palette": {"Background (kraft)": "#F4EDE3", "Alt": "#EADFCF", "Card": "#FFFCF7", "Ink": "#26201A", "Muted": "#6A5E50", "Accent (tape orange)": "#E2711D", "Accent hover": "#C45B0C", "Secondary (navy)": "#1F3A5F"},
    "logo_svg": '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" fill="none"><rect width="64" height="64" rx="10" fill="#1F3A5F"/><path d="M14 24 32 15l18 9v20l-18 9-18-9V24z" fill="#C9A77C" stroke="#F4EDE3" stroke-width="2.5" stroke-linejoin="round"/><path d="M14 24l18 9 18-9M32 33v20" stroke="#F4EDE3" stroke-width="2.5"/><path d="M23 19.5l18 9" stroke="#E2711D" stroke-width="5"/></svg>',
    "css_vars": """
  --bg:#F4EDE3;--bg-alt:#EADFCF;--card:#FFFCF7;--ink:#26201A;--muted:#6A5E50;--line:#DCCDB8;
  --accent:#C45B0C;--accent-2:#A34A08;--on-accent:#FFFFFF;--hi:#E2711D;--radius:10px;
  --font-display:'Bricolage Grotesque', system-ui, sans-serif;--font-body:'Manrope', system-ui, sans-serif;
  --shadow-card:0 14px 30px rgba(38,32,26,.10);--shadow-btn:0 8px 18px rgba(196,91,12,.28);
  --cta-band-bg:#1F3A5F;--cta-band-ink:#F4EDE3;--cta-band-btn:#E2711D;--cta-band-btn-ink:#1A0E03;--tracking:-0.03em;
""",
    "personality": "background:linear-gradient(135deg,#EFDDC4 0%, var(--bg) 50%);",
    "extra_css": "h1{font-weight:800}.journey-card{border-left:6px solid var(--hi)}.badge{background:#1F3A5F;color:#fff}",
    "dos": ["Link only to official sites (USPS, FMCSA, DMV).", "Be clear that terms are fixed and don’t auto-renew."],
    "donts": ["Sell or share leads with movers.", "Promise cost savings or legal outcomes on leases/deposits."],
}
BRAND.update(env_names("movewright"))
