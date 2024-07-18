# coding: utf-8

"""
    Ory APIs

    Documentation for all public and administrative Ory APIs. Administrative APIs can only be accessed with a valid Personal Access Token. Public APIs are mostly used in browsers. 

    The version of the OpenAPI document: v1.14.2
    Contact: support@ory.sh
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ory_client.models.project_branding import ProjectBranding

class TestProjectBranding(unittest.TestCase):
    """ProjectBranding unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProjectBranding:
        """Test ProjectBranding
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProjectBranding`
        """
        model = ProjectBranding()
        if include_optional:
            return ProjectBranding(
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                default_theme = ory_client.models.project_branding_theme_represents_a_theme_for_the_ory_account_experience/.ProjectBrandingTheme represents a Theme for the Ory Account Experience.(
                    accent_default_color = '', 
                    accent_disabled_color = '', 
                    accent_emphasis_color = '', 
                    accent_muted_color = '', 
                    accent_subtle_color = '', 
                    account_experience_variables = [
                        ory_client.models.account_experience_theme_variables.accountExperienceThemeVariables(
                            accent = '', 
                            bg_default = '', 
                            border_radius_branding = '', 
                            border_radius_buttons = '', 
                            border_radius_cards = '', 
                            border_radius_forms = '', 
                            border_radius_general = '', 
                            button_primary_bg_default = '', 
                            button_primary_bg_disabled = '', 
                            button_primary_bg_hover = '', 
                            button_primary_border_default = '', 
                            button_primary_border_disabled = '', 
                            button_primary_border_hover = '', 
                            button_primary_fg_default = '', 
                            button_primary_fg_disabled = '', 
                            button_primary_fg_hover = '', 
                            button_secondary_bg_default = '', 
                            button_secondary_bg_disabled = '', 
                            button_secondary_bg_hover = '', 
                            button_secondary_border_default = '', 
                            button_secondary_border_disabled = '', 
                            button_secondary_border_hover = '', 
                            button_secondary_fg_default = '', 
                            button_secondary_fg_disabled = '', 
                            button_secondary_fg_hover = '', 
                            button_social_bg_default = '', 
                            button_social_bg_disabled = '', 
                            button_social_bg_hover = '', 
                            button_social_bg_provider = '', 
                            button_social_border_default = '', 
                            button_social_border_disabled = '', 
                            button_social_border_hover = '', 
                            button_social_border_provider = '', 
                            button_social_fg_default = '', 
                            button_social_fg_disabled = '', 
                            button_social_fg_hover = '', 
                            button_social_fg_provider = '', 
                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            dialog_bg_default = '', 
                            dialog_bg_subtle = '', 
                            dialog_border_default = '', 
                            dialog_fg_default = '', 
                            dialog_fg_mute = '', 
                            dialog_fg_subtle = '', 
                            forms_bg_default = '', 
                            forms_bg_disabled = '', 
                            forms_bg_hover = '', 
                            forms_border_default = '', 
                            forms_border_disabled = '', 
                            forms_border_error = '', 
                            forms_border_focus = '', 
                            forms_border_hover = '', 
                            forms_border_success = '', 
                            forms_border_warn = '', 
                            forms_checkbox_bg_checked = '', 
                            forms_checkbox_bg_default = '', 
                            forms_checkbox_border_checked = '', 
                            forms_checkbox_border_default = '', 
                            forms_checkbox_fg_checked = '', 
                            forms_checkbox_fg_default = '', 
                            forms_fg_default = '', 
                            forms_fg_error = '', 
                            forms_fg_mute = '', 
                            forms_fg_subtle = '', 
                            forms_fg_success = '', 
                            forms_fg_warn = '', 
                            forms_radio_bg_checked = '', 
                            forms_radio_bg_default = '', 
                            forms_radio_border_checked = '', 
                            forms_radio_border_default = '', 
                            forms_radio_fg_checked = '', 
                            forms_radio_fg_default = '', 
                            forms_toggle_bg_checked = '', 
                            forms_toggle_bg_default = '', 
                            forms_toggle_border_checked = '', 
                            forms_toggle_border_default = '', 
                            forms_toggle_fg_checked = '', 
                            forms_toggle_fg_default = '', 
                            id = '', 
                            links_link_default = '', 
                            links_link_disabled = '', 
                            links_link_hover = '', 
                            links_link_inverted_default = '', 
                            links_link_inverted_hover = '', 
                            links_link_mute_default = '', 
                            links_link_mute_hover = '', 
                            syntax_syntax = '', 
                            syntax_syntax_key = '', 
                            syntax_syntax_num = '', 
                            syntax_syntax_value = '', 
                            updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                        ], 
                    account_experience_variables_stylesheet = '', 
                    background_canvas_color = '', 
                    background_subtle_color = '', 
                    background_surface_color = '', 
                    border_default_color = '', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    error_default_color = '', 
                    error_emphasis_color = '', 
                    error_muted_color = '', 
                    error_subtle_color = '', 
                    favicon_type = '', 
                    favicon_url = '', 
                    foreground_default_color = '', 
                    foreground_disabled_color = '', 
                    foreground_muted_color = '', 
                    foreground_on_accent_color = '', 
                    foreground_on_dark_color = '', 
                    foreground_on_disabled_color = '', 
                    foreground_subtle_color = '', 
                    id = '', 
                    input_background_color = '', 
                    input_disabled_color = '', 
                    input_placeholder_color = '', 
                    input_text_color = '', 
                    logo_type = '', 
                    logo_url = '', 
                    name = '', 
                    primary_color = '', 
                    project_branding_id = '', 
                    secondary_color = '', 
                    success_emphasis_color = '', 
                    text_default_color = '', 
                    text_disabled_color = '', 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
                id = '',
                project_id = '',
                themes = [
                    ory_client.models.project_branding_theme_represents_a_theme_for_the_ory_account_experience/.ProjectBrandingTheme represents a Theme for the Ory Account Experience.(
                        accent_default_color = '', 
                        accent_disabled_color = '', 
                        accent_emphasis_color = '', 
                        accent_muted_color = '', 
                        accent_subtle_color = '', 
                        account_experience_variables = [
                            ory_client.models.account_experience_theme_variables.accountExperienceThemeVariables(
                                accent = '', 
                                bg_default = '', 
                                border_radius_branding = '', 
                                border_radius_buttons = '', 
                                border_radius_cards = '', 
                                border_radius_forms = '', 
                                border_radius_general = '', 
                                button_primary_bg_default = '', 
                                button_primary_bg_disabled = '', 
                                button_primary_bg_hover = '', 
                                button_primary_border_default = '', 
                                button_primary_border_disabled = '', 
                                button_primary_border_hover = '', 
                                button_primary_fg_default = '', 
                                button_primary_fg_disabled = '', 
                                button_primary_fg_hover = '', 
                                button_secondary_bg_default = '', 
                                button_secondary_bg_disabled = '', 
                                button_secondary_bg_hover = '', 
                                button_secondary_border_default = '', 
                                button_secondary_border_disabled = '', 
                                button_secondary_border_hover = '', 
                                button_secondary_fg_default = '', 
                                button_secondary_fg_disabled = '', 
                                button_secondary_fg_hover = '', 
                                button_social_bg_default = '', 
                                button_social_bg_disabled = '', 
                                button_social_bg_hover = '', 
                                button_social_bg_provider = '', 
                                button_social_border_default = '', 
                                button_social_border_disabled = '', 
                                button_social_border_hover = '', 
                                button_social_border_provider = '', 
                                button_social_fg_default = '', 
                                button_social_fg_disabled = '', 
                                button_social_fg_hover = '', 
                                button_social_fg_provider = '', 
                                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                dialog_bg_default = '', 
                                dialog_bg_subtle = '', 
                                dialog_border_default = '', 
                                dialog_fg_default = '', 
                                dialog_fg_mute = '', 
                                dialog_fg_subtle = '', 
                                forms_bg_default = '', 
                                forms_bg_disabled = '', 
                                forms_bg_hover = '', 
                                forms_border_default = '', 
                                forms_border_disabled = '', 
                                forms_border_error = '', 
                                forms_border_focus = '', 
                                forms_border_hover = '', 
                                forms_border_success = '', 
                                forms_border_warn = '', 
                                forms_checkbox_bg_checked = '', 
                                forms_checkbox_bg_default = '', 
                                forms_checkbox_border_checked = '', 
                                forms_checkbox_border_default = '', 
                                forms_checkbox_fg_checked = '', 
                                forms_checkbox_fg_default = '', 
                                forms_fg_default = '', 
                                forms_fg_error = '', 
                                forms_fg_mute = '', 
                                forms_fg_subtle = '', 
                                forms_fg_success = '', 
                                forms_fg_warn = '', 
                                forms_radio_bg_checked = '', 
                                forms_radio_bg_default = '', 
                                forms_radio_border_checked = '', 
                                forms_radio_border_default = '', 
                                forms_radio_fg_checked = '', 
                                forms_radio_fg_default = '', 
                                forms_toggle_bg_checked = '', 
                                forms_toggle_bg_default = '', 
                                forms_toggle_border_checked = '', 
                                forms_toggle_border_default = '', 
                                forms_toggle_fg_checked = '', 
                                forms_toggle_fg_default = '', 
                                id = '', 
                                links_link_default = '', 
                                links_link_disabled = '', 
                                links_link_hover = '', 
                                links_link_inverted_default = '', 
                                links_link_inverted_hover = '', 
                                links_link_mute_default = '', 
                                links_link_mute_hover = '', 
                                syntax_syntax = '', 
                                syntax_syntax_key = '', 
                                syntax_syntax_num = '', 
                                syntax_syntax_value = '', 
                                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                            ], 
                        account_experience_variables_stylesheet = '', 
                        background_canvas_color = '', 
                        background_subtle_color = '', 
                        background_surface_color = '', 
                        border_default_color = '', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        error_default_color = '', 
                        error_emphasis_color = '', 
                        error_muted_color = '', 
                        error_subtle_color = '', 
                        favicon_type = '', 
                        favicon_url = '', 
                        foreground_default_color = '', 
                        foreground_disabled_color = '', 
                        foreground_muted_color = '', 
                        foreground_on_accent_color = '', 
                        foreground_on_dark_color = '', 
                        foreground_on_disabled_color = '', 
                        foreground_subtle_color = '', 
                        id = '', 
                        input_background_color = '', 
                        input_disabled_color = '', 
                        input_placeholder_color = '', 
                        input_text_color = '', 
                        logo_type = '', 
                        logo_url = '', 
                        name = '', 
                        primary_color = '', 
                        project_branding_id = '', 
                        secondary_color = '', 
                        success_emphasis_color = '', 
                        text_default_color = '', 
                        text_disabled_color = '', 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return ProjectBranding(
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                default_theme = ory_client.models.project_branding_theme_represents_a_theme_for_the_ory_account_experience/.ProjectBrandingTheme represents a Theme for the Ory Account Experience.(
                    accent_default_color = '', 
                    accent_disabled_color = '', 
                    accent_emphasis_color = '', 
                    accent_muted_color = '', 
                    accent_subtle_color = '', 
                    account_experience_variables = [
                        ory_client.models.account_experience_theme_variables.accountExperienceThemeVariables(
                            accent = '', 
                            bg_default = '', 
                            border_radius_branding = '', 
                            border_radius_buttons = '', 
                            border_radius_cards = '', 
                            border_radius_forms = '', 
                            border_radius_general = '', 
                            button_primary_bg_default = '', 
                            button_primary_bg_disabled = '', 
                            button_primary_bg_hover = '', 
                            button_primary_border_default = '', 
                            button_primary_border_disabled = '', 
                            button_primary_border_hover = '', 
                            button_primary_fg_default = '', 
                            button_primary_fg_disabled = '', 
                            button_primary_fg_hover = '', 
                            button_secondary_bg_default = '', 
                            button_secondary_bg_disabled = '', 
                            button_secondary_bg_hover = '', 
                            button_secondary_border_default = '', 
                            button_secondary_border_disabled = '', 
                            button_secondary_border_hover = '', 
                            button_secondary_fg_default = '', 
                            button_secondary_fg_disabled = '', 
                            button_secondary_fg_hover = '', 
                            button_social_bg_default = '', 
                            button_social_bg_disabled = '', 
                            button_social_bg_hover = '', 
                            button_social_bg_provider = '', 
                            button_social_border_default = '', 
                            button_social_border_disabled = '', 
                            button_social_border_hover = '', 
                            button_social_border_provider = '', 
                            button_social_fg_default = '', 
                            button_social_fg_disabled = '', 
                            button_social_fg_hover = '', 
                            button_social_fg_provider = '', 
                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            dialog_bg_default = '', 
                            dialog_bg_subtle = '', 
                            dialog_border_default = '', 
                            dialog_fg_default = '', 
                            dialog_fg_mute = '', 
                            dialog_fg_subtle = '', 
                            forms_bg_default = '', 
                            forms_bg_disabled = '', 
                            forms_bg_hover = '', 
                            forms_border_default = '', 
                            forms_border_disabled = '', 
                            forms_border_error = '', 
                            forms_border_focus = '', 
                            forms_border_hover = '', 
                            forms_border_success = '', 
                            forms_border_warn = '', 
                            forms_checkbox_bg_checked = '', 
                            forms_checkbox_bg_default = '', 
                            forms_checkbox_border_checked = '', 
                            forms_checkbox_border_default = '', 
                            forms_checkbox_fg_checked = '', 
                            forms_checkbox_fg_default = '', 
                            forms_fg_default = '', 
                            forms_fg_error = '', 
                            forms_fg_mute = '', 
                            forms_fg_subtle = '', 
                            forms_fg_success = '', 
                            forms_fg_warn = '', 
                            forms_radio_bg_checked = '', 
                            forms_radio_bg_default = '', 
                            forms_radio_border_checked = '', 
                            forms_radio_border_default = '', 
                            forms_radio_fg_checked = '', 
                            forms_radio_fg_default = '', 
                            forms_toggle_bg_checked = '', 
                            forms_toggle_bg_default = '', 
                            forms_toggle_border_checked = '', 
                            forms_toggle_border_default = '', 
                            forms_toggle_fg_checked = '', 
                            forms_toggle_fg_default = '', 
                            id = '', 
                            links_link_default = '', 
                            links_link_disabled = '', 
                            links_link_hover = '', 
                            links_link_inverted_default = '', 
                            links_link_inverted_hover = '', 
                            links_link_mute_default = '', 
                            links_link_mute_hover = '', 
                            syntax_syntax = '', 
                            syntax_syntax_key = '', 
                            syntax_syntax_num = '', 
                            syntax_syntax_value = '', 
                            updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                        ], 
                    account_experience_variables_stylesheet = '', 
                    background_canvas_color = '', 
                    background_subtle_color = '', 
                    background_surface_color = '', 
                    border_default_color = '', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    error_default_color = '', 
                    error_emphasis_color = '', 
                    error_muted_color = '', 
                    error_subtle_color = '', 
                    favicon_type = '', 
                    favicon_url = '', 
                    foreground_default_color = '', 
                    foreground_disabled_color = '', 
                    foreground_muted_color = '', 
                    foreground_on_accent_color = '', 
                    foreground_on_dark_color = '', 
                    foreground_on_disabled_color = '', 
                    foreground_subtle_color = '', 
                    id = '', 
                    input_background_color = '', 
                    input_disabled_color = '', 
                    input_placeholder_color = '', 
                    input_text_color = '', 
                    logo_type = '', 
                    logo_url = '', 
                    name = '', 
                    primary_color = '', 
                    project_branding_id = '', 
                    secondary_color = '', 
                    success_emphasis_color = '', 
                    text_default_color = '', 
                    text_disabled_color = '', 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
                id = '',
                project_id = '',
                themes = [
                    ory_client.models.project_branding_theme_represents_a_theme_for_the_ory_account_experience/.ProjectBrandingTheme represents a Theme for the Ory Account Experience.(
                        accent_default_color = '', 
                        accent_disabled_color = '', 
                        accent_emphasis_color = '', 
                        accent_muted_color = '', 
                        accent_subtle_color = '', 
                        account_experience_variables = [
                            ory_client.models.account_experience_theme_variables.accountExperienceThemeVariables(
                                accent = '', 
                                bg_default = '', 
                                border_radius_branding = '', 
                                border_radius_buttons = '', 
                                border_radius_cards = '', 
                                border_radius_forms = '', 
                                border_radius_general = '', 
                                button_primary_bg_default = '', 
                                button_primary_bg_disabled = '', 
                                button_primary_bg_hover = '', 
                                button_primary_border_default = '', 
                                button_primary_border_disabled = '', 
                                button_primary_border_hover = '', 
                                button_primary_fg_default = '', 
                                button_primary_fg_disabled = '', 
                                button_primary_fg_hover = '', 
                                button_secondary_bg_default = '', 
                                button_secondary_bg_disabled = '', 
                                button_secondary_bg_hover = '', 
                                button_secondary_border_default = '', 
                                button_secondary_border_disabled = '', 
                                button_secondary_border_hover = '', 
                                button_secondary_fg_default = '', 
                                button_secondary_fg_disabled = '', 
                                button_secondary_fg_hover = '', 
                                button_social_bg_default = '', 
                                button_social_bg_disabled = '', 
                                button_social_bg_hover = '', 
                                button_social_bg_provider = '', 
                                button_social_border_default = '', 
                                button_social_border_disabled = '', 
                                button_social_border_hover = '', 
                                button_social_border_provider = '', 
                                button_social_fg_default = '', 
                                button_social_fg_disabled = '', 
                                button_social_fg_hover = '', 
                                button_social_fg_provider = '', 
                                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                dialog_bg_default = '', 
                                dialog_bg_subtle = '', 
                                dialog_border_default = '', 
                                dialog_fg_default = '', 
                                dialog_fg_mute = '', 
                                dialog_fg_subtle = '', 
                                forms_bg_default = '', 
                                forms_bg_disabled = '', 
                                forms_bg_hover = '', 
                                forms_border_default = '', 
                                forms_border_disabled = '', 
                                forms_border_error = '', 
                                forms_border_focus = '', 
                                forms_border_hover = '', 
                                forms_border_success = '', 
                                forms_border_warn = '', 
                                forms_checkbox_bg_checked = '', 
                                forms_checkbox_bg_default = '', 
                                forms_checkbox_border_checked = '', 
                                forms_checkbox_border_default = '', 
                                forms_checkbox_fg_checked = '', 
                                forms_checkbox_fg_default = '', 
                                forms_fg_default = '', 
                                forms_fg_error = '', 
                                forms_fg_mute = '', 
                                forms_fg_subtle = '', 
                                forms_fg_success = '', 
                                forms_fg_warn = '', 
                                forms_radio_bg_checked = '', 
                                forms_radio_bg_default = '', 
                                forms_radio_border_checked = '', 
                                forms_radio_border_default = '', 
                                forms_radio_fg_checked = '', 
                                forms_radio_fg_default = '', 
                                forms_toggle_bg_checked = '', 
                                forms_toggle_bg_default = '', 
                                forms_toggle_border_checked = '', 
                                forms_toggle_border_default = '', 
                                forms_toggle_fg_checked = '', 
                                forms_toggle_fg_default = '', 
                                id = '', 
                                links_link_default = '', 
                                links_link_disabled = '', 
                                links_link_hover = '', 
                                links_link_inverted_default = '', 
                                links_link_inverted_hover = '', 
                                links_link_mute_default = '', 
                                links_link_mute_hover = '', 
                                syntax_syntax = '', 
                                syntax_syntax_key = '', 
                                syntax_syntax_num = '', 
                                syntax_syntax_value = '', 
                                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                            ], 
                        account_experience_variables_stylesheet = '', 
                        background_canvas_color = '', 
                        background_subtle_color = '', 
                        background_surface_color = '', 
                        border_default_color = '', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        error_default_color = '', 
                        error_emphasis_color = '', 
                        error_muted_color = '', 
                        error_subtle_color = '', 
                        favicon_type = '', 
                        favicon_url = '', 
                        foreground_default_color = '', 
                        foreground_disabled_color = '', 
                        foreground_muted_color = '', 
                        foreground_on_accent_color = '', 
                        foreground_on_dark_color = '', 
                        foreground_on_disabled_color = '', 
                        foreground_subtle_color = '', 
                        id = '', 
                        input_background_color = '', 
                        input_disabled_color = '', 
                        input_placeholder_color = '', 
                        input_text_color = '', 
                        logo_type = '', 
                        logo_url = '', 
                        name = '', 
                        primary_color = '', 
                        project_branding_id = '', 
                        secondary_color = '', 
                        success_emphasis_color = '', 
                        text_default_color = '', 
                        text_disabled_color = '', 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )
        """

    def testProjectBranding(self):
        """Test ProjectBranding"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
