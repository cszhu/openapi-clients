# coding: utf-8

"""
    Visier Public Platform APIs

    Visier APIs for querying data and model metadata

    The version of the OpenAPI document: 22222222.99201.1371
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.model_query_apis.models.list_query_source_dto import ListQuerySourceDTO

class TestListQuerySourceDTO(unittest.TestCase):
    """ListQuerySourceDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListQuerySourceDTO:
        """Test ListQuerySourceDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListQuerySourceDTO`
        """
        model = ListQuerySourceDTO()
        if include_optional:
            return ListQuerySourceDTO(
                analytic_object = '',
                formula = '',
                metric = ''
            )
        else:
            return ListQuerySourceDTO(
        )
        """

    def testListQuerySourceDTO(self):
        """Test ListQuerySourceDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
