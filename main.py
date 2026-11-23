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
    # Self-check against the competition gate before writing: exactly one
    # sentence, 1-300 characters, not only whitespace.
    assert 1 <= len(STORY) <= 300, len(STORY)
    assert STORY.count(".") == 1, "entry must be exactly one sentence"
    assert STORY.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(STORY)


if __name__ == "__main__":
    main()
