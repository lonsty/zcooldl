=====
Usage
=====

To use ZCool Downloader in terminal:

* Download all images of an **user**

.. code-block:: console

    $ zcooldl -u <username>

* Download all images of a **collection**

.. code-block:: console

    $ zcooldl -c <collection URL>

Type `zcooldl --help` to get full usage:

.. code-block:: none

    Usage: zcooldl [OPTIONS]

      ZCool picture crawler, download pictures, photos and illustrations of
      ZCool (https://zcool.com.cn/). Visit https://github.com/lonsty/scraper.

    Options:
      -u, --usernames TEXT    One or more user names, separated by commas.
      -i, --ids TEXT          One or more user IDs, separated by commas.
      -c, --collections TEXT  One or more collection URLs, separated by commas.
      -t, --topics TEXT       Specific topics to download, separated by commas.
      -d, --destination TEXT  Destination to save images.
      -R, --retries INTEGER   Repeat download for failed images.  [default: 3]
      -r, --redownload TEXT   Redownload images from failed records (PATH of the
                              .json file).
      -o, --overwrite         Override the existing files.
      --thumbnail             Download thumbnails with a maximum width of 1280px.
      --max-pages INTEGER     Maximum pages to download.
      --max-topics INTEGER    Maximum topics per page to download.
      --max-workers INTEGER   Maximum thread workers.  [default: 20]
      --help                  Show this message and exit.
