# coding: utf-8

"""
    Visier Public Platform APIs

    Visier APIs for querying data and model metadata

    The version of the OpenAPI document: 22222222.99201.1371
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.model_query_apis.models.list_query_execution_dto import ListQueryExecutionDTO

class TestListQueryExecutionDTO(unittest.TestCase):
    """ListQueryExecutionDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListQueryExecutionDTO:
        """Test ListQueryExecutionDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListQueryExecutionDTO`
        """
        model = ListQueryExecutionDTO()
        if include_optional:
            return ListQueryExecutionDTO(
                columns = [
                    visier.model_query_apis.models.property_column_dto.PropertyColumnDTO(
                        column_definition = null, 
                        column_name = '', )
                    ],
                filters = [
                    visier.model_query_apis.models.query_filter_dto.QueryFilterDTO(
                        cohort = null, 
                        formula = '', 
                        member_set = null, 
                        selection_concept = null, )
                    ],
                options = visier.model_query_apis.models.list_query_execution_options_dto.ListQueryExecutionOptionsDTO(
                    calendar_type = 'TENANT_CALENDAR', 
                    currency_conversion_code = '', 
                    currency_conversion_date = '', 
                    currency_conversion_mode = 'TENANT_CURRENCY_CONVERSION', 
                    date_time_display_mode = 'EPOCH', 
                    limit = 56, 
                    multiple_tables = True, 
                    omit_header = True, 
                    page = 56, 
                    query_mode = 'DEFAULT', 
                    record_mode = 'NORMAL', ),
                parameter_values = [
                    visier.model_query_apis.models.query_parameter_value_dto.QueryParameterValueDTO(
                        aggregation_type_value = null, 
                        member_value = null, 
                        numeric_value = null, 
                        plan_value = null, )
                    ],
                sort_options = [
                    visier.model_query_apis.models.sort_option_dto.SortOptionDTO(
                        column_index = 56, 
                        sort_direction = 'SORT_ASCENDING', )
                    ],
                source = visier.model_query_apis.models.list_query_source_dto.ListQuerySourceDTO(
                    analytic_object = '', 
                    formula = '', 
                    metric = '', ),
                time_interval = visier.model_query_apis.models.query_time_interval_dto.QueryTimeIntervalDTO(
                    direction = 'BACKWARD', 
                    dynamic_date_from = '', 
                    from_date_time = '', 
                    from_instant = '', 
                    interval_period_count = 56, 
                    interval_period_type = 'MONTH', 
                    shift = null, )
            )
        else:
            return ListQueryExecutionDTO(
        )
        """

    def testListQueryExecutionDTO(self):
        """Test ListQueryExecutionDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
