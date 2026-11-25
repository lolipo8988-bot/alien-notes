"""Write one alien tourist's review of Earth to /output/entry.txt.

One line, under the 200-character cap: a star rating up front so it
reads as a real review, then a single joke seen from outside — Earth's
plants arm themselves with chemical pain (capsaicin) to stop mammals
eating them, and the mammals treat that defence as a seasoning. The
alien narrator tries one at the end, and the punch lands there.
Plain, concrete words; nothing explains the joke.
"""

import os

TEXT = "3/5 stars. Earth's plants are laced with chemical pain to stop mammals eating them; the mammals call it flavour, hunt the strongest, and weep with joy. I tried one and met my ancestors."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
