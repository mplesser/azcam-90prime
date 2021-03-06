gapX = 118.074  # gaps between amplifiers and CCDs (in pixels)
gapY = 363.978


detector_bok90prime = {
    "name": "bok90prime",
    "description": "90prime mosaic",
    "ref_pixel": [4091.04, 4277.99],
    "format": [4032 * 2, 6, 0, 20, 4096 * 2, 0, 0, 0, 0],
    "focalplane": [2, 2, 4, 4, "3210321001230123"],
    "roi": [1, 4032 * 2, 1, 4096 * 2, 1, 1],
    "ext_position": [
        [2, 2],
        [1, 2],
        [2, 1],
        [1, 1],
        [4, 2],
        [3, 2],
        [4, 1],
        [3, 1],
        [1, 3],
        [2, 3],
        [1, 4],
        [2, 4],
        [3, 3],
        [4, 3],
        [3, 4],
        [4, 4],
    ],
    "jpg_order": [4, 3, 8, 7, 2, 1, 6, 5, 9, 10, 13, 14, 11, 12, 15, 16],
    "det_number": [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4],
    "det_position": [
        [1, 1],
        [1, 1],
        [1, 1],
        [1, 1],
        [2, 1],
        [2, 1],
        [2, 1],
        [2, 1],
        [1, 2],
        [1, 2],
        [1, 2],
        [1, 2],
        [2, 2],
        [2, 2],
        [2, 2],
        [2, 2],
    ],
    "det_gap": [
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [gapX, 0],
        [gapX, 0],
        [gapX, 0],
        [gapX, 0],
        [0, gapY],
        [0, gapY],
        [0, gapY],
        [0, gapY],
        [gapX, gapY],
        [gapX, gapY],
        [gapX, gapY],
        [gapX, gapY],
    ],
    "ext_name": [
        "im4",
        "im3",
        "im2",
        "im1",
        "im8",
        "im7",
        "im6",
        "im5",
        "im9",
        "im10",
        "im11",
        "im12",
        "im13",
        "im14",
        "im15",
        "im16",
    ],
    "ext_number": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
}

detector_bok90prime_one = {
    "name": "bok90prime_one",
    "description": "90prime mosaic in single chip mode",
    "ref_pixel": [2016.0, 2048.0],
    "format": [4032, 6, 0, 20, 4096, 0, 0, 0, 0],
    "focalplane": [1, 1, 2, 2, "0123"],
    "roi": [1, 4032, 1, 4096, 1, 1],
    "ext_position": [[1, 1], [2, 1], [1, 2], [2, 2]],
    "jpg_order": [1, 2, 3, 4],
}

detector_bok90prime_6k = {
    "name": "bok90prime_6k",
    "description": "6k CCD",
    "ref_pixel": [3060.0, 3060.0],
    "format": [6120, 0, 0, 20, 6120, 0, 0, 0, 0],
    "focalplane": [1, 1, 2, 2, "0123"],
    "roi": [1, 6120, 1, 6120, 1, 1],
    "ext_position": [[1, 1], [2, 1], [1, 2], [2, 2]],
    "jpg_order": [1, 2, 3, 4],
    "amp_cfg": [0, 1, 2, 3],
    "ext_number": [1, 2, 3, 4],
    "det_number": [1, 1, 1, 1],
    "det_position": [
        [1, 1],
        [1, 1],
        [1, 1],
        [1, 1],
    ],
    "det_gap": [
        [0.0, 0.0],
        [0.0, 0.0],
        [0.0, 0.0],
        [0.0, 0.0],
    ],
    "amp_position": [
        [1, 1],
        [2, 1],
        [1, 2],
        [2, 2],
    ],
    "amp_pixel_position": [
        [1, 1],
        [6120, 1],
        [1, 6120],
        [6120, 1],
    ],
    "ext_name": [
        "im1",
        "im2",
        "im3",
        "im4",
    ],
}
