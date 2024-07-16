# coding: utf-8

"""
    Visier Public Platform APIs

    Visier APIs for querying data and model metadata

    The version of the OpenAPI document: 22222222.99201.1371
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.model_query_apis.models.dimension_reference_dto import DimensionReferenceDTO

class TestDimensionReferenceDTO(unittest.TestCase):
    """DimensionReferenceDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DimensionReferenceDTO:
        """Test DimensionReferenceDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DimensionReferenceDTO`
        """
        model = DimensionReferenceDTO()
        if include_optional:
            return DimensionReferenceDTO(
                name = '',
                qualifying_path = ''
            )
        else:
            return DimensionReferenceDTO(
        )
        """

    def testDimensionReferenceDTO(self):
        """Test DimensionReferenceDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
