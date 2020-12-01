import sys
import logging

logging.basicConfig(
    format="%(asctime)s [%(levelname)s:%(lineno)s] [%(name)s] %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


def main():
    logger.info("Hello! こんにちは! 123")
    logger.info("これはmain.pyでの出力の例です")


if __name__ == "__main__":
    sys.exit(main())
