"""Forensic comparison of the three bug PNGs vs known-genuine MakeCode refs.
Goal: decide whether the bug PNGs plausibly came from a real MakeCode session
(cropped live screenshot) or were fabricated.
"""
from PIL import Image
import os, hashlib, struct, zlib, json

HERE = os.path.dirname(os.path.abspath(__file__))

def png_chunks(path):
    """Return list of (type, data) chunks and basic info."""
    with open(path, 'rb') as f:
        data = f.read()
    assert data[:8] == b'\x89PNG\r\n\x1a\n', "not png"
    chunks = []
    i = 8
    w = h = bd = ct = None
    while i < len(data):
        ln = struct.unpack('>I', data[i:i+4])[0]
        ctype = data[i+4:i+8].decode('latin1')
        cdata = data[i+8:i+8+ln]
        chunks.append((ctype, cdata))
        if ctype == 'IHDR':
            w, h, bd, ct = struct.unpack('>IIBB', cdata[:10])
        i += 12 + ln
    return chunks, dict(w=w, h=h, bitdepth=bd, colortype=ct)

def palette(path):
    im = Image.open(path).convert('RGB')
    # downsample histogram
    small = im.resize((200, 200))
    hs = small.getcolors(200*200)
    # top colors
    hs.sort(reverse=True)
    return [c for _, c in hs[:12]], im.size

def toolbox_strip(path, left=0, width=270):
    im = Image.open(path).convert('RGB')
    w, h = im.size
    width = min(width, w)
    strip = im.crop((left, 0, left+width, h))
    strip = strip.resize((width, 400))
    return strip

def mse(a, b):
    pa = list(a.getdata()); pb = list(b.getdata())
    if len(pa) != len(pb):
        # resize match
        b = b.resize(a.size); pb = list(b.getdata())
    s = 0.0
    for (r1,g1,b1),(r2,g2,b2) in zip(pa, pb):
        s += (r1-r2)**2 + (g1-g2)**2 + (b1-b2)**2
    return s / len(pa) / 3.0

files = {
    'img-19.png': 'REF (claimed real MakeCode)',
    'img-20.png': 'REF (claimed real MakeCode close-up)',
    'img-20-bug1.png': 'BUG1 (on start+show string)',
    'img-20-bug2.png': 'BUG2 (forever+show string Hello!)',
    'img-20-bug3.png': 'BUG3 (empty forever + loose show string)',
    'img-19-labelled-a.png': 'LABELLED-A',
    'img-19-labelled-b.png': 'LABELLED-B',
    'img-05-led.png': 'LED crop',
}

print("=== SIZE / METADATA ===")
for fn in files:
    p = os.path.join(HERE, fn)
    if not os.path.exists(p):
        print(fn, "MISSING"); continue
    chunks, info = png_chunks(p)
    types = [c for c,_ in chunks]
    pal, size = palette(p)
    # look for tEXt/iTXt with software
    software = None
    for c, d in chunks:
        if c in ('tEXt','iTXt','zTXt'):
            try: software = d[:60]
            except: pass
    print(f"{fn:24} {str(size):12} ct={info['colortype']} chunks={types} soft={software}")

print("\n=== TOOLBOX STRIP MSE (lower = more similar) ===")
strips = {}
for fn in files:
    p = os.path.join(HERE, fn)
    if os.path.exists(p):
        strips[fn] = toolbox_strip(p)

# compare each bug strip to img-19 strip
ref = strips.get('img-19.png')
if ref is not None:
    for fn in ['img-20-bug1.png','img-20-bug2.png','img-20-bug3.png','img-19-labelled-a.png','img-19-labelled-b.png']:
        if fn in strips:
            print(f"  {fn:24} vs img-19 toolbox MSE = {mse(ref, strips[fn]):.1f}")

print("\n=== SHA256 ===")
for fn in files:
    p = os.path.join(HERE, fn)
    if os.path.exists(p):
        print(fn, hashlib.sha256(open(p,'rb').read()).hexdigest()[:16])
