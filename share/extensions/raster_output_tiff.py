#!/usr/bin/env python
"""
Convert PNG to Tiff using Raster Output extension.
"""

import io
import inkex


class TiffOutput(inkex.RasterOutputExtension):
    def add_arguments(self, pars):
        pars.add_argument("--tab")
        pars.add_argument("--compression", default=None)
        pars.add_argument("--quality", type=int, default=90)

    def save(self, stream):
        tempstream = io.BytesIO()
        self.img.convert("RGB").save(
            tempstream,
            format="tiff",
            compression=(self.options.compression or None),
            quality=100,
        )
        stream.write(tempstream.getvalue())
        # TODO: Add other fields such as copyright etc.


if __name__ == "__main__":
    TiffOutput().run()
