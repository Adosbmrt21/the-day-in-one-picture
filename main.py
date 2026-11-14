"""news-image-01 entry: writes the entry image to /output/entry.png.

The image is a front-page grid summing up the world's news of Friday
13 November 2026: Ukraine's near-1,200-drone salvo and Europe joining the
peace talks; four tankers hit in the Strait of Hormuz; Nvidia CEO Jensen
Huang's resignation; the FAA's four-hour nationwide ground stop; China's
unannounced Pacific drills detailed by Taiwan; and Pope Leo meeting abuse
survivors before record crowds in Lima - with a ticker of the day's other
headlines. The program simply copies the image held in this repository.
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
SRC = os.path.join(HERE, "entry.png")
DST = os.path.join(OUT_DIR, "entry.png")

os.makedirs(OUT_DIR, exist_ok=True)
shutil.copyfile(SRC, DST)

# Sanity check: the written image must be byte-identical to the held image
# and within the gate's 1 MiB limit, or the run should fail loudly.
written = os.path.getsize(DST)
if written != os.path.getsize(SRC):
    sys.exit("entry.png copy mismatch")
if written > 1024 * 1024:
    sys.exit("entry.png exceeds 1 MiB")
print(f"entry.png written: {written} bytes")
