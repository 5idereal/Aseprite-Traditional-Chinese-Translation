import logging
import os

from aseprite_ini import Aseini

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('format')

project_root_dir = os.path.dirname(__file__)
strings_dir = os.path.join(project_root_dir, 'assets', 'strings')
data_dir = os.path.join(project_root_dir, 'data')


def main():
    strings_en = Aseini.pull_strings()
    strings_en.fallback(Aseini.pull_strings('v1.3-rc6'))
    strings_en.fallback(Aseini.pull_strings('v1.2.40'))
    strings_en.save(os.path.join(strings_dir, 'en.ini'))
    logger.info("Update strings: 'en'")

    zh_hant_file_path = os.path.join(data_dir, 'zh-hant.ini')
    strings_zh_hant = Aseini.load(zh_hant_file_path)
    strings_zh_hant.save(zh_hant_file_path, strings_en)
    logger.info("Update strings: 'zh-hant'")

    translated, total = strings_zh_hant.coverage(strings_en)
    progress = translated / total
    finished_emoji = '🚩' if progress == 1 else '🚧'
    print(f'progress: {translated} / {total} ({progress:.2%} {finished_emoji})')


if __name__ == '__main__':
    main()