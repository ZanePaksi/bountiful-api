import os, json, logging

class SearchBuilder:

    def __init__(self, table, alt_select='*'):
        self.table = table
        self.select = alt_select
        self.base_query = f"SELECT {self.select} FROM {self.table}"

    def build_conditional_query(self, func_get_conditionals=None, search_parameters={}):
        conditionals = []
        if search_parameters and func_get_conditionals:
            conditionals = func_get_conditionals(search_parameters)
            if conditionals:
                return f"{self.base_query} WHERE {' AND '.join(conditionals)}"
        return self.base_query

class BountySearchBuilder(SearchBuilder):

    def __init__(self, table, alt_select='*'):
        super().__init__(table, alt_select)

    def build_search_query(self, search_parameters):
        return super().build_conditional_query(self.get_bounty_conditionals, search_parameters)

    def get_bounty_conditionals(self, search_parameters):
        conditionals = []
        if 'hunter' in search_parameters and search_parameters['hunter'].isdigit():
            conditionals.append(f"hunter_id = {search_parameters['hunter']}")
        if 'creator' in search_parameters and search_parameters['creator'].isdigit():
            conditionals.append(f"creator_id = {search_parameters['creator']}")
        if 'value:above' in search_parameters and search_parameters['value:above'].isdigit() and int(search_parameters['value:above']) > 0:
            conditionals.append(f"value >= {search_parameters['value:above']}")
        # if 'value:below' in search_parameters and self.__verify_value_params(search_parameters):
        #     conditionals.append(f"value <= {search_parameters['value:below']}")
        return conditionals

class UserSearchBuilder(SearchBuilder):

    def __init__(self, table, alt_select='*'):
        super().__init__(table, alt_select)

    def build_search_query(self, search_parameters):
        return super().build_conditional_query(self.get_user_conditionals, search_parameters)

    def get_user_conditionals(self, search_parameters):
        conditionals = []
        if 'username' in search_parameters and not search_parameters['username'].isdigit():
            conditionals.append(f"username = '{search_parameters['username']}'")
        return conditionals
