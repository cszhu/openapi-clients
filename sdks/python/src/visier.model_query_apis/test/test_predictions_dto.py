# coding: utf-8

"""
    Visier Public Platform APIs

    Visier APIs for querying data and model metadata

    The version of the OpenAPI document: 22222222.99201.1371
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.model_query_apis.models.predictions_dto import PredictionsDTO

class TestPredictionsDTO(unittest.TestCase):
    """PredictionsDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PredictionsDTO:
        """Test PredictionsDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PredictionsDTO`
        """
        model = PredictionsDTO()
        if include_optional:
            return PredictionsDTO(
                predictions = [
                    visier.model_query_apis.models.prediction_dto.PredictionDTO(
                        data_end_date = '', 
                        data_start_date = '', 
                        description = '', 
                        display_name = '', 
                        event = '', 
                        event_filter = '', 
                        factor_concepts = [
                            ''
                            ], 
                        factor_dimensions = [
                            ''
                            ], 
                        factor_properties = [
                            ''
                            ], 
                        factors_name = '', 
                        id = '', 
                        is_multi_tenant = True, 
                        label_property = '', 
                        minimum_training_months = '', 
                        score_name = '', 
                        subject = '', 
                        subject_filter = '', 
                        subject_key = '', 
                        subject_parent_key = '', )
                    ]
            )
        else:
            return PredictionsDTO(
        )
        """

    def testPredictionsDTO(self):
        """Test PredictionsDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
