# coding: utf-8

"""
    Visier Public Platform APIs

    Visier APIs for querying data and model metadata

    The version of the OpenAPI document: 22222222.99201.1371
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.model_query_apis.models.properties_dto import PropertiesDTO

class TestPropertiesDTO(unittest.TestCase):
    """PropertiesDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PropertiesDTO:
        """Test PropertiesDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PropertiesDTO`
        """
        model = PropertiesDTO()
        if include_optional:
            return PropertiesDTO(
                properties = [
                    visier.model_query_apis.models.property_dto.PropertyDTO(
                        data_type = '', 
                        description = '', 
                        display_name = '', 
                        id = '', 
                        parameters = [
                            visier.model_query_apis.models.parameter_definition_dto.ParameterDefinitionDTO(
                                aggregation_type_parameter = null, 
                                member_parameter = null, 
                                numeric_parameter = null, 
                                plan_parameter = null, )
                            ], 
                        primitive_data_type = '', 
                        tags = [
                            visier.model_query_apis.models.tag_map_element_dto.TagMapElementDTO(
                                display_name = '', 
                                id = '', )
                            ], )
                    ]
            )
        else:
            return PropertiesDTO(
        )
        """

    def testPropertiesDTO(self):
        """Test PropertiesDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
