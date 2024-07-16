# coding: utf-8

"""
    Visier Public Platform APIs

    Visier APIs for querying data and model metadata

    The version of the OpenAPI document: 22222222.99201.1371
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.model_query_apis.models.aggregation_query_source_dto import AggregationQuerySourceDTO

class TestAggregationQuerySourceDTO(unittest.TestCase):
    """AggregationQuerySourceDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AggregationQuerySourceDTO:
        """Test AggregationQuerySourceDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AggregationQuerySourceDTO`
        """
        model = AggregationQuerySourceDTO()
        if include_optional:
            return AggregationQuerySourceDTO(
                formula = '',
                metric = '',
                metrics = visier.model_query_apis.models.aggregation_query_source_metrics_dto.AggregationQuerySourceMetricsDTO(
                    columns = [
                        visier.model_query_apis.models.aggregation_query_source_metric_dto.AggregationQuerySourceMetricDTO(
                            column_name = '', 
                            formula = '', 
                            id = '', 
                            qualifying_path = '', )
                        ], )
            )
        else:
            return AggregationQuerySourceDTO(
        )
        """

    def testAggregationQuerySourceDTO(self):
        """Test AggregationQuerySourceDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
