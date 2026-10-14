# Generates input/images/apix-before-after.svg (home-page before/after graphic).
# Usage (from repo root): python3 parking/apix-before-after-gen.py && mv apix-before-after.svg input/images/
# Edit labels, colours, or the per-country method lists (`methods`) below. No dependencies.
W,H=1200,700
NAVY='#1e2f5c'; TEAL='#0f7a8a'; RED='#c2410c'; GREEN='#047857'; INK='#111827'; MUTED='#6b7280'
F="font-family=\"Inter, 'Segoe UI', Helvetica, Arial, sans-serif\""
o=[]
a=o.append
a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-labelledby="t d">')
a('<title id="t">Before and after RWI-pharma</title>')
a('<desc id="d">Before: industry connects to each regulator with different exchange methods (email, secure email, FTP, AS2, HTTPS, portals, mail) that vary by product type, procedure, and country. After: industry uses one standardized FHIR API connection pattern with every regulator, regardless of product type, procedure, or country.</desc>')
a('<rect width="100%" height="100%" fill="#ffffff"/>')
# panels
a(f'<rect x="0" y="0" width="592" height="{H}" fill="#f6f7fb"/>')
a(f'<rect x="608" y="0" width="592" height="{H}" fill="#f2f9f9"/>')
a(f'<rect x="0" y="0" width="592" height="64" fill="{NAVY}"/>')
a(f'<rect x="608" y="0" width="592" height="64" fill="{TEAL}"/>')
a(f'<text x="296" y="41" text-anchor="middle" {F} font-size="20" font-weight="800" letter-spacing="2" fill="#fff">BEFORE: FRAGMENTED</text>')
a(f'<text x="904" y="41" text-anchor="middle" {F} font-size="20" font-weight="800" letter-spacing="2" fill="#fff">AFTER: ONE STANDARD</text>')
a(f'<text x="296" y="100" text-anchor="middle" {F} font-size="15" font-weight="600" fill="{MUTED}">A different exchange method for every combination</text>')
a(f'<text x="904" y="100" text-anchor="middle" {F} font-size="15" font-weight="600" fill="{MUTED}">The same connection pattern with every regulator</text>')

def industry(cx,cy,col):
    a(f'<circle cx="{cx}" cy="{cy}" r="46" fill="#fff" stroke="{col}" stroke-width="4"/>')
    # two towers
    a(f'<rect x="{cx-22}" y="{cy-14}" width="18" height="34" rx="2" fill="{col}"/>')
    a(f'<rect x="{cx+2}" y="{cy-26}" width="20" height="46" rx="2" fill="{col}"/>')
    for i in range(3):
        for j in range(2):
            a(f'<rect x="{cx+6+j*8}" y="{cy-20+i*11}" width="4" height="6" fill="#fff"/>')
        a(f'<rect x="{cx-17}" y="{cy-8+i*9}" width="8" height="4" fill="#fff"/>')
    a(f'<text x="{cx}" y="{cy+72}" text-anchor="middle" {F} font-size="15" font-weight="800" fill="{INK}">INDUSTRY</text>')
    a(f'<text x="{cx}" y="{cy+90}" text-anchor="middle" {F} font-size="12" fill="{MUTED}">Applicant</text>')

def regulator(cx,cy,col,label):
    a(f'<circle cx="{cx}" cy="{cy}" r="34" fill="#fff" stroke="{col}" stroke-width="3.5"/>')
    a(f'<path d="M{cx-18} {cy-6} L{cx} {cy-19} L{cx+18} {cy-6} Z" fill="{col}"/>')
    for k in range(4):
        a(f'<rect x="{cx-15+k*9}" y="{cy-3}" width="5" height="16" fill="{col}"/>')
    a(f'<rect x="{cx-19}" y="{cy+14}" width="38" height="4" fill="{col}"/>')
    a(f'<text x="{cx+46}" y="{cy-2}" {F} font-size="13" font-weight="800" fill="{INK}">REGULATOR</text>')
    a(f'<text x="{cx+46}" y="{cy+15}" {F} font-size="12" fill="{MUTED}">{label}</text>')

def chip(x,y,text,col,fill='#fff',fs=12,bold=700):
    w=len(text)*fs*0.62+20
    a(f'<rect x="{x-w/2:.1f}" y="{y-13}" width="{w:.1f}" height="26" rx="13" fill="{fill}" stroke="{col}" stroke-width="2"/>')
    a(f'<text x="{x}" y="{y+4.5}" text-anchor="middle" {F} font-size="{fs}" font-weight="{bold}" fill="{col}">{text}</text>')

REGY=[185,355,525]
countries=['Country A','Country B','Country C']
# ---- BEFORE ----
ix,iy=96,355
rx=430
methods=[[('Portal','#7c3aed'),('Email','#2563eb'),('Mail','#b45309')],
         [('AS2','#0d9488'),('Secure email','#1d4ed8'),('FTP','#be123c')],
         [('HTTPS','#15803d'),('Portal','#7c3aed'),('Email','#2563eb')]]
def bez(p0,p1,p2,p3,t):
    return tuple((1-t)**3*p0[i]+3*(1-t)**2*t*p1[i]+3*(1-t)*t*t*p2[i]+t**3*p3[i] for i in range(2))
chips=[]
for r,ry in enumerate(REGY):
    for k,(m,c) in enumerate(methods[r]):
        off=(k-1)*9
        P0=(ix+46,iy+off); P3=(rx-34,ry+off*1.3)
        P1=(P0[0]+120,P0[1]+off*3); P2=(P3[0]-120,P3[1]-off*2)
        if r==1:
            P1=(P0[0]+110,P0[1]+(k-1)*62); P2=(P3[0]-110,P3[1]+(k-1)*62)
        a(f'<path d="M{P0[0]} {P0[1]} C{P1[0]} {P1[1]} {P2[0]} {P2[1]} {P3[0]} {P3[1]}" fill="none" stroke="{c}" stroke-width="2.5" stroke-dasharray="{"7 5" if k%2 else "none"}" opacity=".85"/>')
        t=[0.40,0.60,0.80][k] if r!=1 else 0.74
        chips.append((bez(P0,P1,P2,P3,t),m,c))
for (x,y),m,c in chips: chip(round(x),round(y),m,c)
industry(ix,iy,NAVY)
for ry,cn in zip(REGY,countries): regulator(rx,ry,NAVY,cn)
# multiplier strip
a(f'<rect x="40" y="612" width="512" height="56" rx="10" fill="#fff" stroke="#fecaca" stroke-width="2"/>')
a(f'<circle cx="80" cy="631" r="9" fill="{RED}"/>')
a(f'<path d="M76.5 627.5 l7 7 m0 -7 l-7 7" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round"/>')
a(f'<text x="308" y="636" text-anchor="middle" {F} font-size="14" font-weight="800" fill="{RED}">Different pattern per product type, procedure, and country</text>')
a(f'<text x="296" y="656" text-anchor="middle" {F} font-size="12" fill="{MUTED}">Each combination is its own integration, credentials, and tracking.</text>')

# ---- AFTER ----
jx,jy=704,355
qx=1036
for ry in REGY:
    sx,sy=jx+46,jy; ex,ey=qx-34,ry
    a(f'<path d="M{sx} {sy} C{sx+120} {sy} {ex-120} {ey} {ex} {ey}" fill="none" stroke="{TEAL}" stroke-width="6" stroke-linecap="round"/>')
for ry in REGY:
    t=0.62; mx=(jx+46)+((qx-34)-(jx+46))*t
    my=jy+(ry-jy)*(3*t*t-2*t*t*t)
    chip(mx,my,'FHIR API',TEAL,fill='#e6f4f5')
industry(jx,jy,TEAL)
for ry,cn in zip(REGY,countries): regulator(qx,ry,TEAL,cn)
# pattern strip
a(f'<rect x="648" y="612" width="512" height="56" rx="10" fill="#fff" stroke="#a7f3d0" stroke-width="2"/>')
a(f'<circle cx="680" cy="635" r="9" fill="{GREEN}"/>')
a(f'<path d="M675.5 635 l3 3 l6 -6" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>')
a(f'<text x="916" y="640" text-anchor="middle" {F} font-size="14" font-weight="800" fill="{GREEN}">Same pattern, no matter the product, procedure, or country</text>')
a(f'<text x="904" y="658" text-anchor="middle" {F} font-size="12" fill="{MUTED}">Task · DocumentReference · Binary · Subscription</text>')
# divider arrow
a(f'<rect x="592" y="0" width="16" height="{H}" fill="#ffffff"/>')
a(f'<circle cx="600" cy="355" r="22" fill="#fff" stroke="#d1d5db" stroke-width="2"/>')
a(f'<path d="M591 355 h16 m-6 -7 l7 7 l-7 7" fill="none" stroke="{INK}" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>')
a('</svg>')
open('apix-before-after.svg','w').write('\n'.join(o))
