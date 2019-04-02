from django.test.runner import DiscoverRunner

class NoDbTestRunner(DiscoverRunner):
  """ A test runner to test without database creation """

  def setup_databases(self, **kwargs):
    """ Override the database creation defined in parent class """
    assert True

