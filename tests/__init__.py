import os
import sys
from unittest import TestLoader, TestSuite, TextTestRunner

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..'))


def run():
    from tests import test_quadkey, test_util
    from tests.tilesystem import test_tilesystem

    loader: TestLoader = TestLoader()
    suite: TestSuite = TestSuite()
    suite.addTests(loader.loadTestsFromModule(test_quadkey))
    suite.addTests(loader.loadTestsFromModule(test_tilesystem))
    suite.addTests(loader.loadTestsFromModule(test_util))
    TextTestRunner().run(suite)


if __name__ == '__main__':
    run()
