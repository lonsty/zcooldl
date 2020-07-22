"""Console script for zcooldl."""
import sys
import click

from zcooldl.utils import parse_users
from zcooldl.zcooldl import ZCoolScraper, RETRIES, MAX_WORKERS


@click.command()
@click.option('-u', '--usernames', 'names', help='One or more user names, separated by commas.')
@click.option('-i', '--ids', 'ids', help='One or more user ids, separated by commas.')
@click.option('-t', '--topics', 'topics', help='Specific topics of this user to download, separated by commas.')
@click.option('-d', '--destination', 'destination', help='Destination to save images.')
@click.option('-R', '--retries', 'retries', default=RETRIES, show_default=True, type=int,
              help='Repeat download for failed images.')
@click.option('-r', '--redownload', 'redownload', help='Redownload images from failed records.')
@click.option('-o', '--overwrite', 'overwrite', is_flag=True, default=False, help='Override existing files.')
@click.option('--thumbnail', 'thumbnail', is_flag=True, default=False,
              help='Download thumbnails with a maximum width of 1280px.')
@click.option('--max-pages', 'max_pages', type=int, help='Maximum pages to download.')
@click.option('--max-topics', 'max_topics', type=int, help='Maximum topics per page to download.')
@click.option('--max-workers', 'max_workers', default=MAX_WORKERS, show_default=True, type=int,
              help='Maximum thread workers.')
def main(ids, names, destination, max_pages, topics, max_topics,
         max_workers, retries, redownload, overwrite, thumbnail):
    """ZCool picture crawler. Download ZCool (https://www.zcool.com.cn/)
    Designer's or User's pictures, photos and illustrations.
    """
    if redownload:
        scraper = ZCoolScraper(destination=destination, max_pages=max_pages, spec_topics=topics,
                               max_topics=max_topics, max_workers=max_workers, retries=retries,
                               redownload=redownload, overwrite=overwrite, thumbnail=thumbnail)
        scraper.run_scraper()

    elif ids or names:
        topics = topics.split(',') if topics else []
        users = parse_users(ids, names)
        for user in users:
            scraper = ZCoolScraper(user_id=user.id, username=user.name, destination=destination,
                                   max_pages=max_pages, spec_topics=topics, max_topics=max_topics,
                                   max_workers=max_workers, retries=retries, redownload=redownload,
                                   overwrite=overwrite)
            scraper.run_scraper()

    else:
        click.echo('Must give an <id> or <username>!')
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
