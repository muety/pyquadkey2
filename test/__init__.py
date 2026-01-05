from unittest import TestLoader, TestSuite, TextTestRunner


def run():
    from test import quadkey_test, tilesystem_test, util_test

    loader: TestLoader = TestLoader()
    suite: TestSuite = TestSuite()
    suite.addTests(loader.loadTestsFromModule(quadkey_test))
    suite.addTests(loader.loadTestsFromModule(tilesystem_test))
    suite.addTests(loader.loadTestsFromModule(util_test))
    TextTestRunner().run(suite)


if __name__ == '__main__':
    run()
