from PIL import Image
import numpy as np, os, glob

d = "."
files = sorted(glob.glob("*.png"))

def analyze(path):
    im = Image.open(path).convert("RGB")
    w,h = im.size
    a = np.asarray(im, dtype=np.float32)
    mean = a.reshape(-1,3).mean(0)
    corners=[]
    for (cx,cy) in [(30,h-30),(30,30),(w-30,30),(w-30,h-30)]:
        block = a[max(0,cy-20):cy+20, max(0,cx-20):cx+20].reshape(-1,3)
        corners.append(block.mean(0))
    cm = np.array(corners).mean(0)
    white = (a.sum(2) > 3*230).mean()
    dark = (a.sum(2) < 3*70).mean()
    return w,h,mean,cm,white,dark

print(f"{'name':14} {'wh':10} {'meanRGB':18} {'cornerRGB':18} {'%white':7} {'%dark':7}")
for f in files:
    name=os.path.basename(f)
    w,h,m,cm,white,dark=analyze(f)
    print(f"{name:14} {f'{w}x{h}':10} {str(np.round(m,1).tolist()):18} {str(np.round(cm,1).tolist()):18} {white*100:6.1f}% {dark*100:6.1f}%")
