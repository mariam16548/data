# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import csv
import os
import pandas as pd
import unittest
from india.geo.districts import IndiaDistrictsMapper


class TestPreprocess(unittest.TestCase):

    def test_get_district_name_to_lgd_code_mapping(self):
        mapper = IndiaDistrictsMapper()
        district_lgd_code = mapper.get_district_name_to_lgd_code_mapping(
            "Karnataka", "bengaluru rural")
        self.assertEqual(district_lgd_code, "526")

        district_lgd_code = mapper.get_district_name_to_lgd_code_mapping(
            "Assam", "karbi anglong")
        self.assertEqual(district_lgd_code, "292")

        district_lgd_code = mapper.get_district_name_to_lgd_code_mapping(
            "Assam", "east karbi anglong")
        self.assertEqual(district_lgd_code, "292")

        district_lgd_code = mapper.get_district_name_to_lgd_code_mapping(
            "tamil nadu", "tuticorin")
        self.assertEqual(district_lgd_code, "594")

        district_lgd_code = mapper.get_district_name_to_lgd_code_mapping(
            "tamilnadu", "thoothukudi")
        self.assertEqual(district_lgd_code, "594")

        district_lgd_code = mapper.get_district_name_to_lgd_code_mapping(
            "karnataka", "vijayanagar")
        self.assertEqual(district_lgd_code, "738")

        district_lgd_code = mapper.get_district_name_to_lgd_code_mapping(
            "karnataka", "vijayapura")
        self.assertEqual(district_lgd_code, "530")

        district_lgd_code = mapper.get_district_name_to_lgd_code_mapping(
            "telangana", "hanamkonda")
        self.assertEqual(district_lgd_code, "686")

        district_lgd_code = mapper.get_district_name_to_lgd_code_mapping(
            "telangana", "warangal")
        self.assertEqual(district_lgd_code, "522")
