"""
    Ory APIs

    Documentation for all public and administrative Ory APIs. Administrative APIs can only be accessed with a valid Personal Access Token. Public APIs are mostly used in browsers.   # noqa: E501

    The version of the OpenAPI document: v0.0.1-alpha.57
    Contact: support@ory.sh
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import ory_client
from ory_client.model.project_lookup_secret_config import ProjectLookupSecretConfig
from ory_client.model.project_password_config import ProjectPasswordConfig
from ory_client.model.project_recovery_config import ProjectRecoveryConfig
from ory_client.model.project_totp_config import ProjectTotpConfig
from ory_client.model.project_verification_config import ProjectVerificationConfig
from ory_client.model.project_web_authn_config import ProjectWebAuthnConfig
from ory_client.model.redirection_config import RedirectionConfig
globals()['ProjectLookupSecretConfig'] = ProjectLookupSecretConfig
globals()['ProjectPasswordConfig'] = ProjectPasswordConfig
globals()['ProjectRecoveryConfig'] = ProjectRecoveryConfig
globals()['ProjectTotpConfig'] = ProjectTotpConfig
globals()['ProjectVerificationConfig'] = ProjectVerificationConfig
globals()['ProjectWebAuthnConfig'] = ProjectWebAuthnConfig
globals()['RedirectionConfig'] = RedirectionConfig
from ory_client.model.project_patch import ProjectPatch


class TestProjectPatch(unittest.TestCase):
    """ProjectPatch unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testProjectPatch(self):
        """Test ProjectPatch"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ProjectPatch()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
