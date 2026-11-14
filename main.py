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

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

os.makedirs(OUT_DIR, exist_ok=True)
shutil.copyfile(os.path.join(HERE, "entry.png"), os.path.join(OUT_DIR, "entry.png"))
