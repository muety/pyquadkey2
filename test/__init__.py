from unittest import TestLoader, TestSuite, TextTestRunner


def run():
    from test import test_quadkey, test_util
    from test.tilesystem import test_tilesystem

    loader: TestLoader = TestLoader()
    suite: TestSuite = TestSuite()
    suite.addTests(loader.loadTestsFromModule(test_quadkey))
    suite.addTests(loader.loadTestsFromModule(test_tilesystem))
    suite.addTests(loader.loadTestsFromModule(test_util))
    TextTestRunner().run(suite)


if __name__ == '__main__':
    run()
