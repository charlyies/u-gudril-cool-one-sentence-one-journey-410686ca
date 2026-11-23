#!/usr/bin/env python3
"""One Sentence, One Journey.

Writes a complete story about a journey, told in exactly one sentence,
to /output/entry.txt.

The story: Mara misses the last ferry off the island and rows after it in
her grandfather's leaking boat (departure), is chased through a storm that
tears her map to ribbons (middle / turn), and discovers that the lighthouse
she always feared is her own front porch light (arrival — somewhere she did
not expect to be). One sentence, concrete detail throughout (leaking boat,
gulls, storm, torn map, porch light), and it closes on a clause that lands.
"""

import os

STORY = (
    "When the last ferry left the island, Mara rowed after it in her "
    "grandfather's leaking boat, following the gulls through a storm that "
    "tore her map to ribbons, until the lighthouse she had always feared "
    "turned out to be her own front porch light."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(STORY)


if __name__ == "__main__":
    main()
