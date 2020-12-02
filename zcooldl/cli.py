"""Console script for zcooldl."""
import sys

import click
from termcolor import colored

from zcooldl import __version__
from zcooldl.utils import parse_resources
from zcooldl.zcooldl import MAX_WORKERS, RETRIES, ZCoolScraper


@click.command()
@click.option('-u', '--usernames', 'names', help='One or more user names, separated by commas.')
@click.option('-i', '--ids', 'ids', help='One or more user IDs, separated by commas.')
@click.option('-c', '--collections', 'collections', help='One or more collection URLs, separated by commas.')
@click.option('-t', '--topics', 'topics', help='Specific topics to download, separated by commas.')
@click.option('-d', '--destination', 'destination', help='Destination to save images.')
@click.option('-R', '--retries', 'retries', default=RETRIES, show_default=True, type=int,
              help='Repeat download for failed images.')
@click.option('-r', '--redownload', 'redownload',
              help='Redownload images from failed records (PATH of the .json file).')
@click.option('-o', '--overwrite', 'overwrite', is_flag=True, help='Override the existing files.')
@click.option('--thumbnail', 'thumbnail', is_flag=True,
              help='Download thumbnails with a maximum width of 1280px.')
@click.option('--max-pages', 'max_pages', type=int, help='Maximum pages to download.')
@click.option('--max-topics', 'max_topics', type=int, help='Maximum topics per page to download.')
@click.option('--max-workers', 'max_workers', default=MAX_WORKERS, show_default=True, type=int,
              help='Maximum thread workers.')
@click.option('-V', '--version', is_flag=True, help='Show ZCool Downloader version and exit.')
def main(ids, names, collections, destination, max_pages, topics, max_topics,
         max_workers, retries, redownload, overwrite, thumbnail, version):
    """ZCool picture crawler, download pictures, photos and illustrations of
    ZCool (https://zcool.com.cn/). Visit https://github.com/lonsty/zcooldl.
    """
    if version:
        click.echo(f'ZCool Downloader Version: {colored(__version__, "cyan")}')
        return 0

    if redownload:
        scraper = ZCoolScraper(destination=destination, max_pages=max_pages, spec_topics=topics,
                               max_topics=max_topics, max_workers=max_workers, retries=retries,
                               redownload=redownload, overwrite=overwrite, thumbnail=thumbnail)
        scraper.run_scraper()

    elif any([ids, names, collections]):
        topics = topics.split(',') if topics else []
        resources = parse_resources(ids, names, collections)
        for res in resources:
            scraper = ZCoolScraper(user_id=res.id, username=res.name, collection=res.collection,
                                   destination=destination, max_pages=max_pages, spec_topics=topics,
                                   max_topics=max_topics, max_workers=max_workers, retries=retries,
                                   redownload=redownload, overwrite=overwrite)
            scraper.run_scraper()

    else:
        click.echo('Try "python crawler.py --help" for help.')
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
