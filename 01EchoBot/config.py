#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "5a40ed0e-459b-41f4-8ca1-940d8da01ce9")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "4w4HnA-_g~KSpI5vN~.2To.qE82VOjAiqR")
