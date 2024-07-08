# coding: utf-8

"""
    Ory APIs

    Documentation for all public and administrative Ory APIs. Administrative APIs can only be accessed with a valid Personal Access Token. Public APIs are mostly used in browsers. 

    The version of the OpenAPI document: v1.13.9
    Contact: support@ory.sh
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ory_client.models.set_project_branding_theme_body import SetProjectBrandingThemeBody

class TestSetProjectBrandingThemeBody(unittest.TestCase):
    """SetProjectBrandingThemeBody unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SetProjectBrandingThemeBody:
        """Test SetProjectBrandingThemeBody
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SetProjectBrandingThemeBody`
        """
        model = SetProjectBrandingThemeBody()
        if include_optional:
            return SetProjectBrandingThemeBody(
                favicon_type = '',
                favicon_url = '',
                logo_type = '',
                logo_url = '',
                name = '',
                theme = ory_client.models.project_branding_colors_are_the_colors_used_by_the_ory_account_experience_theme/.ProjectBrandingColors are the colors used by the Ory Account Experience theme.(
                    accent_default_color = '', 
                    accent_disabled_color = '', 
                    accent_emphasis_color = '', 
                    accent_muted_color = '', 
                    accent_subtle_color = '', 
                    background_canvas_color = '', 
                    background_subtle_color = '', 
                    background_surface_color = '', 
                    border_default_color = '', 
                    error_default_color = '', 
                    error_emphasis_color = '', 
                    error_muted_color = '', 
                    error_subtle_color = '', 
                    foreground_default_color = '', 
                    foreground_disabled_color = '', 
                    foreground_muted_color = '', 
                    foreground_on_accent_color = '', 
                    foreground_on_dark_color = '', 
                    foreground_on_disabled_color = '', 
                    foreground_subtle_color = '', 
                    input_background_color = '', 
                    input_disabled_color = '', 
                    input_placeholder_color = '', 
                    input_text_color = '', 
                    primary_color = '', 
                    secondary_color = '', 
                    success_emphasis_color = '', 
                    text_default_color = '', 
                    text_disabled_color = '', )
            )
        else:
            return SetProjectBrandingThemeBody(
        )
        """

    def testSetProjectBrandingThemeBody(self):
        """Test SetProjectBrandingThemeBody"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
