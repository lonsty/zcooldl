=====
Usage
=====

To use ZCool Downloader in terminal:

.. code-block:: console

    $ zcooldl -u <username>

Type `zcooldl --help` to get full usage:

.. code-block:: none

    Usage: zcooldl [OPTIONS]

      ZCool picture crawler. Download ZCool (https://www.zcool.com.cn/)
      Designer's or User's pictures, photos and illustrations.

    Options:
      -u, --usernames TEXT    One or more user names, separated by commas.
      -i, --ids TEXT          One or more user ids, separated by commas.
      -t, --topics TEXT       Specific topics of this user to download, separated
                              by commas.
      -d, --destination TEXT  Destination to save images.
      -R, --retries INTEGER   Repeat download for failed images.  [default: 3]
      -r, --redownload TEXT   Redownload images from failed records.
      -o, --overwrite         Override existing files.
      --thumbnail             Download thumbnails with a maximum width of 1280px.
      --max-pages INTEGER     Maximum pages to download.
      --max-topics INTEGER    Maximum topics per page to download.
      --max-workers INTEGER   Maximum thread workers.  [default: 20]
      --help                  Show this message and exit.
