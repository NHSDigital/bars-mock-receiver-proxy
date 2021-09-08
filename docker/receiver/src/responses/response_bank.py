import os
import json
import sys
import copy

sys.path.append(os.getcwd())

this_directory = os.path.dirname(os.path.realpath(__file__))


class ResponseBank:
    def __init__(self):
        with open(f'{this_directory}/success.json') as f:
            self.__success = json.load(f)

        with open(f'{this_directory}/entity-not-found.json') as f:
            self.__entity_not_found = json.load(f)

        # TODO add the rest of the files with getters. Inside getters deepcopy them so caller can't mutate

    def success(self, resource_type: str = None):
        res = copy.deepcopy(self.__success)
        if resource_type:
            res['resourceType'] = resource_type

        return res

    def entity_not_found(self):
        return copy.deepcopy(self.__entity_not_found)


responses = ResponseBank()
